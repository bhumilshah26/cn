import math

def calculate_parity_bits(parity_index, hamming_code, l):
    i = parity_index
    count = 0

    while i < l + 1:
        j = i

        while j < l + 1 and j < i + parity_index:
            count += hamming_code[j - 1]
            j += 1
        
        i = j + parity_index

    return count % 2

def encode():
    mp = {1: 2, 2: 3, 3: 3, 4: 3, 5: 4}
    parity_indices = []

    input_data = list(input("Enter the data: "))
    data_length = len(input_data)
    data_index = 0

    hamming_code = [0] * (data_length + mp[data_length])

    for index in range(len(hamming_code) - 1, -1, -1):
        if not math.log2(index + 1).is_integer():
            hamming_code[index] = int(input_data[data_index])
            data_index += 1
        else:
            hamming_code[index] = calculate_parity_bits(index + 1, hamming_code, data_length + mp[data_length])
            parity_indices.append(index)
    
    return hamming_code, parity_indices

def decode(recv_mssg, parity_indices, l):
    err = 0

    for index in parity_indices:
        if calculate_parity_bits(index + 1, recv_mssg, l):
            err += index + 1

    if err:
        recv_mssg[err - 1] = 1 - recv_mssg[err - 1]

        print("Error found at position", err)
        print("Corrected message: ", recv_mssg)
        return

    print("No Error")

sent_data, parity_indices = encode()
print("Data Sent: ", sent_data)

recv_mssg = list(input("Enter received data: "))
recv_mssg = [int(bit) for bit in recv_mssg]

decode(recv_mssg[::-1], parity_indices, len(recv_mssg))