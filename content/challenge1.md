title: Analysis Challenge #1
slug: challenge1

Welcome to the first ngEHT analysis challenge. The primary objective
of this first challenge is to set up a framework for the generation of
synthetic ngEHT data based on theoretical source models, and to
conduct the organized submission and cross-comparison of
reconstruction results from multiple teams. This challenge includes
two static total-intensity source models (SgrA* and M87), and a
simulated observation using a hypothetical ngEHT array including the
current EHT and 10 additional stations. Participants are requested to
submit image reconstructions by June 30th to the ngEHT challenge
website -- see below for details. Please note that unless otherwise
specified, all source models and data products should be kept
proprietary among those currently invited to participate in the
challenge, which includes all EHT Collaboration members.

## Table of Contents

- [Downloads](./#Downloads)
- [Example Scripts](./#ExampleScripts)
- [Submissions](./#Submissions)

## Schedule

- June 11, 2021: Synthetic data available
- June 30, 2021: Submission deadline

## Related links

[ngEHT Winter meeting challenge files (previous work)](https://drive.google.com/drive/folders/10TrAZbQUzyYQzrK7Ruzt-XCR0T31bySe?usp=sharing)

ngEHT Simulation group presentations:
[12/8/2020](https://docs.google.com/presentation/d/1nv3mRWQrk-90J-OzqOQon7R5ZbMEi5OXnxy2p9cjWrk/edit#slide=id.gb228cefa57_7_0),
[4/23/2021](https://docs.google.com/presentation/d/1fhsno3peFbO5tAXeuIVvdPpNSA_IyVYyCHqVn43Z7Hc/edit#slide=id.gd03baebd48_1_15),
[6/4/2021](https://docs.google.com/presentation/d/1dsfEtEMKXrhUgC62tT5O1xG1iqWwrZc40X3-WRslykc/edit?pli=1#slide=id.p)

## Source models

### SGRA

![Sgr A* model](../static/sgra_model_challenge1.png)

Description: Semi-analytic stationary RIAF model for SgrA in the literature (see, e.g. Broderick & Loeb 2006). This model can be used to test the capabilities of next generation arrays in precision modeling of BH parameters. High resolution is needed to capture the unique signature from subring structure. This model does not capture any variability due to turbulence in the system.

Details: The basic model is a=0 (Schwarzschild) at an inclination of i=130 deg and all models include non-thermal particles. The model includes disk height (following Pu et al. 2018), sub-Keplerian flow properties (kappa=0.5, alpha=0.5) following the notation of Tiede et al. 2020 -- e.g. Eq. 10 and 11) and fitted to the observed data of Bower et al. 2015, 2019, Liu et al. 2016 and Zhao et al. 2003.

Citation: These images are generated for the ngEHT winter science meeting end-to-end simulation studies by Christian Fromm (cfromm@th.physik.uni-frankfurt.de). Please contact C.F. for use outside ngEHT challenge activities.

Parameters:

- GRRT at 230/345/690 GHz at 4096x4096 pixels
- FOV 128M, d=8.178kpc and m=4.14M\_sun (GRAVITY et al. 2019)

### M87

Yet to be written

## Array and Data Synthesis

### Station locations

Two arrays were used to generate the synthetic data. They are labeled
eht\_2022 and ngeht\_ref1. eht\_2022 consists of the 11 stations expected
to participate in the 2022 EHT observations. In ngeht\_ref1, 10
stations are added to this array. The station locations were chosen
based on a uv-coverage analysis led by Alex Raymond, investigating
which combination of sites from Raymond et al. (2021) provided optimal
uv-coverage, folding in weather dropouts. The LMT, SPT, and KP were
not included in the 345 GHz observations with eht\_2022. The station
locations are shown in the image below.

![ngEHT ref1](../static/ngeht_ref1.png)

### Data properties

A 24-hour observing track was simulated for each array, source, and
frequency. Each track consists of 10-minute scans interleaved with
10-minute gaps. A single frequency channel with a time resolution of
10 seconds is provided.

Thermal noise expected from the receiver and enhanced by atmospheric
opacity were added to the complex visibilities. The following
assumptions were made for all sites:

- Receiver temperature:
- - 60 K for 230 GHz
- - 100 K for 345 GHz
- Aperture efficiency:
- - 0.68 for 230 GHz
- - 0.42 for 345 GHz
- Bandwidth: 8 GHz
- Quantization efficiency: 0.88
- Dish diameter: 6 m for new sites, actual diameter for existing sites
- Opacity: median values in April as extracted from the MERRA-2 data by Raymond et al. (2021), at 30 degrees elevation.

Visibility phases were scrambled, but stabilized across scans. No further systematic errors were added, this will be done in future challenges.

After data generation, data points with a signal-to-noise ratio less than 1 were flagged.

### Summary table

The table below summarizes the station locations and SEFDs resulting
from the assumptions outlined above. For a more detailed breakdown,
see [arrays/station_info.csv](../static/ngEHT_Analysis_Challenges/Challenge_1/arrays/station_info.csv)

[jtable]
Station, Code, X (m), Y (m), Z (m), SEFD\_230 (Jy), SEFD\_345 (Jy)
IRAM-30m, PV, 5088968, -301682, 3825016, 809, 4456
SMT, AZ, -1828796, -5054407, 3427865, 4973, 27410
SMA, SM, -5464523, -2493147, 2150612, 1500, 5882
LMT, LM, -768714, -5988542, 2063276, 357, 2710
ALMA, AA, 2225061, -5440057, -2481681, 63, 231
SPT, SP, 0, 0, -6359610, 3669, 11552, 
APEX, AP, 2225040, -5441198, -2479303, 2609, 9261
JCMT, JC, -5464585, -2493001, 2150654, 2105, 8259
GLT, GL, 541647, -1388536, 6180829, 2417, 23326
NOEMA, PB, 4523998, 468045, 4460310, 307, 3022
KP, KP, -1994314, -5037909, 3357619, 3535, 34109
BAJA, BA, -2352576, -4940331, 3271508, 11125, 53309
BAR, BR, -2363000, -4445000, 3907000, 10905, 51219
CNI, CI, 5311000, -1725000, 3075000, 11813, 74896
CAT, CT, 1569000, -4559000, -4163000, 15321, 166684
GAM, GB, 5627890, 1637767, -2512493, 6099, 285727
GARS, GR, 1538000, -2462000, -5659000, 28480, 949659
HAY, HA, 1521000, -4417000, 4327000, 1090, 144350
NZ, NZ, -4540000, 719000, -4409000, 16932, 225001
OVRO, OV, -2409598, -4478348, 3838607, 23788, 894355
SGO, SG, 1832000, -5034000, -3455000, 10905, 50204
[/jtable]

## <a name="Downloads">Downloads</a>

## <a name="ExampleScripts">Example Scripts</a>

## <a name="Submissions">Submissions</a>

### Images

Please submit your images as FITS files bundled in a zip file. The
images can be reconstructed with any field of view or pixel
resolution, as long as this is clear from the FITS header. We will be
using eht-imaging to load and evaluate the images, so it may be worth
checking if your image loads properly in eht-imaging.

### Non-imaging results

If you have performed analysis other than imaging (e.g., fit a
geometric model, measured the black hole mass or spin, or constrained
plasma parameters), please provide a text file summarizing your method
and results. These results will not be formally compared or analyzed,
but could certainly provide us with valuable insights.

### Evaluation

It would be helpful but not required to add a txt file summarizing your experience with this challenge. Think of questions like

- What imaging parameters did you find work best on these datasets?
- How difficult was it to image ngeht\_ref1 versus eht\_2022, or 345 GHz versus 230 GHz?
- Did the reconstruction quality and improvement of different arrays and frequencies meet your expectations?
- Based on your experience with these datasets, do you think there should be more development of the reconstruction method you used?
- What source models, data properties, or specific charges would you like to see in future challenges?
- Do you have any feedback on the infrastructure and organization of the challenges?

### Filename conventions

For the zip files, use the format challenge1\_[firstnamelastname].zip. 

Example: challenge1\_freekroelofs.zip

For the FITS files, use the format challenge1\_[source]\_[array]\_[frequency]\_[method]\_[firstnamelastname].fits

- source: SGRA or M87
- array: eht2022 or ngeht\_ref1
- frequency: 230 or 345
- method: rml, clean, themage, or other

Example: challenge1\_SGRA\_eht2022\_230\_rml\_freekroelofs.fits

For non-imaging results, use the format challenge1\_[source]\_[array]\_[frequency]\_nonimaging\_[firstnamelastname].txt

Example: challenge1\_SGRA\_eht2022\_230\_nonimaging\_freekroelofs.txt

For the evaluation, use the format challenge1\_evaluation\_[firstnamelastname].txt. 

Example: challenge1\_evaluation\_freekroelofs.txt

## Submit your results

<form action="/upload" method="post" accept-charset="utf-8"
      enctype="multipart/form-data">

    <input type="hidden" name="challenge" value="challenge1"/>
    <input type="text" name="name" placeholder="Your Name"/><br/>
    <input type="email" name="email" placeholder="Your Email"/><br/>
    <label for="zip">zip file: </label>
    <input id="zip" name="zip" type="file" value=""/><br/>

    <input type="submit" value="submit"/>
</form>

Our server has a 1 gigabit Internet connection, so uploads shouldn't
take too long.  The challenge organizers get notified by Slack for
every failed or successful upload. If you see any problems, we're likely
to reach out to contact you quickly.

## Communicating with the organizers

The primary way to talk to the challenge organizers is the private
`analysis-challenge-1` channel on the ngEHT-2021 Slack.  If you need an
invite to the Slack or to the channel, please contact Greg at glindahl
ZAT cfa.harvard.edu.  We're also happy to help people with software
installation advice.

