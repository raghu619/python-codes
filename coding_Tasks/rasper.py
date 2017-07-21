import  Tkinter
home=Tkinter.Tk()
def btnclick():
	print("hello")
	label1.config(text="Hello")
button1=Tkinter.Button(home,text="click",command=btnclick)
button1.grid(column=10,row=10,padx=10,pady=10)
label1=Tkinter.Label(home)
label1.grid(column=0,row=0,padx=10,pady=10)
#button1.pack()
home.mainloop()	