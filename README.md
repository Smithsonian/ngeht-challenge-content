# Editing the ngEHT Analysis Website

This git repo contains the content of the ngEHT Analysis Challenge website.

With luck, this README contains is everything you'll need to know to
edit the content of the website.

The live website can be found at https://challenge.ngeht.org/

The github repos are currently
- https://github.com/wumpus/ngeht-challenge-content/
- https://github.com/wumpus/ngeht-challenge-infra/

You will probably only need the first repo.

Following the overall theme of training people, we're going to update
the website using github "pull requests", which is the usualy way
people use github for collaborative software developments. We'll also
be using the "markdown" formatting langauge for documents, enhanced
with a plugin that lets us use TeX to typeset math.

## Website layout

The website is currently populated with a few pages. All of the page
content is in the content/ directory, formatted as "markdown".

- The homepage, which is index.md
- The 3 challenge webpages, which are challenge1.md, challenge2.md, etc
- additional webpages for installing the software, a FAQ, and a Credits page

## Formatting webpages

The basics for formatting a markdown webpage can be read about at
https://www.markdownguide.org/cheat-sheet/

If you need math, the render-math plugin is installed so that you can
use TeX syntax. This can either be inline enclosed by one $e=mc^2$ or
in a centered block enclosed by two $$e = mc^2$$

## Uploads

The challenge pages include a convoluted HTML form that talks to the
upload webserver. Hopefully you won't need to edit it. It's already included
in all of the challenge pages.

## Adding static files

If you want to add more .fits files to the website, for exmaple sample data or
image examples, place them in the directory content/static/

## Editing content and submitting a pull request

- go to the repo on github using a browser https://github.com/wumpus/ngeht-challenge-content/
- fork your own copy of the repo using the button on the upper right
- click on the green "Code" button to get an URL to download your copy of the repo
- (it will look like "git@github.com:your-github-name/ngeht-challenge-content.git")
- at the command line, type "git clone <url>"
- if you're using conda on your laptop, activate the conda environment
- cd into the new directory
- install the software needed to build the content with "pip install requirements.txt"
- edit content
- test the new content to make sure it looks good (see below)
- type "git status" to see what changes you are about to check in
- "git add" any new files, if there are any
- check in your changes with "git commit -m 'a good message describing your changes' -a
- type "git push"
- go back to github in your browser, and create the pull request by clicking the green button in the upper right
- someone (probably Greg) will double-check your changes, and then merge and deploy them to the live website

## Testing your changes

There are 2 ways that you can test changes. The first is to create a
temporary webserver on your development machine and look at it with a
browser. To do this, cd into the top level directory of the repo and
then type "make html" (and fix any problems it reports) and then "make
serve". While this server is running, you can look at
http://127.0.0.1:8000 in your browser and see the
website. (Everything except uploading should work.)

Alternately, you can just check in (without any testing), create a
pull request, and ask Greg to make your new content visible on the
test website, which is at https://test.content.bx9.net/
