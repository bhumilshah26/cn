import socket, threading, time

lock = threading.Lock()
max_bucket_size = 10
bucket_token_list = list()

def add_to_bucket():
    while True:
        with lock:
            if len(bucket_token_list) <= max_bucket_size:
                bucket_token_list.append(1)
        time.sleep(1)

def handle_client():
    print("Received message:", data)
    with lock:
        if bucket_token_list:
            bucket_token_list.pop(0)
            print("1 Token used. Bucket: ", bucket_token_list)
            server_socket.sendto("".encode(), addr)
        else:
            server_socket.sendto("No token left, wait".encode(), addr)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))
print("Server connected to localhost:12345")

threading.Thread(target=add_to_bucket, daemon=True).start() # start adding tokens to the list

while True:
    data, addr = server_socket.recvfrom(1024)
    threading.Thread(target=handle_client, daemon=True).start()