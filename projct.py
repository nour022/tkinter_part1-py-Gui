from  tkinter import *

window = Tk()
window.minsize(width=300,height=200)
window.config(pady=20,padx=20)
entry=Entry()
entry.config(width=10,bg="#EFEFEF", fg="black", font=("Arial", 14), bd=1, relief="solid", insertbackground="black")
entry.grid(column=2,row=1)

miles=Label(text="Miles")
miles.grid(column=3,row=1)

label=Label(text=f"is equal to")
label.grid(row=2,column=1)

label2=Label(text="0")
label2.grid(row=2,column=2)

label3= Label(text="KM")
label3.grid(row=2,column=3)

def on_click():
	text=round(int(entry.get())*1.60932)
	label2.config(text=text)
	
button=Button(text="Calculate",command=on_click)
button.grid(row=3,column=2)
window.mainloop()