alphabet1 = 'abcdefghijklmnopqrstuvwxyz'
def caesar_encrypt(plaintext, key):
    ciphertext = ''
    for i in plaintext.lower():
        if i in alphabet1:
            index = alphabet1.find(i)
            new_index = index+key
            new_letter = alphabet1[new_index%len(alphabet1)]
            ciphertext += new_letter
        else:
            ciphertext += i
    return ciphertext
        
def caesar_descrypt(plaintext, key):
    ciphertext = ''
    for i in plaintext.lower():
        if i in alphabet1:
            index = alphabet1.find(i)
            new_index = index-key
            new_letter = alphabet1[new_index%len(alphabet1)]
            ciphertext += new_letter
        else:
            ciphertext += i
    return ciphertext

alphabet2 = 'zyxwvutsrqponmlkjihgfedcba'
def atbash_encrypt(plaintext):
    ciphertext = ''
    for i in plaintext.lower():
        if i in alphabet1:
            index = alphabet1.find(i)
            letter = alphabet2[index]
            ciphertext += letter
        else:
            ciphertext+= i
    return ciphertext
    
#def hacking(plaintext):
    #for i in range(len(alphabet)):
        #print(caesar_descrypt(plaintext, i))


