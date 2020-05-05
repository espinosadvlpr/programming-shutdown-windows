import sys
import os
import tkinter
import time

time1 = ''

def reloj():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.configure(text=time2)
    clock.after(500, reloj)


def shutdown_10():
    os.system('shutdown /s /t 600')
    #sleep_time("10 minutos")


def shutdown_15():
    os.system('shutdown /s /t 900')
    #sleep_time("15 minutos")


def shutdown_20():
    os.system('shutdown /s /t 1200')
    #sleep_time("20 minutos")


def shutdown_30():
    os.system('shutdown /s /t 1800')
    #sleep_time("30 minutos")


def shutdown_40():
    os.system('shutdown /s /t 2400')
    #sleep_time("40 minutos")


def shutdown_50():
    os.system('shutdown /s /t 3000')
    #sleep_time("50 minutos")


def shutdown_hour():
    os.system('shutdown /s /t 3600')
    #sleep_time("1 hora")


def shutdown_2():
    os.system('shutdown /s /t 7200')
    #sleep_time("2 horas")


def shutdown_3():
    os.system('shutdown /s /t 10800')
    #sleep_time("3 horas")


def shutdown_now():
    os.system('shutdown /s')


def shutdown_cancel():
    os.system('shutdown /a')


root = tkinter.Tk()
root.title("Sleep")
frame_left = tkinter.Frame()
frame_center = tkinter.Frame()
frame_right = tkinter.Frame()

clock = tkinter.Label(root, font=('Consolas', 40), fg="black")
clock.pack()

tkinter.Label(root, font=('Consolas', 14),text="Apagado: ").pack(side='top')
tkinter.Label(root, text=" ").pack()

tkinter.Button(frame_left, text="10 Minutos",
               command=shutdown_10).pack(fill=tkinter.BOTH)
tkinter.Button(frame_center, text="15 Minutos",
               command=shutdown_15).pack(fill=tkinter.BOTH)
tkinter.Button(frame_right, text="20 Minutos",
               command=shutdown_20).pack(fill=tkinter.BOTH)
tkinter.Button(frame_left, text="30 Minutos",
               command=shutdown_30).pack(fill=tkinter.BOTH)
tkinter.Button(frame_center, text="40 Minutos",
               command=shutdown_40).pack(fill=tkinter.BOTH)
tkinter.Button(frame_right, text="50 Minutos",
               command=shutdown_15).pack(fill=tkinter.BOTH)
tkinter.Button(frame_left, text="1 Hora",
               command=shutdown_hour).pack(fill=tkinter.BOTH)
tkinter.Button(frame_center, text="2 Horas",
               command=shutdown_2).pack(fill=tkinter.BOTH)
tkinter.Button(frame_right, text="3 Horas",
               command=shutdown_3).pack(fill=tkinter.BOTH)
tkinter.Button(frame_left, text="Apagar ahora",
               command=shutdown_now).pack(fill=tkinter.BOTH)
tkinter.Button(
    frame_center, text="Cancelar apagado", command=shutdown_cancel).pack(fill=tkinter.BOTH)
tkinter.Button(frame_right, text="Salir",
               command=root.quit).pack(fill=tkinter.BOTH)

frame_left.pack(side='left', fill='y', expand='1')
frame_right.pack(side='right', fill='y', expand='1')
frame_center.pack(side='right', fill='y', expand='1')

reloj()
root.mainloop()