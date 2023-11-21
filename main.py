import tkinter as tk

root = tk.Tk()
root.geometry('1280x720')
label1 = tk.Label(root,text='初めてのアコム',font = ('Arial',30))
label2 = tk.Label(root,text='初めてのアコム',font = ('Arial',30))
label3 = tk.Label(root,text='初めてのアコム',font = ('Arial',30))
label4 = tk.Label(root,text='初めてのアコム',font = ('Arial',30))
# label.pack()
# label1.pack()
# label2.pack()
# label3.pack()
# label4.pack()

# label1.grid(row=0,column=0)
# label2.grid(row=0,column=1)
# label3.grid(row=0,column=2)
# label4.grid(row=0,column=3)
# label.grid(column=0)
# label.place (x=6,y=2)
def button_click():
    text = entry.get()
    print(text)
label1.place(x=40,y=100)

button = tk.Button(root,text='ボタンだよ',font=('Arial',30),command=button_click)
button.pack()

entry = tk.Entry(root,font=('Arial',30))
entry.pack()
root.mainloop()