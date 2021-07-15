#!/usr/bin/env python

"""
====================================
Filename:         genericImaging.py
Author:           Joseph Farah
Description:      Produce image from observation quickly.
Version:          1.2.0
====================================
Notes
    - This is an example script for the 2021 ngEHT imaging challenges.
    - Example command: python genericImaging.py ../dat/synthetic_data/M87_eht2022_230_thnoise.uvfits
Changelog
    - Version 1.0.0: first production version of file.
    - Version 1.1.0: cleaning up code and adding more explicit comments.
    - Version 1.2.0: Fixed bug found by Nimesh for ngEHT ref1 antenna filename
"""

# ------------- imports ------------- #
import os
import sys
import time
import ehtim as eh


#------------- global script parameters -------------#
T_AVG_COHERENT  = 100           ## coherent averaging time
PRIOR           = "DISC"        ## prior type; can be DISC, FLAT, or EMPTY
DATA_TERM       = 'cphase'      ## imaging data term; e.g., cphase, vis, amp
TTYPE           = 'direct'      ## Fourier transform method; nfft vs direct

#------------- debugging settings -------------#
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def warning(message):
        print(bcolors.WARNING + "[" + message + "]" + bcolors.ENDC)

    @staticmethod
    def success(message):
        print(bcolors.OKGREEN + "[" + message + "]" + bcolors.ENDC)

    @staticmethod
    def failure(message):
        print(bcolors.FAIL + "[" + message + "]" + bcolors.ENDC)



#------------- functions -------------#
def imageObs(obs, prior, save_name="output.fits", d1='bs'):

    """
        Takes an observation and performs several rounds of regularized 
        maximum likelihood imaging (see e.g., Chael et al. 2018).
    
        Args:
            obs (ehtim.obsdata.Obsdata): observation object
            prior (ehtim.image.Image): prior image
            save_name (str): name of output image file
            d1 (str): data product to use for imaging (bs, vis, amp, cphase)
    
        Returns:
            out (ehtim.image.Image): final output image
            outblur (ehtim.image.Image): final image blurred to 15*eh.RADPERUAS
    
    """
     
    
    zbl = 2.3  # zero baseline flux of the image, in Jansky

    #------------- first round of imaging -------------#
    flux = zbl
    tt = time.time()
    out = eh.imager_func(obs, prior, prior, flux,
                         d1=d1, s1='simple',
                         alpha_s1=1, alpha_d1=100,
                         alpha_flux=100, alpha_cm=50,
                         maxit=100, ttype=TTYPE, show_updates=False)

    out = out.blur_circ(5*eh.RADPERUAS)   

    #------------- second round of imaging -------------#
    out = eh.imager_func(obs, out, out, flux,
                         d1=d1, s1='tv',
                         alpha_s1=1, alpha_d1=50,
                         alpha_flux=100, alpha_cm=50,
                         maxit=100, ttype=TTYPE, show_updates=False)

    out = out.blur_circ(5*eh.RADPERUAS)

    #------------- third round of imaging -------------#
    out = eh.imager_func(obs, out, out, flux,
                         d1=d1, s1='tv',
                         alpha_s1=1, alpha_d1=10,
                         alpha_flux=100, alpha_cm=50,
                         maxit=100, ttype=TTYPE, show_updates=False)

    ## elapsed time for imaging (debugging) ##
    print("Total time elapsed: ", time.time() - tt)

    ## blur final image ##
    outblur = out.blur_circ(15*eh.RADPERUAS)

    ## save image if requested ##
    if save_name is not None:
        outblur.save_fits(save_name)

    return out, outblur

def produceOutput(image, _obs_fpath, output_dir_root="../results/",
                  firstname='joseph', lastname='farah', method='rml'):

    """
        Format output per ngEHT challenge conventions.
    
        Args:
            image (ehtim.image.Image): final image, to be saved
            _obs_fpath (str): path to obs file (used to extract params)
            output_dir_root (str): path to root directory for output
            firstname (str): your firstname
            lastname (str): your lastname
            method (str): imaging method; if you're using this script, its "rml"

        Returns:
            none (none): none
    
    """

    bcolors.warning("Beginning export.")

    ## compile information from observation filename and kwargs ##
    folder_name = "challenge1_{}{}/".format(firstname, lastname)
    source = _obs_fpath.split('/')[-1].split('_')[0]
    array = _obs_fpath.split('/')[-1].split('_')[1]
    freq = _obs_fpath.split('/')[-1].split('_')[2]
    if 'ref' in _obs_fpath:
        array += '_' + _obs_fpath.split('/')[-1].split('_')[2]
        freq = _obs_fpath.split('/')[-1].split('_')[3]
    method = method

    ## construct output filenames ##
    im_fname = "challenge1_{}_{}_{}_{}_{}{}.fits".format(
        source, array, freq, method, firstname, lastname)
    pdf_fname = "PDF_challenge1_{}_{}_{}_{}_{}{}.pdf".format(
        source, array, freq, method, firstname, lastname)

    ## make folder for storing output images ##
    ## NOTE: command will fail if folder already exists, but
    ## script will continue ##
    os.system("mkdir " + output_dir_root + folder_name)

    ## save image ##
    image.save_fits(output_dir_root + folder_name + im_fname)

    ## export pdf to same location as image ##
    image.display(export_pdf=output_dir_root + folder_name + pdf_fname)

    bcolors.success("Finished exporting.")


def main():
    """
        main function execution

        Args:
            none (none): none

        Returns:
            none (none): none

    """

    #------------- load in observation from filepath -------------#

    ## sys.argv[1] refers to a command line argument ##
    _obs_fpath = str(sys.argv[1])
    obs = eh.obsdata.load_uvfits(_obs_fpath).avg_coherent(T_AVG_COHERENT)

    bcolors.success("Imaging " + _obs_fpath)

    #------------- construct image prior -------------#

    ## preset imaging constraints ##
    npix        = 128               ## number of pixels in prior
    zbl         = 1.0               ## zero baseline flux of prior, in Jansky
    fov         = 128*eh.RADPERUAS  ## Field Of View of the prior
    prior_fwhm  = 200*eh.RADPERUAS  ## size of the prior

    ## construct priors ##
    emptyprior  = eh.image.make_square(obs, npix, fov)
    flatprior   = emptyprior.add_flat(zbl)
    gaussprior  = emptyprior.add_gauss(zbl, (prior_fwhm, prior_fwhm, 0, 0, 0))
    discprior   = emptyprior.add_tophat(1.0, 25*eh.RADPERUAS)

    priors = {
        'empty': emptyprior,
        'flat': flatprior,
        'gauss': gaussprior,
        'disc': discprior,
    }

    ## select prior ##
    prior = priors[PRIOR.lower()]

    #------------- peform imaging -------------#
    out, outblur = imageObs(obs, prior, d1=DATA_TERM)

    #------------- format and save output -------------#
    produceOutput(outblur, _obs_fpath)


if __name__ == '__main__':
    main()
