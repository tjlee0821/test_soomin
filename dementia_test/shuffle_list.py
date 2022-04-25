import random
import tkinter as tk
from tkinter import *
import time 
import threading

global changer
changer = False
screenSize = "1280x1024"


target_list = []

keys = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]

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
    
    right_List_dict = dict()
    answer_List_dict = dict()
    right_List_dict = dict(zip(keys,right_List))
    answer_List_dict = dict(zip(keys,answer_List))
    
    return right_List_dict, answer_List_dict

def showQuestionAndAnswer(itx): #잘 만들어졌는지 확인해본다
    right_List_dict = dict()
    answer_List_dict = dict()
    (right_List_dict,answer_List_dict) = BuildQuestionAndAnswerList(itx)
    
    print("Question :",right_List_dict)
    print("Answer :",answer_List_dict)
    
    qestion_1 = right_List_dict.get(1)
    print(qestion_1)        
    

###=============================###

def ChangeSpecies():
    if chkvar1.get() == 1:
        label.config(bg="gray")
        setTargetList(True)
    if chkvar1.get() == 0:
        label.config(bg="white")
        setTargetList(False)

###============================###

def print_Question(qests,clrs, lgc):
#    qLb.config(text=qests)
#    qLb.config(bg=clrs)
    print(qests)
    print(clrs)
    print(lgc)
    
###============================###

        

###============================###
def testStart():   
    ChangeSpecies()
    print(target_list)
    print("Start")
    showQuestionAndAnswer(6)
    # 버튼 배치
    #root.after(10, update_status)
    
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

#qLb = Label(root)
#qLb.config(height=50)
#qLb.config(width=720)
#qLb.config(bg='blue')
#qLb.pack()            


status = tk.Label(root, text="Working")
status.pack()

def update_status():
    # Get the current message
    current_status = status["text"]
    # If the message is "Working...", start over with "Working"
    if current_status.endswith("..."): current_status = "Working"
    # If not, then just add a "." on the end
    else: current_status += "."
    # Update the message
    status.config(text = current_status)
    # After 1 second, update the status
    root.after(1000, update_status)
# Launch the status message after 1 millisecond (when the window is loaded)
#root.after(1, update_status)


root.mainloop()
    




