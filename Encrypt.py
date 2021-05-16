message = input("""Enter message to encrypt: """)

encrypt_message = ""
for letter in message:
    if letter == ' ':
        encrypt_message += ' '
    else:
        encrypt_message += chr(ord(letter) + 7)

print("\n~~ Encrypted Message: ~~")
print(encrypt_message)