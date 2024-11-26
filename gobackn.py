import time, random

window_size = 4

ack_rcvd = 0
sent_packets = 0

total_frames = 10


while ack_rcvd < total_frames:
    for i in range(window_size):
        if sent_packets < total_frames:
            print(f"Received frames: {sent_packets}")
            sent_packets += 1
            time.sleep(1)

    for i in range(window_size):
        if ack_rcvd < total_frames:
            ack = random.choice([True, False])
            if ack:
                print(f"Ack Rvd {ack_rcvd}")
                ack_rcvd += 1
            else:
                print(f"Frame {ack_rcvd} lost, resending from this frame")
                sent_packets = ack_rcvd
                break