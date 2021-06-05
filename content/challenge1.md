title: Analysis Challenge #1
slug: challenge1

## Schedule

- June 11?, 2021: Synthetic data available
- June 30?, 2021: Submission deadline

## Communicating with the organizers

The primary way to talk to the challenge organizers is the private
analysis-challenge-1 channel on the ngEHT-2021 Slack.  If you need an
invite to the Slack or to the channel, please contact Greg at glindahl
ZAT cfa.harvard.edu.  We're also happy to help people with software
installation advice.

## Temporary Examples for the people writing content

Math can be rendered inline $e = mc^2$ or in its own (centered) block:

$$e = mc^2$$

You might need to have a shell script:

    :::bash
    echo "this is a shell script!"

or a python script:

    :::python
    print('this is a python script!')


## Download data

## Submit your results

Please zip up all of your results together

    :::bash
    zip -a team_frownie_theme.zip *.

And then fill out the following form to upload, picking the zip file you just made.

<form action="/upload" method="post" accept-charset="utf-8"
      enctype="multipart/form-data">

    <input type="hidden" name="challenge" value="challenge1"/>
    <input type="text" name="name" placeholder="Your Name"/><br/>
    <input type="email" name="email" placeholder="Your Email"/><br/>
    <input type="text" name="team" placeholder="Your Team"/><br/>
    <label for="zip">zip file: </label>
    <input id="zip" name="zip" type="file" value=""/><br/>

    <input type="submit" value="submit"/>
</form>

Our server has a 1 gigabit Internet connection, so uploads shouldn't
take too long.  The challenge organizers get notified by Slack for
every failed or successful upload, so we'll probably be in touch
