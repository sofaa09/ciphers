import interface
from ciphers import caesar_encrypt, atbash_encrypt
def encrypt():
    currentcipher = interface.choice.get()
    if currentcipher == 'Цезарь':   
        plaintext = interface.plaintextbox.get()
        key = int(interface.keybox.get())       
        interface.ciphermessage['text'] = caesar_encrypt(plaintext, key)
    elif currentcipher == 'Атбаш':
        plaintext = interface.plaintextbox.get()
        interface.ciphermessage['text'] = atbash_encrypt(plaintext)

interface.button1['command']= encrypt

def change_cipher():
    currentcipher = interface.choice.get()
    #interface.ciphermessage['text'] = currentcipher
    #if currentcipher == 'Цезарь':
        #interface.ciphername = 'Цезарь'
    #elif currentcipher == 'Атбаш':
        #interface.ciphername = 'Атбаш'
    if currentcipher == 'Цезарь':
        interface.ciphername['text'] = 'Зашифровано шифром Цезаря'
        interface.keybox['state']='normal'
    elif currentcipher == 'Атбаш':
        interface.ciphername['text'] = 'Зашифровано шифром Атбаш'
        interface.keybox['state']='disabled'

interface.radiocaesar.config(command=change_cipher)
interface.radioatbash.config(command=change_cipher)
interface.choice.set('Атбаш')
change_cipher()

interface.window.mainloop()
