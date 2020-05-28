# Caesar cipher

def encode(text, rot):
    cipher = ''
    for char in text:
        if not char.isalpha():
            cipher += char
            continue
        #char = char.upper()
        if ord(char) >= 97 and ord(char) <= 122:
            code = ord(char) + rot
            if code > ord('z'):
                i = code - ord('z')
                code = ord('a') - 1 + i
            cipher += chr(code)
        else:
            code = ord(char) + rot
            if code > ord('Z'):
                i = code - ord('Z')
                code = ord('A') - 1 + i
            cipher += chr(code)
    return cipher
        

# Caesar cipher - decrypting a message
def decode(crypt, rot):
    cipher = input('Enter your cryptogram: ')
    text = ''
    for char in cipher:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) - 1
        if code < ord('A'):
            code = ord('Z')
        text += chr(code)

#print(text)
print(encode("abcxyzABCxyz 123", 2))