title: Analysis Challenge #4
slug: challenge4

Welcome to the fourth ngEHT Analysis Challenge! The fourth Challenge
differs from the first three in that the primary focus is not on image
reconstruction, but on black hole parameter estimation. We have
generated synthetic ngEHT datasets from three different M87-inspired
models: a geometric m-ring model, a time-averaged GRMHD image, and a
GRMHD snapshot image. We invite participants to submit measurements
(preferably with 1-sigma errors) of a set of parameters defined below.
If you want to use an imaging algorithm but don't have access to a
parameter estimation algorithm, you may also upload image
reconstructions, from which we will extract relevant (geometric)
parameters.

Please note that unless otherwise specified, all source models and
data products should be kept proprietary among those currently invited
to participate in the challenge, which includes all EHT Collaboration
members, and any members of ngEHT science and technical working
groups.

In parallel to Challenge 4, we are also running the ngEHT Forecasting
Tournament. Participation in this tournament is highly encouraged for
everyone! (The tournament will be launched soon, and a link will be
posted here.)

## Table of Contents

- [Downloads](./#Downloads)
- [Submissions](./#Submissions)
- [Source models](./#SourceModels)

## Communicating with the organizers

The primary way to talk to the challenge organizers is the private
`analysis-challenge-4` channel on the ngEHT Slack.  If you need an
invite to the Slack or to the channel, please contact Greg at lindahl
ZAT pbm.com.  We're also happy to help people with software
installation advice.

## Schedule

- September 29, 2023: Data release
- November 10, 2023: Submission deadline

## <a name="Downloads">Downloads</a>

Please note that unless otherwise specified, all source models and
data products should be kept proprietary among those currently invited
to participate in the challenge, which includes all EHT Collaboration
members, and any members of ngEHT science and technical working
groups.

Downloads are password protected: the username is `challenge1` (yes,
it's still `challenge1` for the fourth challenge!) and the secret
password is available if you ask the organizers, or on the
`analysis-challenge-4` channel on the ngEHT Slack.

[Challenge 4 Downloads](../c4downloads/)

## Submit your results

If you have any problems with this upload, please contact Greg Lindahl on slack or email at lindahl ZAT pbm.com

<form action="/upload" method="post" accept-charset="utf-8"
      enctype="multipart/form-data">

    <input type="hidden" name="challenge" value="challenge4"/>
    <input type="text" name="name" placeholder="Your Name"/><br/>
    <input type="email" name="email" placeholder="Your Email"/><br/>
    <label for="zip">zip file: </label>
    <input id="zip" name="zip" type="file" value=""/><br/>

    <input type="submit" value="submit"/>
</form>


## <a name="Submissions">Submissions</a>

### Parameter measurements

We are especially interested in your measurements (including 1-sigma errors, see below for format instructions) of the following parameters. This list is non-exhaustive, and we'd like to hear about anything else you learn from your analysis! You do not need to submit a measurement for each parameter or each dataset.


Geometric ring (n=0 and/or n=1) parameters (for all datasets):

- n=1 detection yes/no

- Mean diameter (geometric mean of major and minor axis)

- Ellipticity (axis ratio)

- Ellipticity position angle (major axis, counter-clockwise on the sky)

- Ring width

- Fractional flux of the n=1 ring

- Total linear and/or circular polarization fraction

- Complex (total intensity, linear and/or circular polarization) beta-modes (up to m=2)


Physical parameters (for GRMHD datasets):

- Black hole mass

- Black hole spin

- MAD or SANE accretion flow

- Rhigh


With your parameter measurements, please submit a short explanation on how you got them (what analysis method did you use, with what kind of parameters, etc.).
If you have additional information in the form of plots, a slide deck, etc., that is very welcome as well.


### Images

If you'd like to submit images, please submit them as FITS or hdf5 files bundled in a zip
file as specified below. The images can be reconstructed with any
field of view or pixel resolution, as long as this is clear from the metadata. If you can, submit an image for each source
model, frequency, and array. You may submit multiple images reconstructed using different methods;
please follow the filename conventions as specified below. We will be
using eht-imaging to load and evaluate the images, so it may be worth
checking if your image loads properly in eht-imaging.


### Evaluation

It would be helpful but not required to add a txt file summarizing
your experience with this challenge, and any feedback on how we can improve things for a next challenge.

### Format and file name conventions
Please submit your main parameter measurements in a txt file.

In your txt file, make 4 columns with parameter name, measured value, 1sigma error (or N/A), and unit (or N/A).

For example:

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:1px 1px;word-break:normal;}
.tg th{font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:1px 1px;word-break:normal;}
.tg .tg-73oq{border-color:#000000;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-73oq">n=1_detection</th>
    <th class="tg-73oq">yes</th>
    <th class="tg-73oq">N/A</th>
    <th class="tg-73oq">N/A</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-73oq">meandiameter_n=0</td>
    <td class="tg-73oq">42.2</td>
    <td class="tg-73oq">1.5</td>
    <td class="tg-73oq">uas</td>
  </tr>
  <tr>
    <td class="tg-73oq">axis_ratio_n=1</td>
    <td class="tg-73oq">0.95</td>
    <td class="tg-73oq">0.02</td>
    <td class="tg-73oq">N/A</td>
  </tr>
  <tr>
    <td class="tg-73oq">majoraxis_pa_n=1</td>
    <td class="tg-73oq">1.25</td>
    <td class="tg-73oq">0.2</td>
    <td class="tg-73oq">rad</td>
  </tr>
  <tr>
    <td class="tg-73oq">width_n=1</td>
    <td class="tg-73oq">1.2</td>
    <td class="tg-73oq">0.1</td>
    <td class="tg-73oq">uas</td>
  </tr>
  <tr>
    <td class="tg-73oq">fractionalflux_n=1</td>
    <td class="tg-73oq">0.05</td>
    <td class="tg-73oq">0.003</td>
    <td class="tg-73oq">N/A</td>
  </tr>
  <tr>
    <td class="tg-73oq">total_circpol_fraction_n=0</td>
    <td class="tg-73oq">0.02</td>
    <td class="tg-73oq">0.01</td>
    <td class="tg-73oq">N/A</td>
  </tr>
  <tr>
    <td class="tg-73oq">beta1_stokesi_amp_n=0</td>
    <td class="tg-73oq">0.1</td>
    <td class="tg-73oq">0.2</td>
    <td class="tg-73oq">N/A</td>
  </tr>
  <tr>
    <td class="tg-73oq">beta2_linpol_phase_n=0</td>
    <td class="tg-73oq">1.25</td>
    <td class="tg-73oq">0.2</td>
    <td class="tg-73oq">rad</td>
  </tr>
  <tr>
    <td class="tg-73oq">beta2_linpol_phase_n=1</td>
    <td class="tg-73oq">0.25</td>
    <td class="tg-73oq">0.2</td>
    <td class="tg-73oq">rad</td>
  </tr>
  <tr>
    <td class="tg-73oq">mass</td>
    <td class="tg-73oq">6.5e9</td>
    <td class="tg-73oq">0.5e9</td>
    <td class="tg-73oq">Msun</td>
  </tr>
  <tr>
    <td class="tg-73oq">spin</td>
    <td class="tg-73oq">-0.7</td>
    <td class="tg-73oq">0.2</td>
    <td class="tg-73oq">N/A</td>
  </tr>
  <tr>
    <td class="tg-73oq">magnetization</td>
    <td class="tg-73oq">MAD</td>
    <td class="tg-73oq">N/A</td>
    <td class="tg-73oq">N/A</td>
  </tr>
  <tr>
    <td class="tg-73oq">rhigh</td>
    <td class="tg-73oq">60</td>
    <td class="tg-73oq">40</td>
    <td class="tg-73oq">N/A</td>
  </tr>
</tbody>
</table>


With the file name following the format below:

ch4\_[model]\_[array]\_[frequency]GHz\_[syntheticdatapipeline]\_[analysismethodname]\_[firstnamelastname]\_measurements.txt

- model: mring, grmhd\_average, or grmhd\_singleframe

- array: phase1 or phase2

- syntheticdatapipeline: ngehtsim or symba

You can provide additional explanations in a seperate (text) file.

Please upload any images (.fits or .hdf5) using the same file name format as above.


## <a name="SourceModels">Source models</a>

### Double m-ring model
We use a double m-ring model, which is the sum of a thicker and a thinner m-ring, representing n=0 and n=1 emission, respectively (similar to Tiede et al. 2022).
The single m-ring definition is given in the paper snippet below, taken from EHT Collaboration et al., 2022d (Sgr A* Paper IV):

<p><img src="../static/challenge4/mring_definition_sgrapaperiv.png" alt="mring" width="50%"/></p>

The definition in linear and circular polarization is equivalent, except that in linear polarization there is no conjugation symmetry in the betas (the linear polarization image is complex), and in circular polarization the image is not confined to be positive. Note that we do *not* add a Gaussian floor component like in Sgr A* Paper IV.

In addition, we add an ellipticity to the m-rings by squishing it on one axis (or, equivalently, stretching it on the orthogonal axis from a smaller diameter). This operation consists of a scaling (axis ratio) and a position angle.

Our double m-ring model is frequency-independent apart from an overall total flux scaling.

We have used the implementation in eht-imaging to generate the m-ring model. An example double m-ring generation script has been added to the Challenge 4 release.

### GRMHD time-average
This is a time-averaged image generated from the frames from a GRMHD movie at 86, 230, and 345 GHz, parameterized by a black hole mass, spin, magnetization (MAD/SANE), and electron temperature distribution parameter (Rhigh, from the prescription by Moscibrodzka et al. 2016).

### GRMHD snapshot
This is a single snapshot (frame) from a GRMHD movie at 86, 230, and 345 GHz. The GRMHD snapshot may or may not come from the same model as the time average above.

## Array and data synthesis
The synthetic datasets were generated with either  <a href="https://github.com/Smithsonian/ngehtsim">ngehtsim</a>  or <a href="https://bitbucket.org/M_Janssen/symba/src/master/SYMBA">SYMBA</a>, using the latest versions of the ngEHT Phase 1 and Phase 2 arrays, at 86, 230, at 345 GHz. The figure below shows the Phase 2 array, where we have included all sites (including the yellow sites, which are not ngEHT sites but may observe with the ngEHT) in the synthetic datasets. The SPM site is called BAJA and the LCO site is LAS in the synthetic datasets. The Phase 1 array is identical to the Phase 2 array, but does not contain the stations BOL, KILI, SGO, and SPX. Not all stations observe at all frequencies (simultaneously). Thermal noise with contributions from the receiver and atmosphere was added to the data, and the effect of frequency phase transfer (FPT) was included in setting detection limits. No amplitude gain errors and no polarimetric leakage effects were added to the ngehtsim datasets. See the data generation script released with the datasets for more specific details.

In addition to the ngehtsim datasets, we included datasets generated with SYMBA (Roelofs et al. 2020), using the same array and weather parameters. The effect of frequency phase transfer is not included here, and the datasets contain additional systematics from antenna pointing offsets and imperfect fringe fitting and a-priori amplitude calibration. No polarimetric leakage effects were added. See the SYMBA input files released with the datasets for specific settings.

<p><img src="../static/challenge4/phase2_array.png" alt="array" width="90%"/></p>

Image: ngEHT Phase 2 reference array, taken from Doeleman et al. (2023).

<p><img src="../static/challenge4/uv-coverage_grmhd_singleframe_phase1_ngehtsim.png" alt="array" width="45%"/> <img src="../static/challenge4/uv-coverage_grmhd_singleframe_phase2_ngehtsim.png" alt="array" width="45%"/></p>

Image: Example uv-coverage of the ngEHT Phase 1 and Phase 2 arrays from our synthetic datasets.



