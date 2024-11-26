def character_count():
    frames = int(input("Enter the number of frames: "))
    transmitted_message=''

    for i in range(frames):
        message = input(f"Enter message {i+1}: ")
        c = str(len(message) + 1) + message
        transmitted_message += c

    return transmitted_message


def byte_stuffing():
    message = input("Enter the message: ")
    s = input("Enter the start character: ")
    e = input("Enter the end character: ")
    esc = input("Enter the escape character: ")
    transmitted_message = s

    for i in range(len(message)):
        if message[i] == s or message[i] == e or message[i] == esc:
            transmitted_message += f'{esc}'
        transmitted_message += message[i]

    transmitted_message += str(e)

    return transmitted_message

def bit_stuffing():
    data = list(input("Enter binary data: "))
    transmitted_message = ''
    
    c = 0

    for i in range(len(data)):
        c = c + 1 if data[i] == '1' else 0

        if c == 6:
            transmitted_message += str(0)
            c = 0

        transmitted_message += str(data[i])
    
    return transmitted_message



# print("character count:")
# transmitted_message_character_count=character_count()
# print("transmitted message character count:"+transmitted_message_character_count)


# print("byte stuffing:")
# transmitted_message_byte_stuffing=byte_stuffing()
# print("transmitted message byte stuffing:"+transmitted_message_byte_stuffing)


print("bit stuffing:")
transmitted_message_bit_stuffing=bit_stuffing()
print("transmitted message bit stuffing:"+transmitted_message_bit_stuffing)

        