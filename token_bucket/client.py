import socket, random, time

client_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = str(random.randint(1, 5))
    print("Data Sent:", data)

    client_server.sendto(data.encode(), ('localhost', 12345))  
    data, addr = client_server.recvfrom(1024)
    if data:
        print(data.decode())
        time.sleep(7)