import random
import string
import tkinter as tk
from tkinter import *
import time 

global changer # 종 바꾸기
changer = False

global trialLeft #Total Trial
trialLeft = 3     

global NextQuestionLength # the least length
NextQuestionLength = 6 


screenSize = "1280x1024"


target_list = []

keys = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]

reptiles = ['adder', 'alligator', 'anaconda', 'angonoka', 'anole', 'asp', 'basilisk', 'black caiman', 'black racer', 'boaconstrictor', 'box turtle', 'bull snake', 'caiman', 'cobra', 'collared lizard', 'copperhead', 'cottonmouth', 'crocodile', 'desert tortoise', 'frilled lizard', 'gaboon viper', 'garter snake', 'gavial', 'gecko', 'gila monster', 'glass lizard', 'gopher snake', 'green iguana', 'ground skink', 'horned lizard', 'iguana', 'indigo snake']

mammals = ['Bat', 'Bear', 'Beaver', 'Cat', 'Cow', 'Coyote', 'Deer', 'Dog', 'Dolphin', 'Elephant', 'Fox', 'Gibbon', 'Giraffe', 'Goat', 'Goat', 'Gopher', 'Hedgehog', 'Hippopotamus', 'Horse', 'Horse', 'Jaguar', 'Kangaroo', 'Koala', 'Leopard', 'Lion', 'Llama', 'Lynx', 'Mole', 'Monkey', 'Mouse', 'Narwhal', 'Orangutan', 'Orca', 'Otter', 'Ox', 'Panda', 'Pig', 'Polar bear', 'Puma', 'Rabbit', 'Raccoon', 'Rat', 'Rhinoceros', 'Sheep', 'Squirrel', 'Tiger', 'Walrus', 'Weasel', 'Wolf', 'Zebra']

colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple','Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple','Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple','Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple','Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple','Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple','Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple','Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple']

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
    print('ITX')
    print(itx)
    rRightList = random.sample(target_list,itx)      
    rRightColors = random.sample(colors,1)
    rRightLogic = []
    for i in range(0,itx):#수만큼 true 를 넣어준다.
        rRightLogic.append(True)
        rRightColors.append(random.sample(colors,1))
        
    rWrongLogic = []
    rWrongList = random.sample(target_list,1)
    rWrongColors = random.sample(colors,1)
    rWrongLogic.append(False)

    right_List = list(zip(rRightList,rRightColors,rRightLogic))
    wrong_List = list(zip(rWrongList,rWrongColors,rWrongLogic))

    answer_List = random.sample(right_List,3)
    answer_List.extend(wrong_List)
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
    
    d = dict()
    d = right_List_dict
    
    ans = dict()
    ans = answer_List_dict
    
    update_question(d,1,itx,ans)  

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
    global NextQuestionLength
    
    target_list.clear()#list reset 
    ChangeSpecies()
    print(target_list)
    print("Start")
    print(NextQuestionLength)
    showQuestionAndAnswer(NextQuestionLength)
    update_status('testing')

def nullCommand():
    print("nullcommand")
    
def beReadyForTest():
    a1Btn.config(text="answer1")
    a2Btn.config(text="answer2")
    a3Btn.config(text="answer3")
    a4Btn.config(text="answer4")
    a1Btn.config(command=nullCommand)
    a2Btn.config(command=nullCommand)
    a3Btn.config(command=nullCommand)
    a4Btn.config(command=nullCommand)    
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
btn.config(width=30)
btn.config(height=2)              
btn.config(command=testStart)  
btn.config(cursor='hand2')
btn.config(font=("Arial",25))    
btn.pack()            
   
## ===================================##
  
status = tk.Label(root, text="ready")
status.pack()

def update_status(doWhat):
    current_status = status["text"]
    if current_status.endswith("..."): current_status = doWhat
    else: current_status += "."
    status.config(text = current_status)
    statud_id=root.after(1000, update_status, doWhat)
# Launch the status message after 1 millisecond (when the window is loaded)
#root.after(1, update_status)

question_Label = tk.Label(root, text="QUESTIONS")
question_Label.pack()
question_Label.config(width="30")
question_Label.config(height="5")
question_Label.config(font=("Arial",50))

## ===================================##

