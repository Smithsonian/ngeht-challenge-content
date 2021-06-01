title: Analysis Challenge #3
slug: challenge3

You might need to have a shell script:

    :::bash
    echo "this is a shell script!"

or a python script:

    :::python
    print('this is a python script!')




## Submit your results

<form action="/upload" method="post" accept-charset="utf-8"
      enctype="multipart/form-data">

    <input type="hidden" name="challenge" value="challenge3"/>
    <input type="text" name="name" placeholder="Your Name"/><br/>
    <input type="email" name="email" placeholder="Your Email"/><br/>
    <input type="text" name="team" placeholder="Your Team"/><br/>
    <label for="zip">zip file: </label>
    <input id="zip" name="zip" type="file" value=""/><br/>

    <input type="submit" value="submit"/>
</form>
