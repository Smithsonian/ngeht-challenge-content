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
