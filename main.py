from tkinter import *
import random
import pyperclip

tk=Tk()
tk.geometry('300x300')
tk.configure(background='skyblue')


pswd=StringVar()


passlen=IntVar()
passlen.set('Enter Length')


def password_generator():
    characters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 !@#$%^&*()'
    password=''
    if passlen.get()>=8:
        for i in range(passlen.get()):
            password+=random.choice(characters)
        pswd.set(password)


def copyclipboard():
    random_password = pswd.get()
    pyperclip.copy(random_password)
    Label(tk,text="Copied to Clipboard",bg="red").pack(pady=6)


Label(tk, text="Enter the number to get password \n (Minimum length should be 8)",bg='Blue',fg='white').pack(pady=3)


Entry(tk, textvariable=passlen).pack(pady=3)


Button(tk, text="Generate Password", command=password_generator,bg='black',fg='white').pack(pady=7)
Entry(tk, textvariable=pswd).pack(pady=3)

Button(tk, text="Copy to clipboard", command=copyclipboard,bg='black',fg='white').pack()

tk.mainloop()