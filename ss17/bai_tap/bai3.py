import tkinter as tk

root = tk.Tk()
root.title("Address_Entry_Form")
root.geometry("600x300")

label = tk.Label(root, text="First name")
label.grid(row=1, column=0)
fname = tk.Entry(root)
fname.grid(row=1, column=1)

label = tk.Label(root, text="Last name")
label.grid(row=2, column=0)
lname = tk.Entry(root)
lname.grid(row=2, column=1)

label = tk.Label(root, text="Address line 1")
label.grid(row=3, column=0)
adr = tk.Entry(root)
adr.grid(row=3, column=1)

label = tk.Label(root, text="Address line 2")
label.grid(row=4, column=0)
adr2 = tk.Entry(root)
adr2.grid(row=4, column=1)

label = tk.Label(root, text="City")
label.grid(row=5, column=0)
city = tk.Entry(root)
city.grid(row=5, column=1)

label = tk.Label(root, text="Province")
label.grid(row=6, column=0)
prv = tk.Entry(root)
prv.grid(row=6, column=1)

label = tk.Label(root, text="Postal Code")
label.grid(row=7, column=0)
pc = tk.Entry(root)
pc.grid(row=7, column=1)

label = tk.Label(root, text="Country")
label.grid(row=8, column=0)
ctr = tk.Entry(root)
ctr.grid(row=8, column=1)

btn1 = tk.Button(root, text="Clear")
btn1.grid(row=9, column=2)

btn2 = tk.Button(root, text="Submit")
btn2.grid(row=9, column=3)

root.mainloop() 