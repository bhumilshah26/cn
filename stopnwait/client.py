import socket, time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = input("Enter the data to be sent:")
    client_socket.sendto(data.encode(), ('localhost', 12345))

    client_socket.settimeout(5)
    ack, addr = client_socket.recvfrom(1024)
    ack = ack.decode()

    if ack:
        print("Data ack recevied")
    else:
        print("Retransmitting data", data)
        client_socket.sendto(data.encode(), ("localhost", 12345))