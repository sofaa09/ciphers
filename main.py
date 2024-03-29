import interface
from ciphers import caesar_encrypt, atbash_encrypt
def encrypt():
    currentcipher = interface.choice.get()
    if currentcipher == 'caesar':   
        plaintext = interface.plaintextbox.get()
        key = int(interface.keybox.get())       
        interface.ciphermessage['text'] = caesar_encrypt(plaintext, key)
    elif currentcipher == 'atbash':
        plaintext = interface.plaintextbox.get()
        interface.ciphermessage['text'] = atbash_encrypt(plaintext)

interface.button1['command']= encrypt

def change_cipher():
    currentcipher = interface.choice.get()
    if currentcipher == 'caesar':
        interface.ciphername['text'] = 'encrypted with Caesars cipher'
        interface.keybox['state']='normal'
    elif currentcipher == 'atbash':
        interface.ciphername['text'] = 'encrypted with Atbash cipher'
        interface.keybox['state']='disabled'

interface.radiocaesar.config(command=change_cipher)
interface.radioatbash.config(command=change_cipher)
interface.choice.set('atbash')
change_cipher()

interface.window.mainloop()
