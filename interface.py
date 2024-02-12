from tkinter import*
window = Tk()
window.geometry("350x370")
window.title("Шифрование")
window.resizable(False, False)

choice = StringVar()

frame1 = LabelFrame(text = 'Выбор шрифта', width = 300, height = 90)
frame1.pack(side = TOP, expand = True, fill=X, pady = 1)

frame2 = LabelFrame(text = 'Данные', width = 330, height = 90)
frame2.pack(expand=True, fill=X, pady = 2)

button1 = Button(text = 'Зашифровать')
button1.pack(side=BOTTOM, expand = True, pady = 1)

frame3 = LabelFrame(text = 'Зашифрованные сообщения', width = 330, height = 90)
frame3.pack(side=BOTTOM, expand=True, fill=X, pady = 1)

#frame1
radiocaesar = Radiobutton(frame1, text = 'Шифр Цезаря', width = 20, height = 1, variable=choice, value = 'Цезарь')
radiocaesar.pack(side = TOP, expand = True, pady = 5)

radioatbash = Radiobutton(frame1, text = 'Шифр Атбаш', width = 20, height = 1, variable=choice, value = 'Атбаш')
radioatbash.pack(side = BOTTOM, expand=True, pady = 5)


#frame2
label1 = Label(frame2, text = 'Введите текст: ', width = 15, height = 1)
label1.grid(padx = 35, pady = 3, column = 0, row = 0)
label2 = Label(frame2, text = 'Введите ключ: ', width = 15, height = 1)
label2.grid(padx = 35, pady = 3, column = 1, row = 0)

plaintextbox = Entry(frame2, width=15)
plaintextbox.grid(padx = 35, pady = 7, column = 0, row = 1)
keybox = Entry(frame2, width=5)
keybox.grid(padx = 35, pady = 7, column = 1, row = 1)

#frame3

ciphername = Label(frame3, text = 'Шифр', width = 25, height = 1)
ciphername.pack(side=TOP, pady=5)

ciphermessage = Label(frame3, width = 20, height=1)
ciphermessage.pack(side=BOTTOM)


if __name__ == "__main__":
    window.mainloop()
