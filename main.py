import tkinter as tk

window=tk.Tk()
window.title("Adress Entry Form")

frame1=tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=3)
frame2=tk.Frame(master=window, relief=tk.FLAT)
frame1.pack()
frame2.pack(fill=tk.X, ipadx=5, ipady=5)
lbl1=tk.Label(master=frame1, text="First Name:")
lbl2=tk.Label(master=frame1, text="Last Name:")
lbl3=tk.Label(master=frame1, text="Adress Line 1:")
lbl4=tk.Label(master=frame1, text="Adress Line 2:")
lbl5=tk.Label(master=frame1, text="City:")
lbl6=tk.Label(master=frame1, text="State:")
lbl7=tk.Label(master=frame1, text="Postal Code:")
lbl8=tk.Label(master=frame1, text="Country:")
lbl1.grid(row=0,column=0, sticky="e")
lbl2.grid(row=1,column=0, sticky="e")
lbl3.grid(row=2,column=0, sticky="e")
lbl4.grid(row=3,column=0, sticky="e")
lbl5.grid(row=4,column=0, sticky="e")
lbl6.grid(row=5,column=0, sticky="e")
lbl7.grid(row=6,column=0, sticky="e")
lbl8.grid(row=7,column=0, sticky="e")


entry1 = tk.Entry(master=frame1, width=50)
entry2 = tk.Entry(master=frame1, width=50)
entry3 = tk.Entry(master=frame1, width=50)
entry4 = tk.Entry(master=frame1, width=50)
entry5 = tk.Entry(master=frame1, width=50)
entry6 = tk.Entry(master=frame1, width=50)
entry7 = tk.Entry(master=frame1, width=50)
entry8 = tk.Entry(master=frame1, width=50)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)
entry4.grid(row=3, column=1)
entry5.grid(row=4, column=1)
entry6.grid(row=5, column=1)
entry7.grid(row=6, column=1)
entry8.grid(row=7, column=1)

button1=tk.Button(text="Clear", master=frame2, relief=tk.RAISED)
button2=tk.Button(text="Submit", master=frame2, relief=tk.RAISED)
button2.pack(side=tk.RIGHT, padx=10,pady=10)
button1.pack(side=tk.RIGHT, ipadx=10)



window.mainloop()