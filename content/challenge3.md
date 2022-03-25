title: Analysis Challenge #3
slug: challenge3

Welcome to the third ngEHT analysis challenge. The first analysis
challenge successfully tested our framework for generating synthetic
ngEHT data based on hypothetical array configurations and collecting
submitted reconstructions. In our second challenge, we moved to a more
scientific challenge using dynamical models of SgrA\* and M87, while
testing the capabilities of ngEHT at making movies of black holes on
our primary science targets. This third challenge is nearly identical to the second challenge, but with all Stokes parameters included in the synthetic data rather than Stokes I only. The challenge is meant to assess the (dynamical) polarization reconstruction capabilities of the ngEHT reference array and current analysis algorithms under realistic observing conditions

We invite participants to submit image reconstructions from a set of synthetic datasets. Additionally, results from any non-imaging
analysis are also welcome, as well as an evaluation on the
challenge. This challenge includes two dynamical full Stokes
source models for SgrA\*: one based on GRMHD simulations and one using
a sheared hot-spot model on top of a stationary RIAF semi-analytic
source. It also includes a dynamical GRMHD model of M87 with simulated
observations taken over several months. Simulated observations are
taken at two distinct frequencies (230 and 345 GHz) using a
hypothetical ngEHT array including the current EHT and 10 additional
stations (ngeht and eht\_2022). Participants are requested to
submit results as images or image sequences (for a dynamical model) to
the ngEHT challenge website.

Please note that unless otherwise specified, all source models and
data products should be kept proprietary among those currently invited
to participate in the challenge, which includes all EHT Collaboration
members, and any members of ngEHT science and technical working
groups.

## Table of Contents

