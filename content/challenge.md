title: Analysis Challenge #1
slug: challenge
category: challenge

blah blah

## Submit your results

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
