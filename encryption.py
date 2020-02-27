alphabet= ('abcdefghijklmnopqrstuvwxyz')
key= int(input('Enter your Secret Key: '))
newMessage= ''
message= input('Enter a Message: ')
for character in message:
    if character in alphabet:
        position= alphabet.find(character)
        newPosition= (position + key) %26
        newCharacter= alphabet[newPosition]
        newMessage+= newCharacter
    else:
        newMessage+= character
print('Encrypted Message is: ',newMessage)
