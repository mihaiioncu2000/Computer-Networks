import socket, threading, time



shutdown = False
join = False

def receving (name, sock):
	while not shutdown:
		try:
			while True:
				data, addr = sock.recvfrom(1024)
				print(data.decode("utf-8"))
				time.sleep(0.2)
		except:
			pass # trecem de eroare(daca e)
host = socket.gethostbyname(socket.gethostname())
port = 0 #clientul doar se conecteza,nu o creaza

server = ("169.254.165.112",9090)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

alias = input("Name: ")

rT = threading.Thread(target = receving, args = ("RecvThread",s))
rT.start()

while shutdown == False: #cat clientul nu a iesit
	if join == False: 
		s.sendto(("["+alias + "] => join chat ").encode("utf-8"),server)
		join = True
	else:
		try:
			message = input()
			if message != "":
				s.sendto(("["+alias + "] :: "+message).encode("utf-8"),server)
			
			time.sleep(0.2)
		except: # ctrl c de exemplu
			s.sendto(("["+alias + "] <= left chat ").encode("utf-8"),server)
			shutdown = True

rT.join() #join pentru timp
s.close()
input()