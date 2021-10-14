from tkinter import *

ms = Tk()
ms.geometry("1000x500")
ms.title("Restaurant Management System")
ms.resizable(width=False, height=False)

frame1 = Frame(ms, bd=5, bg="white", highlightthickness=7, highlightbackground="black", height=110, width=1000)
frame1.pack(side=TOP)
label = Label(frame1, text="Restaurant Management System", bg="white", font="Calibri 40 bold")
label.place(x=100, y=1)
frame2 = Frame(ms, bd=5, bg="white", highlightthickness=7, highlightbackground="black", height=390, width=1000)
frame2.pack()
frame3 = Frame(frame2, bd=5, bg="light blue", highlightthickness=7, highlightbackground="black", height=365, width=240)
frame3.place(x=1, y=1)
frame4 = Frame(frame2, bd=5, bg="light blue", highlightthickness=7, highlightbackground="black", height=365, width=240)
frame4.place(x=240, y=1)
frame5 = Frame(frame2, bd=5, bg="light blue", highlightthickness=7, highlightbackground="black", height=365, width=240)
frame5.place(x=480, y=1)
frame6 = Frame(frame2, bd=5, bg="light blue", highlightthickness=7, highlightbackground="black", height=365, width=250)
frame6.place(x=720, y=1)
v1 = IntVar()
c1 = Checkbutton(frame3, text="Burger:10", variable=v1, onvalue=1, offvalue=0)
c1.place(x=2, y=2)
a1 = IntVar()
e1 = Entry(frame3, bd=4, textvar=a1)
e1.place(x=90, y=2)
v2 = IntVar()
c2 = Checkbutton(frame3, text="Pizza:20", variable=v2, onvalue=1, offvalue=0)
c2.place(x=2, y=28)
a2 = IntVar()
e2 = Entry(frame3, bd=4, textvar=a2)
e2.place(x=90, y=28)
v3 = IntVar()
c3 = Checkbutton(frame3, text="Sandwich:30", variable=v3, onvalue=1, offvalue=0)
c3.place(x=2, y=54)
a3 = IntVar()
e3 = Entry(frame3, bd=4, textvar=a3)
e3.place(x=90, y=54)
v4 = IntVar()
c4 = Checkbutton(frame3, text="Salad:15", variable=v4, onvalue=1, offvalue=0)
c4.place(x=2, y=80)
a4 = IntVar()
e4 = Entry(frame3, bd=4, textvar=a4)
e4.place(x=90, y=80)

v5 = IntVar()
c5 = Checkbutton(frame4, text="Coffee:15", variable=v5)
c5.place(x=2, y=2)
a5 = IntVar()
e5 = Entry(frame4, bd=4, textvar=a5)
e5.place(x=90, y=2)
v6 = IntVar()
c6 = Checkbutton(frame4, text="Tea:20", variable=v6)
c6.place(x=2, y=28)
a6 = IntVar()
e6 = Entry(frame4, bd=4, textvar=a6)
e6.place(x=90, y=28)
v7 = IntVar()
c7 = Checkbutton(frame4, text="Mojita:25", variable=v7)
c7.place(x=2, y=54)
a7 = IntVar()
e7 = Entry(frame4, bd=4, textvar=a7)
e7.place(x=90, y=54)
v8 = IntVar()
c8 = Checkbutton(frame4, text="Shake:40", variable=v8)
c8.place(x=2, y=80)
a8 = IntVar()
e8 = Entry(frame4, bd=4, textvar=a8)
e8.place(x=90, y=80)

