import socket
import threading

bind_ip = "172.20.142.133"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.listen(5)

print("[*] Listening on %s:%d" % (bind_ip, bind_port))

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print ("[*] Received: %s") % request
    client_socket.send("ACK!")
    client_socket.close()

while True:
    clien, addr = server.accept()
    print("[*] Accepted connection from: %s:%d") % (addr[0], addr[1])

    client_handler = threading.Thread(target = handle_client, args=(client,))
    client_handler.start()