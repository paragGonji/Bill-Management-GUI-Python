from tkinter import *

root = Tk()
root.geometry("1000x500")
root.title("Bill Management")
root.resizable(False, False)

def Reset():
    entry_dosa.delete(0, END)
    entry_Cookies.delete(0, END)
    entry_Tea.delete(0, END)
    entry_Coffee.delete(0, END)
    entry_Juice.delete(0, END)
    entry_Pancakes.delete(0, END)
    entry_Milk.delete(0, END)

def Total():
    try:
        a1 = int(dosa.get())
    except:
        a1 = 0
    try:
        a2 = int(Cookies.get())
    except:
        a2 = 0
    try:
        a3 = int(Tea.get())
    except:
        a3 = 0
    try:
        a4 = int(Coffee.get())
    except:
        a4 = 0
    try:
        a5 = int(Juice.get())
    except:
        a5 = 0
    try:
        a6 = int(Pancakes.get())
    except:
        a6 = 0
    try:
        a7 = int(Milk.get())
    except:
        a7 = 0

    c1 = 60 * a1
    c2 = 30 * a2
    c3 = 7 * a3
    c4 = 100 * a4
    c5 = 20 * a5
    c6 = 35 * a6
    c7 = 7 * a7

    lb1_total = Label(f2, font=('aria', 20, 'bold'), text="Total", width=16, fg="lightyellow", bg="black")
    lb1_total.place(x=0, y=50)
    entry_total = Entry(f2, font=("aria", 20, 'bold'), textvariable=Total_bill, bd=6, width=15, bg="lightgreen")
    entry_total.place(x=20, y=100)

    totalcost = c1 + c2 + c3 + c4 + c5 + c6 + c7
    string_bill = "Rs. " + str('%.2f' % totalcost)
    Total_bill.set(string_bill)

Label(text="Bill Management", bg="black", fg="white", font=("calibri", 33), width="300", height="2").pack()

f = Frame(root, bg="lightgreen", highlightbackground="black", highlightthickness=1, width=300, height=370)
f.place(x=10, y=118)

Label(f, text="Menu", font=("Gabriola", 40, "bold"), fg="black", bg="lightgreen").place(x=80, y=0)

Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Dosa...................RS.60/plate", fg="black", bg="lightgreen").place(x=10, y=80)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Cookies..............RS.30/plate", fg="black", bg="lightgreen").place(x=10, y=110)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Tea.....................RS.7/plate", fg="black", bg="lightgreen").place(x=10, y=140)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Coffee.................RS.100/plate", fg="black", bg="lightgreen").place(x=10, y=170)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Juice...................RS.20/plate", fg="black", bg="lightgreen").place(x=10, y=200)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Pancakes............RS.35/plate", fg="black", bg="lightgreen").place(x=10, y=230)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Milk.....................RS.7/plate", fg="black", bg="lightgreen").place(x=10, y=260)

f2 = Frame(root, bg="lightyellow", highlightbackground="black", highlightthickness=1, width=300, height=370)
f2.place(x=690, y=118)

Bill = Label(f2, text="Bill", font=('calibri', 20), bg="lightyellow")
Bill.place(x=120, y=10)

f1 = Frame(root, bd=5, height=370, width=300, relief=RAISED)
f1.pack()

dosa = StringVar()
Cookies = StringVar()
Tea = StringVar()
Coffee = StringVar()
Juice = StringVar()
Pancakes = StringVar()
Milk = StringVar()
Total_bill = StringVar()

lb1_dosa = Label(f1, font=("aria", 20, 'bold'), text="Dosa", width=12, fg="blue")
lb1_Cookies = Label(f1, font=("aria", 20, 'bold'), text="Cookies", width=12, fg="blue")
lb1_Tea = Label(f1, font=("aria", 20, 'bold'), text="Tea", width=12, fg="blue")
lb1_Coffee = Label(f1, font=("aria", 20, 'bold'), text="Coffee", width=12, fg="blue")
lb1_Juice = Label(f1, font=("aria", 20, 'bold'), text="Juice", width=12, fg="blue")
lb1_Pancakes = Label(f1, font=("aria", 20, 'bold'), text="Pancakes", width=12, fg="blue")
lb1_Milk = Label(f1, font=("aria", 20, 'bold'), text="Milk", width=12, fg="blue")

lb1_dosa.grid(row=1, column=0)
lb1_Cookies.grid(row=2, column=0)
lb1_Tea.grid(row=3, column=0)
lb1_Coffee.grid(row=4, column=0)
lb1_Juice.grid(row=5, column=0)
lb1_Pancakes.grid(row=6, column=0)
lb1_Milk.grid(row=7, column=0)

entry_dosa = Entry(f1, font=("aria", 20, 'bold'), textvariable=dosa, bd=6, width=8, bg="lightpink")
entry_Cookies = Entry(f1, font=("aria", 20, 'bold'), textvariable=Cookies, bd=6, width=8, bg="lightpink")
entry_Tea = Entry(f1, font=("aria", 20, 'bold'), textvariable=Tea, bd=6, width=8, bg="lightpink")
entry_Coffee = Entry(f1, font=("aria", 20, 'bold'), textvariable=Coffee, bd=6, width=8, bg="lightpink")
entry_Juice = Entry(f1, font=("aria", 20, 'bold'), textvariable=Juice, bd=6, width=8, bg="lightpink")
entry_Pancakes = Entry(f1, font=("aria", 20, 'bold'), textvariable=Pancakes, bd=6, width=8, bg="lightpink")
entry_Milk = Entry(f1, font=("aria", 20, 'bold'), textvariable=Milk, bd=6, width=8, bg="lightpink")

entry_dosa.grid(row=1, column=1)
entry_Cookies.grid(row=2, column=1)
entry_Tea.grid(row=3, column=1)
entry_Coffee.grid(row=4, column=1)
entry_Juice.grid(row=5, column=1)
entry_Pancakes.grid(row=6, column=1)
entry_Milk.grid(row=7, column=1)

btn_reset = Button(f1, bd=5, fg="black", bg="lightblue", font=("ariel", 16, "bold"), width=10, text="Reset", command=Reset)
btn_reset.grid(row=8, column=0)

btn_total = Button(f1, bd=5, fg="black", bg="lightblue", font=("ariel", 16, "bold"), width=10, text="Total", command=Total)
btn_total.grid(row=8, column=1)

root.mainloop()