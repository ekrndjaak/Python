from tkinter import * #tkinter안에있는 모든 모듈을 한번에 불러오기
root = Tk()

root.title("prgraming") #창의 이름을 정의
root.geometry("400x200") #창의 사이즈 정의

#btn = Button(root, text = "Button") #버튼 지정
#btn.pack() # 이 코드가 있어야 실행이 가능하다.

def btcommand():
    print("Clicked")

btn = Button(root, text = "Button", padx = 10, pady = 10, fg = "blue", command = btcommand)
btn.pack()

root.mainloop() #끄기전에 계속해서 실행되어야 하기위한 코드