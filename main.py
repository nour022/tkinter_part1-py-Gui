from tkinter import *

window= Tk() # to call the class
window.title("OnlineShop")
window.minsize(width=500,height=300)

#lebel
my_label= Label(text="OnlineShop", font=("Arial",24,"bold"))
my_label.pack(side="top")

# Entry text input:
input= Entry(width=10)

input.pack()

#Button
def button_click():
	text=input.get()
	my_label.config(text=text)
	
my_button=Button(text="Click My",command=button_click)
my_button.pack()


# descripion text
text_d=Text(width=40,height=3)
text_d.pack()
#positon mehtod  place()
label2=Label(text="onlineShop")
label2.place(y=0,x=20)

label3=Label(text="WagenKorb")
label3.place(y=0,x=420)

# Grid
# label2=Label(text="onlineShop")
# label2.grid(column=5,row=5)





window.mainloop()    # is a same  while t shode the programm work
