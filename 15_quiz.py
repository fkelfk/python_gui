from tkinter import *

root = Tk()
root.title("제목 없음 - 메모장")
root.geometry("640x480")

menu = Menu(root)

def create_new_file():
    print("새 파일을 만듭니다.")

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)


# txt = Text(root)
# txt.pack(fill=BOTH, expand=Y) #텍스트화면을 좌우로 늘리고, 위아래로 확장


root.mainloop()