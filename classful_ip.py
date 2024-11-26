def generate(data):
    data = [int(octet) for octet in data]
    ip_class = ''
    subnet_mask = ''

    ip_classes = [
        ((0, 127), 'A', '255.0.0.0'),
        ((128, 191), 'B', '255.255.0.0'),
        ((192, 223), 'C', '255.255.255.0'),
        ((224, 239), 'D', None),
        ((240, 255), 'E', None)
    ]

    for ((start, end), clas, sm) in ip_classes:
        if start <= data[0] <= end:
            ip_class = clas
            subnet_mask = sm
            break

    return ip_class, subnet_mask

data = input("Enter the ip: ")
data = list(data.split('.'))

if len(data) > 4 or all(int(octet) > 255 for octet in data):
    print("Invalid IP")
    
else:
    cl, subnet_mask = generate(data)

