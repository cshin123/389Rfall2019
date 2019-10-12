# Writeup 6 - Binaries I

Name: Charlie Shin
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Charlie Shin

## Assignment Writeup

### Part 1 (50 pts)

CMSC389R-{di5a55_0r_d13}

### Part 2 (50 pts)

At first, I just ran the crackme binary and that was when the message of “Did you 
even try dissembling” came up, and then I looked at the assembly. I recognized that 
the executable required arguments, so then I tried providing arguments, however they 
were incorrect because it did not pass the first check. From the first check, the assembly 
was taking an argument and comparing it to the string “Oh God” and if the string matches 
then you can move on. So after running the executable with the string “Oh God” it would 
fail the second check, that would mention “not like the environment.” I realized that this 
check would call getenv on FOOBAR, but when I checked the environment variables there was 
no FOOBAR. So I had to create a environment by doing export FOOBAR=”seye ym “. The reason 
that I had to set FOOBAR to “seye ym “ was because after the getenv call, the code would 
see whether the value of the pointer that it got from getenv was “seye ym .” Then after 
setting the environment variable, I ran the executable and got the “Almost there” because 
I was failing the third check. The beginning of the third check showed that it wanted to 
open a file named “sesame” so I created sesame by running touch sesame in the terminal. 
Then I saw all of the cases and as I was using the down arrow keys to trace through the 
code, I realized that it was a loop, and the loop was checking the contents of the file. 
As part of the check would open the file, read it, and then close it. So then I went 
through the cases and translated the hex numbers into ascii, which was “ they burn”. Then 
I had reverse the FOOBAR environment variable, so it was “ my eyes” and then running the 
crackme executable again, caused the flag to be printed. Most of the checks required calling
functions and comparing the output, however, the functions that would be called would 
be different for each check. The first check is unique as it just compared the argument
with a string.