- [Downloads](./#Downloads)
- [Submissions](./#Submissions)
- [Source models](./#SourceModels)

## Communicating with the organizers

The primary way to talk to the challenge organizers is the private
`analysis-challenge-3` channel on the ngEHT Slack.  If you need an
invite to the Slack or to the channel, please contact Greg at glindahl
ZAT cfa.harvard.edu.  We're also happy to help people with software
installation advice.

## Schedule

- Mar 16, 2022: Data release
- May 1, 2022: Nominal submission deadline for inclusion in first challenge writeup

## <a name="Downloads">Downloads</a>

Please note that unless otherwise specified, all source models and
data products should be kept proprietary among those currently invited
to participate in the challenge, which includes all EHT Collaboration
members, and any members of ngEHT science and technical working
groups.

Downloads are password protected: the username is `challenge1` (yes,
it's still `challenge1` for the third challenge!) and the secret
password is available if you ask on Slack, on the
`analysis-challenge-3` channel on the ngEHT Slack.

[Challenge 2 Downloads](../c2downloads/)

## Submit your results

If you have any problems with this upload, please contact Greg Lindahl on slack or email at glindahl ZAT cfa.harvard.edu

<form action="/upload" method="post" accept-charset="utf-8"
      enctype="multipart/form-data">

    <input type="hidden" name="challenge" value="challenge3"/>
    <input type="text" name="name" placeholder="Your Name"/><br/>
    <input type="email" name="email" placeholder="Your Email"/><br/>
    <label for="zip">zip file: </label>
    <input id="zip" name="zip" type="file" value=""/><br/>

    <input type="submit" value="submit"/>
</form>

## <a name="Submissions">Submissions</a>

### Images

Please submit your (dynamical) images as FITS or hdf5 files bundled in a zip
file as specified below. The images can be reconstructed with any
field of view or pixel resolution, as long as this is clear from the
FITS header. If you can, submit an image or movie for each source
model, frequency, and array. For the M87 datasets and the ngeht
Sgr A\* datasets, you may also analyze the 86, 230 and 345 GHz data
jointly. For Sgr A\*, please submit your best estimate of the
intrinsic source structure (i.e. after any scattering mitigation). You
may submit multiple images reconstructed using different methods;
please follow the filename conventions as specified below. We will be
using eht-imaging to load and evaluate the images, so it may be worth
checking if your image loads properly in eht-imaging.

### Non-imaging results

If you have performed analysis other than imaging (e.g., fit a
geometric model, measured the black hole mass or spin, or constrained
plasma parameters), please provide a text file summarizing your method
and results. These results will not be formally compared or analyzed,
but could certainly provide us with valuable insights.

### Evaluation

It would be helpful but not required to add a txt file summarizing
your experience with this challenge. Think of questions like:

- What imaging parameters did you find work best on these datasets?
- How difficult was it to image ngeht versus eht_2022, or 345 GHz versus 230 GHz?
- Did the reconstruction quality and improvement of different arrays and frequencies meet your expectations?
- Based on your experience with these datasets, do you think there should be more development of the reconstruction method you used?
- What source models, data properties, or specific charges would you like to see in future challenges?
- Do you have any feedback on the infrastructure and organization of the challenges?

### Filename conventions

For the zip files, use the format challenge3\_[firstnamelastname].zip. 

Example: challenge3_freekroelofs.zip

For each combination, make a folder challenge3\_[source]\_[subtype]\_[array]\_[frequency]\_[method]\_[firstnamelastname]

- source: SGRA or M87
- subtype: GRMHD or RIAFSPOT
- array: eht2022 or ngeht
- frequency: 86, 230, 345, or e.g. 230+345
- method: e.g. ehtim, smili, clean, themage

Example: challenge3\_SGRA\_GRMHD\_eht2022\_230\_ehtim\_freekroelofs

Within the folder, put the FITS of hdf5 images sorted by frame number,
e.g. 0000.fits, 0001.fits, etc. You can also put an hdf5 movie file that can be properly loaded by eht-imaging. The different Stokes components can be included in the same fits or hdf5 image (again such that they can be loaded by eht-imaging). Alternatively, you may include the Stokes components as separate images, in the format I-0000.fits, Q-0000.fits, U-0000.fits, V-0000.fits, I-0001.fits, etc.

Also, please provide the movie start time in hours UT and frame duration in
hours in a file timestamps.txt, which for a movie starting at midnight UT with a frame duration of 10 minutes should look like:

0.00 0.16666666666667

For non-imaging results, use the format challenge3\_[source]\_[subtype]\_[array]\_[frequency]\_nonimaging\_[firstnamelastname].txt

Example: challenge3\_SGRA\_GRMHD\_eht2022\_230\_nonimaging\_freekroelofs.txt

For the evaluation, use the format challenge3\_evaluation\_[firstnamelastname].txt. 

Example: challenge3\_evaluation\_freekroelofs.txt

## <a name="SourceModels">Source models</a>

### SGRA_RIAFSPOT

This Sgr A\* model is a RIAF (Broderick et al. 2016) plus shearing
hotspot (Tiede et al. 2020) semi-analytical model prepared by Paul
Tiede. The hotspot parameters are inspired by Gravity (2018) and the
black hole spin was set to 0.1. The pixel resolution is 313x313 px,
with a field of view of 315 uas. The frames are spaced ~30 seconds
apart and form a 4-hour movie of a hotspot shearing and falling in,
which is repeated a few times over the course of the observation. The raw and scattered movies are shown below.

<p><img src="../static/challenge3/merged_SGRA_RIAFSPOT_noscat.gif" alt="SGRA" width="98%"/></p>

<p><img src="../static/challenge3/merged_SGRA_RIAFSPOT_scat.gif" alt="SGRA" width="98%"/></p>

### SGRA_GRMHD

This Sgr A\* GRMHD model was prepared by Koushik Chatterjee. The GRMHD model is a MAD model with spin 0.5. In order to include the polarization information, this model was ray-traced with ipole by Razieh Emami, whereas it was ray-traced in Stokes I only with BHOSS for Challenge 2. A thermal electron distribution was assumed. The 500 frames are spaced 10M (221 s) apart. The pixel resolution is 2048x2048 px, with a FOV of 400 uas. The raw and scattered movies are shown below.

<p><img src="../static/challenge3/merged_SGRA_GRMHD_noscat.gif" alt="SGRA_GRMHD" width="98%"/></p>

<p><img src="../static/challenge3/merged_SGRA_GRMHD_scat.gif" alt="SGRA_GRMHD" width="98%"/></p>

### M87_GRMHD

The M87 model is a GRMHD movie with 20 frames that are spaced 20M (~1
week) apart. The pixel resolution is 2048x2048 px, with a field of
view of 1 mas x 1mas. The images were ray-traced from a HAMR
simulation (MAD, spin 0.94; K. Chatterjee) using ipole by Razieh
Emami. Rhigh was set to 160 and accelerated electron heating was
included, setting kappa=3.5. We only use the Stokes I information from
the model. The movies are shown below.

<p><img src="../static/challenge3/merged_M87.gif" alt="M87" width="98%"/></p>

## Array and data synthesis

### Station locations

Two arrays were used to generate the synthetic data. They are labeled
eht\_2022 and ngeht. eht\_2022 consists of the 11 stations
expected to participate in the 2022 EHT observations. In ngeht,
10 stations are added to this array. The station locations were chosen
based on a uv-coverage analysis led by Alex Raymond, investigating
which combination of sites from Raymond et al. (2021) provided optimal
uv-coverage, folding in weather dropouts. The LMT, SPT, and KP were
not included in the 345 GHz observations with eht_2022. The station locations are shown in the image below.

![ngEHT ref1](../static/ngeht_ref1.png)

## Data properties

Several data corruption and calibration effects were included in the
synthetic data generation, for which SYMBA (Roelofs et al. 2020) was
used. See the SYMBA antenna files included in the release for detailed
antenna and weather parameters.

- Thermal noise with contributions from the receiver and atmosphere
- Atmospheric opacity, corrected with a priori amplitude calibration in rPICARD (Janssen et al. 2019), with remaining systematic errors due to a varying opacity across the band and within a scan. The opacities are based on the median pwv, ground pressure, and ground temperature on 1 April (2000-2020) for each site, taken from the MERRA-2 data (https://disc.gsfc.nasa.gov/datasets/M2I3NPASM_5.12.4/summary).
- Atmospheric turbulence, corrected by a fringe fit with rPICARD. The coherence time was set between 3 and 15 seconds, scaling linearly with the pwv at each site.
- Antenna pointing offsets: 2” rms for each station, stable over a scan
- For Sgr A\* models: each frame was scattered with a refractive scattering screen. The screen is static and self-consistent between frequencies.
- Network calibration was applied, using the (varying) source model flux to calibrate ALMA-APEX and JCMT-SMA
- All Stokes parameters were simulated. No polarization leakage was added to the data. 

