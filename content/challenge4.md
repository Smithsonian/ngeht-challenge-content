title: Analysis Challenge #4
slug: challenge4


This challenge is currently under construction, full details will be posted below.


Welcome to the fourth ngEHT analysis challenge. The first analysis
challenge successfully tested our framework for generating synthetic
ngEHT data based on hypothetical array configurations and collecting
submitted reconstructions. In our second challenge, we moved to a more
scientific challenge using dynamical models of SgrA\* and M87, while
testing the capabilities of ngEHT at making movies of black holes on
our primary science targets. The third challenge is nearly identical to the second challenge, but with all Stokes parameters included in the synthetic data rather than Stokes I only, and is meant to assess the (dynamical) polarization reconstruction capabilities of the ngEHT reference array and current analysis algorithms under realistic observing conditions.

The fourth challenge differs from the first three in that the primary focus is not on image reconstruction, but on black hole parameter estimation. We will generate ngEHT Phase 1 and ngEHT Phase 2 data with different calibration properties from three different M87-inspired models: a geometric m-ring model, a time-averaged GRMHD image, and a GRMHD snapshot. We invite participants to submit measurements with 1-sigma errors of a set of parameters defined below. If you want to use an imaging algorithm but don't have access to a parameter estimation algorithm, you may also upload image reconstructions, from which we will extract the relevant (geometric) parameters. 

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
`analysis-challenge-4` channel on the ngEHT Slack.  If you need an
invite to the Slack or to the channel, please contact Greg at glindahl
ZAT cfa.harvard.edu.  We're also happy to help people with software
installation advice.

## Schedule

- TBD: Data release

Please note that unless otherwise specified, all source models and
data products should be kept proprietary among those currently invited
to participate in the challenge, which includes all EHT Collaboration
members, and any members of ngEHT science and technical working
groups.

Downloads are password protected: the username is `challenge1` (yes,
it's still `challenge1` for the fourth challenge!) and the secret
password is available if you ask on Slack, on the
`analysis-challenge-4` channel on the ngEHT Slack.


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

### Parameter measurements

### Images

Please submit your images as FITS or hdf5 files bundled in a zip
file as specified below. The images can be reconstructed with any
field of view or pixel resolution, as long as this is clear from the
FITS header. If you can, submit an image for each source
model, frequency, and array. You may submit multiple images reconstructed using different methods;
please follow the filename conventions as specified below. We will be
using eht-imaging to load and evaluate the images, so it may be worth
checking if your image loads properly in eht-imaging.


### Evaluation

It would be helpful but not required to add a txt file summarizing
your experience with this challenge.

### Filename conventions



## <a name="SourceModels">Source models</a>

### m-ring geometric model

### GRMHD time-average

### GRMHD snapshot

## Array and data synthesis

### Station locations

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

