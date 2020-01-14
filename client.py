import socket 

HOST = "www.google.com"
PORT = 80
BUFFER_SIZE = 1024

#Has to be separated by \r\n otherwise it won't work 
payload = 'GET / HTTP/1.0\r\nHost: '+ HOST +'\r\n\r\n'

def main():

	#addr_info -> [(<AddressFamily.AF_INET6: 30>, <SocketKind.SOCK_STREAM: 1>, 6, '', ('2607:f8b0:400a:809::2004', 80, 0, 0)), (<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_STREAM: 1>, 6, '', ('172.217.14.196', 80))]
	addr_info = socket.getaddrinfo(HOST, PORT, proto=socket.SOL_TCP)
	address = addr_info[0]
	connect_socket(address)

def connect_socket(address):
	(family, socketype, proto, cannoname, socket_address) = address
	try:
		s = socket.socket(family, socketype, proto)
		s.connect(socket_address)
		print("Connected")
		full_data = b''   #Full data has to be byte string otherwise it won't work  
		s.sendall(payload.encode())    #Client sends the request 
		s.shutdown(socket.SHUT_WR)
		while True:			
			data = s.recv(BUFFER_SIZE)     #Client receives the response from server 
			if not data:
				break
			full_data += data
		print(full_data)
	except:
		print("failed to connect")

main()