from tkinter import *

root = Tk()
root.title("Mido GUI") #프로그램이름
root.geometry("640x480") #가로 x 세로 

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력해요")

def btncmd():
    #내용출력
    print(txt.get("1.0", END)) #1.0은 라인 1, column기준 0에서부터 END까지 가져와라
    print(e.get()) #엔트리 값 가져오기

    #내용삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()