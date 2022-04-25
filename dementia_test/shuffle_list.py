import random
import tkinter as tk
from tkinter import *
import time 
import threading

global changer
changer = False
screenSize = "1280x1024"


target_list = []

reptiles = ['adder', 'alligator', 'anaconda', 'angonoka', 'anole', 'asp', 'basilisk', 'black caiman', 'black racer', 'boaconstrictor', 'box turtle', 'bull snake', 'caiman', 'cobra', 'collared lizard', 'copperhead', 'cottonmouth', 'crocodile', 'desert tortoise', 'frilled lizard', 'gaboon viper', 'garter snake', 'gavial', 'gecko', 'gila monster', 'glass lizard', 'gopher snake', 'green iguana', 'ground skink', 'horned lizard', 'iguana', 'indigo snake']

mammals = ['Bat', 'Bear', 'Beaver', 'Cat', 'Cow', 'Coyote', 'Deer', 'Dog', 'Dolphin', 'Elephant', 'Fox', 'Gibbon', 'Giraffe', 'Goat', 'Goat', 'Gopher', 'Hedgehog', 'Hippopotamus', 'Horse', 'Horse', 'Jaguar', 'Kangaroo', 'Koala', 'Leopard', 'Lion', 'Llama', 'Lynx', 'Mole', 'Monkey', 'Mouse', 'Narwhal', 'Orangutan', 'Orca', 'Otter', 'Ox', 'Panda', 'Pig', 'Polar bear', 'Puma', 'Rabbit', 'Raccoon', 'Rat', 'Rhinoceros', 'Sheep', 'Squirrel', 'Tiger', 'Walrus', 'Weasel', 'Wolf', 'Zebra']

colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple']

list_length_mammals = len(mammals)
list_length_reptiles = len(reptiles)

questionLength = 5
MaxQuestionLength = min(list_length_mammals, list_length_reptiles)


def setTargetList(str):
    if str == True: 
        target_list.extend(mammals)
    if str == False: 
        target_list.extend(reptiles)    
    
    list_length = len(target_list)
    list_length_colors = len(colors)

def BuildQuestionAndAnswerList(itx):
    rRightList = random.sample(target_list,itx)
    for i in range(0,itx): # to make enough color element for target_list 이게 없으면 애러난다. itx 가 컬러 수보다 커지기 때문이다.
        colors.extend(colors)
        
    rRightColors = random.sample(colors,itx)
    rRightLogic = []
    for i in range(0,itx):#수만큼 true 를 넣어준다.
        rRightLogic.append(True)

    rWrongList = random.sample(target_list,1)
    rWrongColors = random.sample(colors,1)
    rWrongLogic = [False]

    right_List = list(zip(rRightList,rRightColors,rRightLogic))
    wrong_List = list(zip(rWrongList,rWrongColors,rWrongLogic))

    answer_List = random.sample(right_List,3)
    answer_List.append(wrong_List)
    random.shuffle(answer_List)
    
    return right_List, answer_List

def ShowQuestionAndAnswer(itx): #잘 만들어졌는지 확인해본다
    (right_List,answer_List) = BuildQuestionAndAnswerList(itx)
    
    print("Question :",right_List)
    print("Answer :",answer_List)
    

###=============================###

def ChangeSpecies():
    if chkvar1.get() == 1:
        label.config(bg="gray")
        setTargetList(True)
    if chkvar1.get() == 0:
        label.config(bg="white")
        setTargetList(False)

###============================###
def print_Question(qests):
    #qLb.config(text=qests)
    print(qests)
    threading.Timer(2.5, print_Question).start()

###============================###
def showQuestion(itx):
    (right_List,answer_List) = BuildQuestionAndAnswerList(itx)
    for sName, sColor, sLogic in right_List:
        print_Question(sName)   
#    for sName, sColor, sLogic in right_List:
#        qLb.config(text=sName)
#        qLb.config(gb=sColor)
        

###============================###
def testStart():   
    ChangeSpecies()
    print(target_list)
    print("Start")
    showQuestion(6)# 버튼 배치
    


###============================###

root = tk.Tk()
root.title("dementia_test")   
root.wm_geometry(screenSize)

label = Label(root)
label.config(bg="white")
label.config(pady=5)
label.config(font=(None, 1))
label.config(height=20)
label.config(width=720)

chkvar1 = IntVar()
checkbox = Checkbutton(root)
checkbox.config(bg="white")
checkbox.config(text="Mammals")
checkbox.config(command=ChangeSpecies)
checkbox.config(variable=chkvar1)
checkbox.pack()
label.pack()

btn = Button(root)                
btn.config(text= "Start Dementia Test")           
btn.config(width=20)              
btn.config(command=testStart)      
btn.pack()            

qLb = Label(root)
qLb.pack()            

root.mainloop()
    




