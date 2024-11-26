import socket, random, time

client_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = str(random.randint(1, 5))
    client_server.sendto(data.encode(), ('localhost', 12345))
    print(f"Packet Sent: {data}")

    time.sleep(1)