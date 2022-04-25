import random
import tkinter as tk
from tkinter import *

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

def DarkenLabel():
    if chkvar1.get() == 1:
        label.config(bg="gray")
        setTargetList(True)
    if chkvar1.get() == 0:
        label.config(bg="white")
        setTargetList(False)
###============================###

def testStart():   
    DarkenLabel()
    print("Start")                # 버튼 배치
###============================###


root = tk.Tk()
root.title("dementia_test")   
root.wm_geometry(screenSize)

label = Label(root, bg="white", pady=5, font=(None, 1), height=20, width=720)
chkvar1 = IntVar()
checkbox = Checkbutton(root,  command=DarkenLabel, variable=chkvar1)
checkbox.config(bg="white")
checkbox.config(text="Mammals")
#checkbox.grid(row=0, column=0, sticky="w")
#label.grid(row=0, column=0, sticky="ew")
checkbox.pack()
label.pack()

btn = Button(root)                
btn.config(text= "Start Dementia Test")           
btn.config(width=20)              
btn.config(command=testStart)      
btn.pack()                        

root.mainloop()
    




