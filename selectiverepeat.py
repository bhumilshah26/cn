import time, random

window_size = 4
total_frames = 10

ack_rcvd = [0] * total_frames
sent_packets = [0] * total_frames

window_start = 0


while not all(ack_rcvd):
    for i in range(window_start, min(window_start + window_size, total_frames)):
        if not sent_packets[i]:
            print(f"Received frames: {i}")
            sent_packets[i] = 1
            time.sleep(1)

    for i in range(window_start, min(window_start + window_size, total_frames)):
        if not ack_rcvd[i]:
            ack = random.random() < 0.7
            if ack < 0.7:
                print(f"Ack Rvd {i}")
                ack_rcvd[i] = 1
            else:
                print(f"Frame {i} lost, resending from this frame")
                sent_packets[i] = 0

            time.sleep(1)
    
    while window_start < total_frames and ack_rcvd[window_start]:
        window_start += 1