def update_question(Qset, Qnum, itx, ans ):
    (questionName, colors, Logic) = Qset.get(Qnum)
    print(questionName)
    question_Label.config(text = questionName)
    question_Label.config(bg = colors)
    Qnum = Qnum + 1
    id = root.after(1500, update_question, Qset, Qnum, itx, ans)
    if Qnum > itx : 
        root.after_cancel(id)
        question_Label.config(text = 'Click~!')
        question_Label.config(bg = 'white')
        showChoices(ans)

## ===================================##
def resetAll():
    global NextQuestionLength
    NextQuestionLength = 6
    stopToGo.config(text = 'ready')

def goFuther():
    global NextQuestionLength
    NextQuestionLength = NextQuestionLength + 1
    testStart()
    print('new test')
   
def stop_test():
    global NextQuestionLength
    out = 'Stop Stop: ' + str(NextQuestionLength) + ''
    stopToGo.config(text = out) # reset level
    update_status('')
    openNewWindow(NextQuestionLength)
    #print('stopped')
    

def checkWhetherGoOrStop():
    beReadyForTest() # set initialization
    global trialLeft
    if trialLeft > 0: goFuther()
    if trialLeft == 0: stop_test()
    
def decreaseTrialNumber():
    global trialLeft
    trialLeft = trialLeft - 1    
    out = 'Wrong ' + str(trialLeft) + ' Left '
    stopToGo.config(text = out)
    
def wrongAnswer():
    print("wrongAnswer")
    decreaseTrialNumber()
    checkWhetherGoOrStop()
    
def rightAnswer():
    global NextQuestionLength
    stopToGo.config(text = NextQuestionLength)
    checkWhetherGoOrStop()
    

stopToGo = Label(root, text="Please, Click which is NOT displayed")
stopToGo.pack()
stopToGo.config(width="30")
stopToGo.config(height="2")
stopToGo.config(font=("Arial",25))

## ===================================##

## ===================================##
def showChoices(ans):
    print(ans)
    (a1, c1, k1) = ans.get(1)
    (a2, c2, k2) = ans.get(2)
    (a3, c3, k3) = ans.get(3)
    (a4, c4, k4) = ans.get(4)
    
    #mac 에서 버튼이 이상하게 작용한다.        
    a1Btn.config(text=a1)
    a1Btn.config(highlightbackground=c1,bg = c1)
    if k1==True : a1Btn.config(command = wrongAnswer)
    if k1==False : a1Btn.config(command = rightAnswer)
    a2Btn.config(text=a2)
    a2Btn.config(highlightbackground=c2,bg = c2)
    if k2==True : a2Btn.config(command = wrongAnswer)
    if k2==False : a2Btn.config(command = rightAnswer)
    a3Btn.config(text=a3)
    a3Btn.config(highlightbackground=c3,bg = c3)
    if k3==True : a3Btn.config(command = wrongAnswer)
    if k3==False : a3Btn.config(command = rightAnswer)
    a4Btn.config(text=a4)
    a4Btn.config(highlightbackground=c4,bg = c4)    
    if k4==True : a4Btn.config(command = wrongAnswer)
    if k4==False : a4Btn.config(command = rightAnswer)




a1Btn = Button(root, text="answer1")
a1Btn.pack()
a1Btn.config(width="15")
a1Btn.config(height="2")
#a1Btn.config(padx=10,pady=10)
a1Btn.config(font=("Arial",25))
a1Btn.config(cursor='hand2')

a2Btn = Button(root, text="answer2")
a2Btn.pack()
a2Btn.config(width="15")
a2Btn.config(height="2")
a2Btn.config(font=("Arial",25))
a2Btn.config(cursor='hand2')
a3Btn = Button(root, text="answer3")
a3Btn.pack()
a3Btn.config(width="15")
a3Btn.config(height="2")
a3Btn.config(font=("Arial",25))
a3Btn.config(cursor='hand2')
a4Btn = Button(root, text="answer4")
a4Btn.pack()
a4Btn.config(width="15")
a4Btn.config(height="2")
a4Btn.config(font=("Arial",25))
a4Btn.config(cursor='hand2')
## ===================================##




## ===================================##

def openNewWindow(level_str):
    result_popup = Toplevel(root)
    result_popup.title("Result")
    result_popup.geometry("400x400")
    pLable = Label(result_popup)
    pLable.config(text =level_str)
    pLable.pack()
#btn_result = Button(root, text ="Click to open a new window")
#btn_result.config(command = openNewWindow)

## ===================================##

#btn_result.pack()

root.mainloop()
    




