import socket

HOST = '127.0.0.1'
PORT = 8001
BUFFER_SIZE = 1024

def main():
    host = 'www.google.com'
    port = 80 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        print('Starting proxy server')
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxy_start.bind((HOST, PORT))
        proxy_start.listen(1) #only listen to 1 connection  

        while True:
            conn, addr = proxy_start.accept() #accept incoming connections
            print('Connected by: ', addr)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                ('Connecting to Google')
                try:
                    remote_IP = socket.gethostbyname(host)
                    proxy_end.connect((remote_IP, port))
                    send_full_data = conn.recv(BUFFER_SIZE)
                    proxy_end.sendall(send_full_data)
                    proxy_end.shutdown(socket.SHUT_WR)

                    data = proxy_end.recv(BUFFER_SIZE)
                    conn.send(data)
                except socket.gaierror:
                    print('Host name could not be resilved, exiting.')
            conn.close()
if __name__ == "__main__":
    main()