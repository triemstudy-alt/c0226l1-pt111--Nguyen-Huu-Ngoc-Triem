import tkinter as tk

# cửa sổ chính
root = tk.Tk()
root.title("Calculator")
root.geometry("300x350")

# màn hình hiển thị
input_text = tk.StringVar()

display = tk.Entry(root,
                   textvariable=input_text,
                   font=("Arial",20),
                   justify="right")

display.grid(row=0,column=0,columnspan=4,ipady=10,padx=5,pady=5)

# các nút
buttons = [
    ('C',1,0),('√',1,1),('^',1,2),('%',1,3),
    ('1',2,0),('2',2,1),('3',2,2),('+',2,3),
    ('4',3,0),('5',3,1),('6',3,2),('-',3,3),
    ('7',4,0),('8',4,1),('9',4,2),('*',4,3),
    ('0',5,0),('.',5,1),('=',5,2),('/',5,3)
]

for (text,row,col) in buttons:

    if text == "=":
        button = tk.Button(root,text=text,width=5,height=2,
                            bg="orange")
    elif text == "C":
        button = tk.Button(root,text=text,width=5,height=2)               
    else:
        button = tk.Button(root,text=text,width=5,height=2)
                          
    button.grid(row=row,column=col,sticky="nsew",padx=2,pady=2)

# làm nút giãn đều
for i in range(6):
    root.rowconfigure(i,weight=1)

for i in range(4):
    root.columnconfigure(i,weight=1)

root.mainloop()