from tkinter import *

root = Tk()
root.title("Mido GUI") #프로그램이름

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2") #내용에 따라 크기 변함 (여백크기)
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4") #고정크기
btn4.pack()

btn5 = Button(root, fg="red", bg="blue", text="버튼5") #fg 글자색, bg 배경색 MacOs에서는 배경색이 변하지 않는다.
btn5.pack()

photo = PhotoImage(file="/Users/junghoonlee/Documents/python_gui/img.png") #버튼 이미지
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")
    
btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()