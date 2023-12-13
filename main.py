from tkinter import *
from tkinter import messagebox

import winsound
from playsound import playsound
import time

root = Tk()
root.title("Timer")
root.geometry("800x700")
root.config(bg="#000")
root.resizable(False, False)

heading = Label(root, text="Timer", font="arial 30 bold", bg="#000", fg="#ea3548")
heading.pack(pady=10)

# clock
Label(root, font=("arial", 15, "bold"), text="current time:", bg="papaya whip").place(x=250, y=80)


def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    current_time.config(text=clock_time)
    current_time.after(1000, clock)


current_time = Label(root, font=("arial", 15, "bold"), text="", fg="#000", bg="#fff")
current_time.place(x=380, y=80)
clock()


# timer
hrs = StringVar()
Entry(root, textvariable=hrs, width=2, font="arial 50", bg="#000", fg="#fff", bd=0).place(x=150, y=155)
hrs.set("00")

min = StringVar()
Entry(root, textvariable=min, width=2, font="arial 50", bg="#000", fg="#fff", bd=0).place(x=350, y=155)
min.set("00")

sec = StringVar()
Entry(root, textvariable=sec, width=2, font="arial 50", bg="#000", fg="#fff", bd=0).place(x=550, y=155)
sec.set("00")

Label(root, text="hours", font="arial 12", bg="#000", fg="#fff").place(x=230, y=200)
Label(root, text="min", font="arial 12", bg="#000", fg="#fff").place(x=430, y=200)
Label(root, text="sec", font="arial 12", bg="#000", fg="#fff").place(x=630, y=200)


def timer():
    times = int(hrs.get()) * 3600 + int(min.get()) * 60 + int(sec.get())
    while times > -1:
        minute, second = (times // 60, times % 60)
        hour = 0
        if minute > 60:
            hour, minute = (minute // 60, minute % 60)
        sec.set(second)
        min.set(minute)
        hrs.set(hour)

        root.update()
        time.sleep(1)

        if (times == 0):
            winsound.Beep(1000, 2000)
            messagebox.showinfo("Temporizator", "Timpul s-a scurs!")
            sec.set("00")
            min.set("00")
            hrs.set("00")

        times -= 1


def coffee():
    hrs.set("00")
    min.set("01")
    sec.set("30")


def pizza():
    hrs.set("00")
    min.set("12")
    sec.set("00")


def gym():
    hrs.set("00")
    min.set("02")
    sec.set("00")


button = Button(root, text="Start", bg="#ea3548", bd=0, fg="#fff", width=20, height=2, font="arial 10 bold", command=timer)
button.pack(padx=5, pady=40, side=BOTTOM)

Image1 = PhotoImage(file="coffee.png")
button1 = Button(root, image=Image1, bg="#000", bd=0, command=coffee)
button1.place(x=100, y=300)

Image2 = PhotoImage(file="pizza.png")
button2 = Button(root, image=Image2, bg="#000", bd=0, command=pizza)
button2.place(x=320, y=300)

Image3 = PhotoImage(file="gym.png")
button3 = Button(root, image=Image3, bg="#000", bd=0, command=gym)
button3.place(x=500, y=300)


root.mainloop()
