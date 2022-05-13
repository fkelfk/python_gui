from tkinter.ttk import Combobox
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Mido GUI") #프로그램이름
root.geometry("640x480") #가로 x 세로 

values = [str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") #최초 목록 설정

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_combobox.current(0) #0번쨰 인덱스 값 선택
readonly_combobox.pack()



def btncmd():
    print(combobox.get()) #선택값 표시
    print(readonly_combobox.get())
    

btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()