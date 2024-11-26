import socket, random, time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("localhost", 12345))

while True:
    data, addr = server_socket.recvfrom(1024)
    data = data.decode()

    if not data:
        continue

    time.sleep(2)
    print("Received data:", data)
    time.sleep(2)
    if random.random() < 0.3:
        server_socket.sendto("".encode(), addr)

    else:
        server_socket.sendto("Ack recv".encode(), addr)