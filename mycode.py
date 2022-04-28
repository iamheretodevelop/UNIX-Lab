import sys

message = ""
prompt = input()
for line in prompt:
    message += line.strip()
message = message.upper()
cipher_number = int(sys.argv[1])
length_of_message = len(message)
final_cipher = ""
for i in range(length_of_message):
    ascii = ord(message[i])
    if ascii >= 65 and ascii <= 90:
        ascii = ascii - 65
        ascii = (ascii + cipher_number) % 26
        final_cipher = final_cipher + chr(ascii + 65)
    else:
        continue
    no_white_spaces = final_cipher.replace(" ","")
    if len(no_white_spaces) % 5 == 0:      #creating blocks of 5 letters
        final_cipher += " "
    if len(no_white_spaces) == 50:         #printing 10 blocks
        print(final_cipher)
        final_cipher = ""
if len(final_cipher) != 5: 
    print(final_cipher)
