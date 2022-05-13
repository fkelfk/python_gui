from tkinter import *

root = Tk()
root.title("Mido GUI") #프로그램이름
root.geometry("640x480") #가로 x 세로 

listbox = Listbox(root, selectmode="extended", height=0) #selectmode="single" height = 0 리스트를 다 보여준다 만약 3이라면 3개만
listbox.insert(0, "apple")
listbox.insert(1, "strawberry")
listbox.insert(2, "banana")
listbox.insert(END, "watermelon")
listbox.insert(END, "grape")
listbox.pack()

def btncmd():
    # listbox.delete(END) #맨 뒤 항목을 삭제
    # listbox.delete(0) #맨 앞 항목을 삭제
    # print(listbox.size(), "in the list") #갯수 확인
    # print("list 1 to 3 : ", listbox.get(0, 2)) #항목 확인
    print("selected list:", listbox.curselection()) # 선택된 항목 확인
 

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()