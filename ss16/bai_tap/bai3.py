import tkinter as tk

root = tk.Tk()
root.title("Address_Entry_Form")
root.geometry("600x300")

#def lg():
#    label = tk.Label(root,text ="Login")
#    label.place(x=100, y=20)

def fName():
    label = tk.Label(root, text="First name")
    label.grid(row=1, column=0)
    entry = tk.Entry(root)
    entry.grid(row=1, column=1)

def lName():
    label = tk.Label(root, text="Last name")
    label.grid(row=2, column=0)
    entry = tk.Entry(root)
    entry.grid(row=2, column=1)

def ad1():
    label = tk.Label(root, text="Address line 1")
    label.grid(row=3, column=0)
    entry = tk.Entry(root)
    entry.grid(row=3, column=1)

def ad2():
    label = tk.Label(root, text="Address line 2")
    label.grid(row=4, column=0)
    entry = tk.Entry(root)
    entry.grid(row=4, column=1)

def city():
    label = tk.Label(root, text="City")
    label.grid(row=5, column=0)
    entry = tk.Entry(root)
    entry.grid(row=5, column=1)

def pr():
    label = tk.Label(root, text="Province")
    label.grid(row=6, column=0)
    entry = tk.Entry(root)
    entry.grid(row=6, column=1)

def code():
    label = tk.Label(root, text="Postal Code")
    label.grid(row=7, column=0)
    entry = tk.Entry(root)
    entry.grid(row=7, column=1)

def country():
    label = tk.Label(root, text="Country")
    label.grid(row=8, column=0)
    entry = tk.Entry(root)
    entry.grid(row=8, column=1)

def btn1():
    button = tk.Button(root, text="Clear")
    button.grid(row=9, column=2)

def btn2():
    button = tk.Button(root, text="Submit")
    button.grid(row=9, column=3)

fName()
lName()
ad1()
ad2()
city()
pr()
code()
country()
btn1()
btn2()

root.mainloop() 