# Writeup 2 - OSINT

Name: Charlie Shin
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Charlie Shin

## Assignment Writeup

### Part 1 (45 pts)


1. What is `ejnorman84`'s real name?
	'ejnorman84's real name is Eric Norman

2. Where does `ejnorman84` work? What is the URL to their website?
	Eric Norman works at Wattsamp Energy. The URL to their website is wattsamp.net	

3. List all personal information (including social media accounts, contacts, etc) you can find about `ejnorman84`. For each, briefly detail how you discovered them.
	By using name check and other user-name searches through the OSINT Framework website, 
	I found ejnorman84 on reddit, hackernews, and instagram. I also found 
	him on mySpace, but I think that is someone else. By using whois Wattsamp.net on Kali Linux, I was able
	to find his Street: 1300 Adabel Dr, City: El Paso, State: Texas, Postal Code: 79835, Country: US, Phone: 202-656-2837
	, and email: ejnorman84@gmail.com, information. 

4. List any ( >= 1 ) IP addresses associated with the website. For each, detail the location of the server, any history in DNS, and how you discovered this information.
	By using nmap and securitytrails.com I was able to find that the IP address of the website was 157.230.179.99. Within 
	securitytrails.com, I found 4 NS record and a SOA record which has a email: cloud-dns-hostmaster@google.com and a TXT section
	that has a flag "CMSC389R-<Do-you_NOT_See_this}.
	
	

5. List any hidden files or directories you found on this website.
	On the Website there are two links, one of them is to the University of Marland Cybersecurity club, and the other is to
	the cybersecurity twitter page.

6. What ports are open on the website? What services are running behind these ports? How did you discover this?
	By using nmap on Kali Linux, the ports that are open are 22, 80, and 1337. The service for the 22 port is tcpwrapped
	and the service for the 80 port is Apache/2.4.29 (Ubuntu). I had to zenmap to find 1337, which does not tell you the service, just
	the open port.

7. Which operating system is running on the server that is hosting the website? How did you discover this?
	For the operating system, I tried using nmap, but I got the error that there are too many fingerprints that match this host to give
	specific OS details.
	

8. **BONUS:** Did you find any other flags on your OSINT mission? Note: the standard flag format for bonus flags is `*CMSC389R-{}`. (Up to 9 pts!)
	I found the flag on the security trails website. "CMSC389R-<Do-you_NOT_See_this}.

### Part 2

	In the beginning I was very confused on this part because I was not too comfortable with python and the concept of sockets. But after 
	clarification from the TA's I was able to understand how to code was supposed to function and from there the development process was standard.
	I incrementally coded where I tryed to just read from the socket at first, and then I tried to send one thing out. Then soon I was developing 
	the parsing and when I my program could communicate with the socket all the way through one time, I created a loop around the body. Then I had to put
	in sleeps in the code and wait around 30 min. for the right password to come up. The password was hello1, and the flag was in the home directory within the
	shell. The flag was in flag.txt and it was "Good! Here's your flag: CMSC389R-{!enough_nrg_4_a_str0ng_Pa$$wrd}. Some of the errors that I would run into
	is that the timing would get jumbled and it would mess up my loop so I had to put some sleeps in the middle of the method. ALso accessing the rockyou.txt did not work
	so I copied the zip rockyou into my home directory and then I unzipped it. 
