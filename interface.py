from tkinter import*
window = Tk()
window.geometry("350x370")
window.title("encrypt")
window.resizable(False, False)

choice = StringVar()

frame1 = LabelFrame(text = 'font selection', width = 300, height = 90)
frame1.pack(side = TOP, expand = True, fill=X, pady = 1)

frame2 = LabelFrame(text = 'data', width = 330, height = 90)
frame2.pack(expand=True, fill=X, pady = 2)

button1 = Button(text = 'encrypt')
button1.pack(side=BOTTOM, expand = True, pady = 1)

frame3 = LabelFrame(text = 'encrypted messages', width = 330, height = 90)
frame3.pack(side=BOTTOM, expand=True, fill=X, pady = 1)

#frame1
radiocaesar = Radiobutton(frame1, text = 'Caesars cipher', width = 20, height = 1, variable=choice, value = 'caesar')
radiocaesar.pack(side = TOP, expand = True, pady = 5)

radioatbash = Radiobutton(frame1, text = 'Atbash cipher', width = 20, height = 1, variable=choice, value = 'atbash')
radioatbash.pack(side = BOTTOM, expand=True, pady = 5)


#frame2
label1 = Label(frame2, text = 'enter message: ', width = 15, height = 1)
label1.grid(padx = 35, pady = 3, column = 0, row = 0)
label2 = Label(frame2, text = 'enter key: ', width = 15, height = 1)
label2.grid(padx = 35, pady = 3, column = 1, row = 0)

plaintextbox = Entry(frame2, width=15)
plaintextbox.grid(padx = 35, pady = 7, column = 0, row = 1)
keybox = Entry(frame2, width=5)
keybox.grid(padx = 35, pady = 7, column = 1, row = 1)

#frame3

ciphername = Label(frame3, text = 'cipher: ', width = 25, height = 1)
ciphername.pack(side=TOP, pady=5)

ciphermessage = Label(frame3, width = 20, height=1)
ciphermessage.pack(side=BOTTOM)


if __name__ == "__main__":
    window.mainloop()
