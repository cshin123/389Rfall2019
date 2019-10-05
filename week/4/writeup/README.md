# Writeup 2 - Pentesting

Name: Charlie Shin
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Charlie Shin

## Assignment Writeup

### Part 1 (45 pts)

By using command injection, in which you use semicolons and a series of commands to get into 
the system, the flag was “Good! Here’s your flag: CMSC389R-{ping_as_a_$erv1c3}.” The input that 
I used to obtain the flag, was once after you did the command nc to the website, you do ;cat /home/flag.txt. 
Once I explored the Wikipedia page on command injection, I found out that servers are vulnerable when you use 
semicolons because any command after the semicolon will run. So I used this to ignore the IP address request and 
just did ;ls. From there I began to really understand what was happening, and I just kept exploring. I did ;ls then 
I went into the directory home, because that seems like a common name for a directory that will probably have some important 
information. However the nc does time out, so the process of exploration was slow, however, I eventually got into the home directory 
and found the flag.txt. So then I just needed cat it and there’s the flag. The easiest way to prevent this vulnerability would have been to 
restrict command usage  on the application level. There is no reason for the users to have the ability to run system commands on the server. 
However, if you do not want to completely restrict command usage then you can require validation. If a person wanted to run commands on the server 
then they would be confront with a password validation, in which case they would be blocked from accessing the server. You can also neutralize different 
characters or symbols that are common for command injection. You can neutralize the use of semicolons for example, in which case would have prevented me from 
going into the system. 

### Part 2 (55 pts)

By using command injection, in which you use semicolons and a series of commands to get into the 
system, the flag was “Good! Here’s your flag: CMSC389R-{ping_as_a_$erv1c3}.” The input that I used to 
obtain the flag, was once after you did the command nc to the website, you do ;cat /home/flag.txt. Once I explored 
the Wikipedia page on command injection, I found out that servers are vulnerable when you use semicolons because any command 
after the semicolon will run. So I used this to ignore the IP address request and just did ;ls. From there I began to really understand 
what was happening, and I just kept exploring. I did ;ls then I went into the directory home, because that seems like a common name for a 
directory that will probably have some important information. However the nc does time out, so the process of exploration was slow, however, 
I eventually got into the home directory and found the flag.txt. So then I just needed cat it and there’s the flag. The easiest way to prevent this 
vulnerability would have been to restrict command usage  on the application level. There is no reason for the users to have the ability to run system 
commands on the server. However, if you do not want to completely restrict command usage then you can require validation. If a person wanted to run commands 
on the server then they would be confront with a password validation, in which case they would be blocked from accessing the server. You can also neutralize 
different characters or symbols that are common for command injection. You can neutralize the use of semicolons for example, in which case would have prevented
 me from going into the system. 
