Charlie Shin
# Operational Security and Social Engineering

## Assignment details

This assignment has two parts. It is due by 9/20 at 11:59 PM.

**There will be a late penalty of 5% off per day late!**

### Part 1

For me to social engineer this information out of Eric Norman, I need to use the information I learned about him from OSINT, 
to connect to him. He is a control specialist, so he may not be so easily fooled if I called for a technical problem. However, 
Eric has shown interest in football and the security field. So I would contact him probably through reddit, where I can respond with 
his comment, to peak his interest. I’ll start having interests in what he finds interesting so we can carry on a conversation. The 
beginning stage of this social engineering is not extracting the information, but fooling him into thinking that I am his friend. Then
if his mother had a pet, Eric probably is close with pets, so I’ll start talking about my own fake experiences with pets. People are 
more likely to open up if the other person opens up too. I’ll start talking about my own pets and then lean in towards my mothers first pet, 
which would be all made-up. Then Eric would give me the name of his mother’s first pet. You need to start off with the light conversation 
questions. From there we could talk about heritage and where each of our parents were born. And then I can talk about how my mother 
never changed her maiden name and then Eric will most likely be open to tell me that his mother changed hers from blank to whatever. We 
can start leaning towards browsers and what our parents use. Then hopefully I learning enough about the mother where I can find any information 
about her online, and his mother is probably gullible, so I can call her about a transaction issue and then make her give up her ATM pin number.


### Part 2

One of the vulnerabilities of the website, was the lack of response from a brute force attack. I wrote a 
python that would go down a password list and it would go on for 40 minutes until I found the right one. A 
common fix for brute force attacks would be to limit the amount of failed responses. This is a common practice, 
where if you keep getting a password login incorrect, you will not be allowed to keep logging in. You can have it 
where you need to contact the desk to relog into your account, and this would make brute forcing impossible. 
There are also 7 more ways to stop brute force attacks from the website
https://phoenixnap.com/kb/prevent-brute-force-attacks Another vulnerability was the open port in which we attacked. 
You need to open up a firewall and find a way to close the open port. In this website
https://windows.tips.net/T013105_Closing_an_Open_Port.html they close an open port. Lastly, another vulnerability 
was the fact that nmap was able to gather so much information. That is where I found phone numbers, address, and the 
real name. In the website https://nmap.org/book/defenses.html they talk about defenses against nmap, where possible defenses 
include “blocking the probes, restricting information returned, slowing down the nmap scan, and returning misleading information”

### Format

The submission should be answered in bullet form or full, grammatical sentences. It should also be stored in `assignments/3_OPSEC_SE/writeup/README.md`. Push it to your GitHub repository by the deadline.

### Scoring

Part 1 is worth 40 points, part 2 is worth 60 points. The rubric with our expectations can be found on the ELMS assignment posting.

Good luck!
