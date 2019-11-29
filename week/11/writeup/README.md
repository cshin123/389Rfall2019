# Writeup 1 - Web I

Name: Charlie Shin
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Charlie Shin


## Assignment details
This assignment has two parts. It is due by 11/27/19 at 11:59PM.

**There will be late penalty of 5% per day late!**

### Part 1 (40 Pts)

Such a Quick Little, website!

[http://142.93.136.81:5000/](http://142.93.136.81:5000/)

So for this part I noticed that the website has a id tag at the end of the URl. So I exploited it by replacing the
end of the URL with id = '||'1' = '1, in which the page displayed everything including the flag.

The flag is: CMSC389R-{y0u_ar3_th3_SQ1_ninj@}

### Part 2 (60 Pts)
Complete all 6 levels of:

[https://xss-game.appspot.com](https://xss-game.appspot.com)

Produce a writeup. We will not take off points for viewing the source code and/or viewing hints, but we strongly discourage reading online write-ups as that defeats the purpose of the homework.

For level 1, I passed in <script>alert()</script> into the search box because this is a search engine.

Then for level 2, the script tactic does not work however you can add in a button then when clicked it
will trigger the alert. I input <button onclick="alert();">Click</button>.

Next for level 3, here I had to look some stuff up and I noticed that you can use onerror to cause the alert to trigger
so you add ' onerror ='alert()' to the end of the URL.

Then for level 4, I noticed that for the URL, and the text box that you can inject javascript to get the alert, so after
putting in ');alert(' I was able to move on.

Next for level 5, I noticed when I clicked sign up, in the URL there is a next=confirm in the URL. So I used this to try
to trigger a alert and after inputting javascript:alert(); then clicking Next it worked.


### Format

Part 1 and 2 can be answered in bullet form or full, grammatical sentences.

### Scoring

* Part 1 is worth 40 points
* Part 2 is worth 60 points

### Tips

Remember to document your thought process for maximum credit!

Review the slides for help with using any of the tools or libraries discussed in
class.
