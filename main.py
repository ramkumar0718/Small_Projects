
Input = input("""Enter message: """)
print("\n1. Encrypt ")
print("2. Decrypt ")

option = int(input("\nEnter your option(1/2): "))
encrypt_message = ""
decrypt_message = ""

def msg(message, opt):
    for letter in Input:
        if letter == ' ':
            message += ' '     
        else:
            if opt == 1:
                message += chr(ord(letter) + 7)
            else:
                message += chr(ord(letter) - 7)

    print("\n~~ Final Message: ~~")
    print(message)


if option == 1 or option == 2:
    if option == 1:
        msg(encrypt_message, 1)

    else:
        msg(decrypt_message, 2)      
else:
    print("Wrong Option !")
