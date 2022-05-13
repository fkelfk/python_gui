import time
from tkinter.ttk import Combobox, Progressbar
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Mido GUI") #프로그램이름
root.geometry("640x480") #가로 x 세로 

# Progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# Progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# Progressbar.start(10) #10ms 마다 움직임
# Progressbar.pack()

# def btncmd():
#     Progressbar.stop()

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01) # 0.01초 대기

        p_var2.set(i) # progress bar 의 값 설정
        progressbar2.update() #ui update
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()