# Writeup 8 - Binaries II

Name: Charlie Shin
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Charlie Shin

## Assignment Writeup

### Part 1 (100 pts)
Answer the following questions regarding the server executable (for which source is provided).

1. How is the per-session administrator password generated? Are there any inherent weaknesses in this implementation?
 The password is generated from the seed of the current system time. So two instances of the same server could generate the 
same password, and this can be exploited because we are given the server's code.

2. Describe two vulnerabilities in this program. Provide specific line numbers and classifications of the vulnerability. Explain potential ramifications as well as ways to avoid these vulnerabilities when writing code.
 One of the vulnerabilities is on line 68, and that is buffer overflow. The length
of the input string should be checked, or else the user can enter as many bytes as they want.
When the buffer is overflowed, then it will go to commands in which the server can be exploited, to prevent this
specify the max number of bytes to read.

 Another vulnerability is string injection on line 46. Because the string depends on user input, the user can 
inject format sequences like "%d" to read information from the memory or the stack.

3. What is the flag?



4. Describe the process you followed to obtain the flag: vulnerabilities exploited, your inputs to the server in a human-readable format, etc. If you create any helper code please include it.