l1 = Label(frame5, text="CostofFoods")
l1.place(x=2, y=2)
e9 = Entry(frame5, bd=3)
e9.place(x=90, y=2)
l2 = Label(frame5, text="CostofBeverage")
l2.place(x=2, y=28)
e10 = Entry(frame5, bd=3)
e10.place(x=90, y=28)
l3 = Label(frame5, text="ServiceCharges")
l3.place(x=2, y=54)
e11 = Entry(frame5, bd=3)
e11.place(x=90, y=54)
l4 = Label(frame5, text="TaxPercentage")
l4.place(x=2, y=80)
e12 = Entry(frame5, bd=3)
e12.place(x=90, y=80)
l5 = Label(frame5, text="SubTotal")
l5.place(x=2, y=106)
e13 = Entry(frame5, bd=3)
e13.place(x=90, y=106)
l6 = Label(frame5, text="Total")
l6.place(x=2, y=132)
e14 = Entry(frame5, bd=3)
e14.place(x=90, y=132)
l = Label(frame6, text="Restaurant Receipt", font="Calibri 12 bold")
l.place(x=2, y=2)
f = Frame(frame6, bd=5, bg="white", highlightthickness=7, highlightbackground="black", height=310, width=220)
f.place(x=2, y=30)


def exit():
    ms.destroy()


button1 = Button(frame5, text="Exit", bg="Grey", bd=15, command=exit)


def receipt():
    global recp1
    recp1 = Label(f,
                  text="Burger\nPizza\nSandwich\nSalad\nCoffee\nTea\nMojita\nShake\nCost of Food\nCost of Beverage\nPaid Tax\nService Charge\nTotal Cost",
                  bg="white", font="Calibri 10 bold", justify=LEFT)
    recp1.place(x=2, y=2)
    global recp2
    recp2 = Label(f, text="{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{:.3s}\n{}".format(e1.get(), e2.get(), e3.get(),
                                                                                          e4.get(), e5.get(), e6.get(),
                                                                                          e7.get(), e8.get(), e9.get(),
                                                                                          e10.get(), e12.get(),
                                                                                          e11.get(), e14.get()),
                  bg="white", font="Calibri 10 bold", justify=LEFT)
    recp2.place(x=110, y=2)


button1.place(x=10, y=200)
button2 = Button(frame5, text="Receipt", bg="Grey", bd=15, command=receipt)
button2.place(x=10, y=270)


def total():
    e9.delete(0, END)
    e10.delete(0, END)
    e11.delete(0, END)
    e12.delete(0, END)
    e13.delete(0, END)
    e14.delete(0, END)

    burger = int(e1.get()) * 10 if v1.get() == 1 else 0
    pizza = int(e2.get()) * 20 if v2.get() == 1 else 0
    sandwich = int(e3.get()) * 30 if v3.get() == 1 else 0
    salad = int(e4.get()) * 15 if v4.get() == 1 else 0
    CostofFoods = burger + pizza + sandwich + salad
    e9.insert(END, CostofFoods)
    coffee = int(e5.get()) * 15 if v5.get() == 1 else 0
    tea = int(e6.get()) * 20 if v6.get() == 1 else 0
    mojita = int(e7.get()) * 25 if v7.get() == 1 else 0
    shake = int(e8.get()) * 40 if v8.get() == 1 else 0
    CostofBeverage = coffee + tea + mojita + shake
    e10.insert(END, CostofBeverage)
    servicecharges = (CostofFoods + CostofBeverage) * 0.008
    e11.insert(END, servicecharges)
    Taxpercentage = (CostofFoods + CostofBeverage) * 0.015
    e12.insert(END, Taxpercentage)
    subtotal = CostofFoods + CostofBeverage + servicecharges
    e13.insert(END, subtotal)
    Total = CostofFoods + CostofBeverage + Taxpercentage
    e14.insert(END, Total)


button3 = Button(frame5, text="Total", bg="Grey", bd=15, command=total)
button3.place(x=120, y=200)


def reset():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)
    e10.delete(0, END)
    e11.delete(0, END)
    e12.delete(0, END)
    e13.delete(0, END)
    e14.delete(0, END)
    recp1.destroy()
    recp2.destroy()
    c1.deselect()
    c2.deselect()
    c3.deselect()
    c4.deselect()
    c5.deselect()
    c6.deselect()
    c7.deselect()
    c8.deselect()


button4 = Button(frame5, text="Reset", bg="Grey", bd=15, command=reset)
button4.place(x=120, y=270)

ms.mainloop()
