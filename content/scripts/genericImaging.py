"""
====================================
Filename:         imageSmallObs.py 
Author:              Joseph Farah 
Description:       Produce image from small observation quickly.
====================================
Notes
     
"""

#------------- imports -------------#
import sys
import time 
import copy
import datetime
import numpy as np
import ehtim as eh

import matplotlib.pyplot as plt


## SCRIPT PARAMETERS ##
T_AVG_COHERENT = 100
PRIOR = "DISC"
DATA_TERM = 'cphase'

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
        print (bcolors.WARNING + "[" + message + "]" + bcolors.ENDC)

    @staticmethod
    def success(message):
        print (bcolors.OKGREEN + "[" + message + "]" + bcolors.ENDC)

    @staticmethod
    def failure(message):
        print (bcolors.FAIL + "[" + message + "]" + bcolors.ENDC)




ttype = 'direct'

def imageSmallObs(obs, prior, save_name="output.fits", d1='bs'):

    zbl = 2.3 ##jy
    
    # Image total flux with bispectrum
    flux = zbl
    tt = time.time()
    out  = eh.imager_func(obs, prior, prior, flux,
                          d1=d1, s1='simple',
                          alpha_s1=1, alpha_d1=100,
                          alpha_flux=100, alpha_cm=50,
                          maxit=100, ttype=ttype, show_updates=False)

    out = out.blur_circ(5*eh.RADPERUAS)
    out = eh.imager_func(obs, out, out, flux,
                    d1=d1, s1='tv',
                    alpha_s1=1, alpha_d1=50,
                    alpha_flux=100, alpha_cm=50,
                    maxit=100,ttype=ttype, show_updates=False)

    out = out.blur_circ(5*eh.RADPERUAS)
    out = eh.imager_func(obs, out, out, flux,
                    d1=d1, s1='tv',
                    alpha_s1=1, alpha_d1=10,
                    alpha_flux=100, alpha_cm=50,
                    maxit=100,ttype=ttype, show_updates=False)

    print ("total time: ", time.time() - tt)

    outblur = out.blur_circ(15*eh.RADPERUAS)

    if save_name is not None: outblur.save_fits(save_name)

    return out, outblur



def getTimeIndexMovie(movie, time):
    closest_index = 0
    delta_t = 1e22
    frames = movie.im_list()
    for f, frames in enumerate(frames):
        dt = abs(frames.time - time)
        if dt < delta_t:
            delta_t = dt 
            closest_index = f 

    return closest_index

def getTimeIndex(split_obs, time):
    closest_index = 0
    delta_t = 1e22
    for s, s_obs in enumerate(split_obs):
        dt = abs(s_obs.tstart - time)
        if dt < delta_t:
            delta_t = dt 
            closest_index = s 

    return closest_index


def produceOutput(image, _obs_fpath, output_dir_root="../results/", firstname='joseph', lastname='farah', method='rml'):

    bcolors.warning("Beginning export.")

    ## imports in case the script doesn't have them ##
    import os 

    ## compile info ##
    folder_name = f"challenge1_{firstname}{lastname}/"
    source = _obs_fpath.split('/')[-1].split('_')[0]
    array = _obs_fpath.split('/')[-1].split('_')[1]
    freq = _obs_fpath.split('/')[-1].split('_')[2]
    method = method

    ## make image file name ##
    im_fname = f"challenge1_{source}_{array}_{freq}_{method}_{firstname}{lastname}.fits"
    pdf_fname = f"PDF_challenge1_{source}_{array}_{freq}_{method}_{firstname}{lastname}.pdf"

    ## make folder ##
    os.system(f"mkdir {output_dir_root+folder_name}")

    ## save image ##
    image.save_fits(output_dir_root+folder_name+im_fname)

    ## save pdf of image to same location ##
    image.display(export_pdf=output_dir_root+folder_name+pdf_fname)

    bcolors.success("Finished exporting.")


def main():
    """
        main function execution
    
        Args:
            none (none): none
    
        Returns:
            none (none): none
    
    """     

    ## load in obs ##
    _obs_fpath = str(sys.argv[1])
    bcolors.success("Imaging " + _obs_fpath)
    obs = eh.obsdata.load_uvfits(_obs_fpath).avg_coherent(T_AVG_COHERENT)

    ## Generate an image prior ##
    npix = 128
    zbl = 1.0 ##jy
    fov = 128*eh.RADPERUAS
    prior_fwhm = 200*eh.RADPERUAS # Gaussian size in microarcssec
    emptyprior = eh.image.make_square(obs, npix, fov)
    flatprior = emptyprior.add_flat(zbl)
    gaussprior = emptyprior.add_gauss(zbl, (prior_fwhm, prior_fwhm, 0, 0, 0))
    # _im_fpath = "./avery_sgra_eofn.txt"
    # im = eh.image.load_image(_im_fpath)
    # ringprior = im.blur_circ(20*eh.RADPERUAS)
    discprior = emptyprior.add_tophat(1.0, 25*eh.RADPERUAS)

    priors = {
        'empty':emptyprior,
        'flat':flatprior,
        'gauss':gaussprior,
        'disc':discprior,
        # 'ring':ringprior
    }

    ## select prior ##
    prior = priors[PRIOR.lower()]

    ## image ##
    out, outblur = imageSmallObs(obs, prior, d1=DATA_TERM)


    ## output ##
    produceOutput(outblur, _obs_fpath)



if __name__ == '__main__':
    main()
    