import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Mido GUI") #프로그램이름
root.geometry("640x480") #가로 x 세로 

# 기차 예매 시스템

def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")

def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")

def error():
    msgbox.showerror("에러", "잘못된 접근입니다.")

def okcancel():
    msgbox.askokcancel("확인 / 취소", "예매하시겟습니까?")

def retrycancel():
    msgbox.askretrycancel("재시도 / 취소", "재시도하시겠습니까?")

def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="저장되지 않았습니다. \n 저장 후 종료하시겠습니까?")    
    # 네 : 저장 후 종료
    # 아니오 : 저장 하지 않고 종료
    # 취소 : 프로그램 종료 취소 (현재 화면에서 계속 작업)
    print("응답:", response)  # True, False, None -> 예 1, 아니오 0, 그 외
    if response == 1: #네, ok
        print("예")
    elif response == 0: # 아니오
        print("아니오")
    else:
        print("취소")     

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()
Button(root, command=okcancel, text="확인 / 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()

root.mainloop()