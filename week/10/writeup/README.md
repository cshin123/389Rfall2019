# Writeup 10 - Crypto I

Name: Charlie Shin
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Charlie Shin


## Assignment details

### Part 1 (45 Pts)

1) 16 bytes were used for the key hash, ciphertext hash, and the IV. The rest of the bytes are for the ciphertext.
2) The program uses a AES128 encryption algorithm and MD5 as a hashing algorithm. This might pose a risk because
with MD5, it can be exploited due to hashing collisions. AES128 seems safe.
3) The total file is 656 bytes.
4) The application ensure Confidentiality through AES128 and then the encryption key is derived by through hashing 
through MD5, and then taking the first 2 bytes and hashing it again
5) the application ensures integrity by comparing the cipertext hash and the password, however the hash may have 
been modified.
6) The application ensures authentication by comparing the key_hash in the file and the password the user puts in
to make sure that they are equal. This is flawed because you are able to brute force it.
7) The IV is generated using 16 bytes and then stored in the ledger. Should be safe.

### Part 2 (45 Pts)
My program uses brute force to find the password. Where I looked for every possibled
4 character password and then hashed it like in ledger.c

Flag: CMCS389R-{k3y5p4c3_2_sm411}

### Part 3 (10 Pts)
Obfuscation should be a priority to stop attackers from breaking different encryptions. Making code public
allows attackers to study and find ways to break the code, so making it not public makes it harder for them.
Making the code public would work, if there werent any malicious attacks who would abuse the information
but to be secure, some code should be hidden from the public.
