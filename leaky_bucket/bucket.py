import socket, time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))

max_bucket_size = 10
current_level = 0
leak_packet = 2

def leak_buckets():
    global current_level, leak_packet

    if current_level > leak_packet - 1:
        print(f"Packets Leaked: {leak_packet} Current level: {current_level}")
        current_level -= leak_packet
    elif current_level > 0:
        print(f"Packets Leaked: {leak_packet} Current level: {current_level}")
        current_level = 0
    else:
        print("Overflow")


while True:
    data, addr = server_socket.recvfrom(1024)
    data = int(data.decode())

    if current_level + data <= max_bucket_size:
        current_level += data
        print("Data added to bucket")
    else:
        print("Overflow")

    leak_buckets()
    time.sleep(2)