import sys

message = ""
song = " Hello my name is anthony goncalves, mein yaha pe akela hoon. Mujhe asdie a dc oasdc. adfvadcas asdcadsc; asdiwpqmaf;sieurbru;\nseiw\naifarfa\nsrferijfme ajdfwer; 'fwefw wiefw sfrogerfefcsc s"
# for line in sys.stdin:
#     message += line.strip()
for line in song:
    message += line.strip()
message = message.upper()
print(message)
encryption_option = input("Would you like to Encode or Decode? ") 
cipher_number = int(sys.argv[1])
length_of_message = len(message)
encoded_message = ""
decoded_message = ""
if encryption_option.lower() == "encode":
    for i in range(length_of_message):
        ascii = ord(message[i])
        if ascii >= 65 and ascii <= 90:
            if ascii + cipher_number <= 90:
                ascii = ascii + cipher_number    #when the encoded character doesn't come after Z
            else:    
                ascii = ascii - (26 - cipher_number) #when the encoded character comes after Z
            encoded_message = encoded_message + chr(ascii)
        else:
            continue
        no_white_spaces = encoded_message.replace(" ","")
        if len(no_white_spaces) % 5 == 0:      #creating blocks of 5 letters
            encoded_message += " "
        if len(no_white_spaces) == 50:         #printing 10 blocks
            print(encoded_message)
            encoded_message = ""
    if len(encoded_message) != 5: 
        print(encoded_message.replace("  ", " "))
        


elif encryption_option.lower() == "decode":
    for i in range(length_of_message):
        ascii = ord(message[i])
        if ascii >= 65 and ascii <= 90:
            if ascii + cipher_number <= 90:
                ascii = ascii - cipher_number    #when the encoded character doesn't come after Z
            else:    
                ascii = ascii + (26 - cipher_number) #when the encoded character comes after Z
            decoded_message = decoded_message + chr(ascii)
        if len(decoded_message) % 5 == 0:      #creating blocks of 5 letters
            decoded_message += " "
        if len(decoded_message) == 60:         #printing 10 blocks
            print(decoded_message)
            decoded_message = ""
    if len(decoded_message) != 5: 
        print(decoded_message)


