import socket 
from multiprocessing import Pool  
import time

HOST = '127.0.0.1'
PORT = 8001
BUFFER_SIZE = 1024

#Has to be separated by \r\n otherwise it won't work 
payload = 'GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n'

def main():
    address = [(HOST, PORT)]
    with Pool() as p:
        p.map(connect, address*10)

def connect(address):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(address)
        print("Connected")
        s.sendall(payload.encode())    #Client sends the request 
        s.shutdown(socket.SHUT_WR)
        full_data = s.recv(BUFFER_SIZE)
        print(full_data)
        time.sleep(1.0)
    except Exception as e:
        print(e)
    finally: 
        s.close()
		

main()