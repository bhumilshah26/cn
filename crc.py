def crc(data, divisor, c):
    cpy = list(data)
    n = len(data) 
    m = len(divisor)
    cpy += ['0'] * (m - 1) if c else [] # append zeros if sending (c = 1) else append nothing (c = 0)
    n -= (m - 1) if not c else 0 # iterate of only the data bits and not the remainder as well

    for i in range(n):
        if cpy[i] == '1':
            for j in range(m):
                cpy[i + j] = '0' if cpy[i + j] == divisor[j] else '1'

    return ''.join(cpy[-(m - 1):])            

send_mssg = input("Enter the data: ")
divisor = list(input("Enter the divisor: "))

remainder = crc(send_mssg, divisor, 1)
print("Data Sent: ", send_mssg + remainder)

recv_mssg = input("Enter the received message: ")
remainder = crc(recv_mssg, divisor, 0)

if remainder == '0' * (len(divisor) - 1):
    print("No error")
else:
    print("Error found, Remainder: ", remainder)