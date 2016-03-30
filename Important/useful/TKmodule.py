# coding utf-8

from tkinter import *
from tkinter.ttk import Combobox

root = Tk() # ñîçäàåì îêíî
root.title("Hello World!") # çàãîëîâîê
root.geometry('300x300') # ðàçìåð îêíà


# callback - ïðè íàæàòèè íà êíîïêó
def button_clicked():
    print(e.get())

# ïðè çàêðûòèè
def close():
    root.destroy()
    root.quit()


# ñîçäàåì êíîïêó
button = Button(root, text="Press Me", command=button_clicked, height="5")
button.pack(fill=BOTH) # îòîáðàçèòü íà îêíå

# ñîçäàåì òåêñòîâîå ïîëå
e = Entry(root)
e.pack() # îòîáðàçèòü

# e.delete(0, END)
# e.insert(0, "a default value")



def makeentry(parent, caption, width=None, **options):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry
#
# user = makeentry(root, "User name:", 10)
# password = makeentry(root, "Password:", 10, show="*")
#
# def login_clicked():
#     print(user.get(), password.get())
#
# login = Button(root, text="Login", command=login_clicked, height="5")
# login.pack(fill=BOTH) # îòîáðàçèòü íà îêíå

def set(*args):
    print(combo.get())
    e.delete(0, END)
    e.insert(0, combo.get())

combo = Combobox(root, values=['1', '2', '3'], state='readonly')
combo.bind('<<ComboboxSelected>>', set)
combo.pack()


root.protocol('WM_DELETE_WINDOW', close) # çàêðîåòñÿ ïðèëîæåíèå ïî çàêðûòèþ îêíà

root.mainloop() # çàïóñêàåì ïðîãðàììó
