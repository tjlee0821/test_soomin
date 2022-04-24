import numpy as np 
import cv2
import playsound
from tkinter import *
import tkinter as tk
import tkinter.ttk
import tkinter.font
import os

#p = vlc.MediaPlayer("./dementia_test/Bear.mp3")
#p.play()

#print(cv2.__version__)

WIDTH = 1280
HEIGHT = 720

def draw():
    img = questionBox
    img = infoBox
    
    for box in answerBox:
        img = box    
    cv2.imshow('dementia test',img)
    
    playsound.playsound("./dementia_test/Bear.mp3")
     
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def btnpress():                   # 함수 btnpress() 정의
    a = []
    if chkvar.get() == 1:         # 체크박스가 체크 되었는지 확인
        a.append("English")
    if chkvar1.get() == 1:
        a.append("Mammals")
    if chkvar1.get() == 0:
        a.append("Reptiles")
    if chkvar2.get() == 1:
        a.append("Text Only")
    if chkvar2.get() == 0:
        a.append("Text with Sound")
    a.append("Selected")
    lb.config(text=a)
    
def btnpress1():                   # 함수 btnpress() 정의
    b = []
    if chkvar.get() == 0:         # 체크박스가 체크 되었는지 확인
        b.append("Only English Version Support\nSorry")
        lb1.config(text=b)
        
        
               
        
def game_over():
    print('def game_over')
    
def correct_answer():
    print('def correct_answer')
    
def on_mouse_down():
    print('def on_mouse_down')
    
def update_time_left():
    print('def update_time_left')
    

##########function##############################
##################################################


##################################################
##################################################
#############################################
##########color##############################
blue_color = (255, 0, 0)
green_color = (0, 255, 0)
red_color = (0, 0, 255)
white_color = (255, 255, 255)
dimgrey = (105,105,105)
##########color##############################
#############################################

#############################################
##########Variables##############################

CheckVar1=0
CheckVar2=0

mammals = ['Bat', 'Bear', 'Beaver', 'Cat', 'Cow', 'Coyote', 'Deer', 'Dog', 'Dolphin', 'Elephant', 'Fox', 'Gibbon', 'Giraffe', 'Goat', 'Goat', 'Gopher', 'Hedgehog', 'Hippopotamus', 'Horse', 'Horse', 'Jaguar', 'Kangaroo', 'Koala', 'Leopard', 'Lion', 'Llama', 'Lynx', 'Mole', 'Monkey', 'Mouse', 'Narwhal', 'Orangutan', 'Orca', 'Otter', 'Ox', 'Panda', 'Pig', 'Polar bear', 'Puma', 'Rabbit', 'Raccoon', 'Rat', 'Rhinoceros', 'Sheep', 'Squirrel', 'Tiger', 'Walrus', 'Weasel', 'Wolf', 'Zebra']

score = 0 
time_Elapse = 0
##########Variables##############################
#############################################

##################################################
##########function##############################
img = cv2.imread('/Users/Taeryong/Projects/soomin_test/Main.png')# 1280 x 1024 white background image read
answerBox1 = cv2.rectangle(img, (100, 350), (500, 500), blue_color, -1)# -1 로 채운다 (양수를 쓰면 선의 두께)
answerBox2 = cv2.rectangle(img, (700, 350), (1100, 500), green_color, -1)
answerBox3 = cv2.rectangle(img, (100, 600), (500, 750), red_color, -1)
answerBox4 = cv2.rectangle(img, (700, 600), (1100, 750), red_color, -1)
answerBox = [ answerBox1, answerBox2, answerBox3, answerBox4 ]
questionBox = cv2.rectangle(img, (350, 100), (1100, 250), dimgrey, -1)
infoBox  = cv2.rectangle(img, (100, 100), (300, 250), dimgrey, -1)


##################################################
##################################################

root = Tk()                      # root라는 창을 생성
root.geometry("600x400")       # 창 크기설정
root.title("dementia_test")    # 창 제목설정
root.option_add("*Font","sans-serif 25") # 폰트설정
root.resizable(False, False) 
    
chkvar = IntVar()                             # chkvar에 int 형으로 값을 저장
chkbox = Checkbutton(root, variable=chkvar)   # root라는 창에 체크박스 생성
chkbox.config(text="English")                  # 체크박스 내용 설정
chkbox.pack()                                 # 체크박스 배치

chkvar1 = IntVar()                            # chkvar1에 int 형으로 값을 저장
chkbox1 = Checkbutton(root, variable=chkvar1) # root라는 창에 체크박스 생성
chkbox1.config(text="Mammals")                      # 체크박스 내용 설정
chkbox1.pack()                                # 체크박스 배치

chkvar2 = IntVar()                            # chkvar2 에 int 형으로 값을 저장
chkbox2 = Checkbutton(root, variable=chkvar2) # root라는 창에 체크박스 생성
chkbox2.config(text="Text Only")                   # 체크박스 내용 설정
chkbox2.pack()                                # 체크박스 배치
    
btn = Button(root)                # root라는 창에 버튼 생성
btn.config(text= "Select")          # 버튼 내용 
btn.config(width=10)              # 버튼 크기
btn.config(command=btnpress)      # 버튼 기능 (btnpree() 함수 호출)
btn.pack()                        # 버튼 배치

lb = Label(root)                 # root라는 창에 레이블 생성
lb.pack()       # 레이블 배치

btn1 = Button(root)                # root라는 창에 버튼 생성
btn1.config(text= "Run Dementia Test")          # 버튼 내용 
btn1.config(width=20)              # 버튼 크기
btn1.config(command=btnpress1)      # 버튼 기능 (btnpree() 함수 호출)
btn1.pack()                        # 버튼 배치

lb1 = Label(root)                 # root라는 창에 레이블 생성
lb1.pack() 

root.mainloop()   


