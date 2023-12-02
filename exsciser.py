from tkinter import *

window=Tk()
window.minsize(400,400)
window.config(padx=20,pady=20)

label=Label(text="New Text")
label.grid(column=1,row=1)
label.config(font=12)
button=Button(text="New Button")
button.grid(column=3,row=1)
button.config(padx=10, pady=5, bd=0, highlightthickness=0, bg="black", fg="white", font=("Arial", 12))
# button.config(borderwidth=0, relief="solid", highlightthickness=20, highlightbackground="white")

button2=Button(text="Button")
button2.grid(column=2,row=2)
button2.config(padx=5,pady=5)

entry=Entry()
entry.grid(column=3,row=4)
entry.config(bg="#EFEFEF", fg="black", font=("Arial", 14), bd=2, relief="solid", insertbackground="black")

window.mainloop()