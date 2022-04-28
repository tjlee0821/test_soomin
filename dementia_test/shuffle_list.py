####==========================================================#####
#### Coded by Soomin Lee, collaborated with Taeryong Lee======#####
#### By presenting longer words list, user feel difficulties to screen out what is not shown; ======#####
#### The name and color is mixed together  ===================#####
#### If we feels difficulties to screen out Now Showing Words with designated color===========#####
#### it is to be believed that we are found to be close to dementia ==========================#####
#### This simple python app show the diagnostic procedures ===========########
#### We call it 'Dementia Test' ==============================#####

#### Caution
### it is not a proven test at all from any remotely distant aspects
#### Caution

#### =========================================================#####


### IMPORTANT ######################################################

### Collaborator part is indicated as collaborator
### Collaborator part is indicated as Collaborator Help
### Collaborator part is indicated as stackoverflow for reference

### rest of them, AP Student Soomin Lee coded
### IMPORTANT ######################################################



### Code Begin ###
### Code Begin ###
### Code Begin ###
### Code Begin ###
### Code Begin ###
### Code Begin ###


import tkinter as tk
from tkinter import *
import random
import string
import time 

##================ basic variable settings ===================##

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

##================ basic variable settings ===================##


##================ fundamental data from variables ===================##

list_length_mammals = len(mammals)
list_length_reptiles = len(reptiles)

##================ To prevent from crash  ===================##
MaxQuestionLength = min(list_length_mammals, list_length_reptiles)
## it is almost impossible to go beyond this length, we should not forget to figure out beyond this number. 
##================ To prevent from crash  ===================##

##================ Select Show List accordingly to Checkbox Tick  ===================##
def setTargetList(str):
    if str == True: 
        target_list.extend(mammals)
    if str == False: 
        target_list.extend(reptiles)    
    
    list_length = len(target_list)
    list_length_colors = len(colors)
##================ Select Show List accordingly to Checkbox Tick  ===================##

##================ Build Question List and Answer List for that  ===================##
##==It is easy to use Dictionary for the final list ================================##
## This function returns two Dictionary, Question and Answer
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
    rWrongList = random.sample(target_list,1) # Wrong Choice 
    rWrongColors = random.sample(colors,1)
    rWrongLogic.append(False)

    right_List = list(zip(rRightList,rRightColors,rRightLogic))
    wrong_List = list(zip(rWrongList,rWrongColors,rWrongLogic))

    answer_List = random.sample(right_List,3) #Right Choice
    answer_List.extend(wrong_List) # It complete 4 Choices
    random.shuffle(answer_List)# shuffle the Choices
    
    #For easy, build up theses two list into Dictionary with integer Key
    right_List_dict = dict()
    answer_List_dict = dict()
    right_List_dict = dict(zip(keys,right_List))
    answer_List_dict = dict(zip(keys,answer_List))
    
    return right_List_dict, answer_List_dict

##================ Build Question List and Answer List for that  ===================##


##================ Collaborator edited this continuously updating question  ===================##
# parameter summary
## itx : number of words
## d : question Dictionary
## ans: answer Dictionary 
## 1 : Dictionary Key Value Start with integer 1

def showQuestionAndAnswer(itx): 
    
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

##================ Collaborator edited this continuously updating question  ===================##

### Change List Selection Accordingly ===##
def ChangeSpecies():
    if chkvar1.get() == 1:
        label.config(bg="gray")
        checkbox.config(bg='gray', fg='white')
        setTargetList(True)
    if chkvar1.get() == 0:
        label.config(bg="white")
        checkbox.config(bg='white', fg='black')
        setTargetList(False)
### Change List Selection Accordingly ===##


### This is only for debugging ===##
def print_Question(qests,clrs, lgc):
#    qLb.config(text=qests)
#    qLb.config(bg=clrs)
    print(qests)
    print(clrs)
    print(lgc)
### This is only for debugging ===##

        

###====This Function Will Do Most of Procedure ====###
###
### get global variable ( NextQuestionLength is going to grow, if user get the right choice ) 
### target_list().clear : it is supposed to be renewed for every set of question list ###
### in case the checkbox ticked, it retrieve the selected list ###
### showQuestionAndAnswer will build the new dictionary of questions and answers. 
### ### it calls update_question(d,1,itx,ans) to update every 1500 miliseconds the next word
### update_status will show brief status which wouldn't distract user. 

def testStart():   
    global NextQuestionLength
    
    target_list.clear()#list reset 
    ChangeSpecies()
#    print(target_list)
#    print("Start")
#    print(NextQuestionLength)
    showQuestionAndAnswer(NextQuestionLength)
    update_status('testing')
###====This Function Will Do Most of Procedure ====###


### === prevent undesired action when test is idle ===##
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
### === prevent undesired action when test is idle ===##

### === tkinter is good UI tools ===##
### === Program Title is on the way. on the app title bar==##
### === simple UI is the best ====### 
### === Use pack widgets from top to bottom ===## 

root = tk.Tk()
root.title("dementia_test")   
root.wm_geometry(screenSize) # screen size 

### === tkinter is good UI tools ===##

##====================================================##
##==== Change Input by the user who triggers events ==##
##==== this will select one of two different list ====##
##====================================================##

## =============== pack 1 button =======================#
## =============== mammal & default ( reptiles ) button#
chkvar1 = IntVar()
checkbox = Checkbutton(root)
checkbox.config(bg="white")
checkbox.config(text="Mammals")
checkbox.config(command=ChangeSpecies)
checkbox.config(variable=chkvar1)
checkbox.pack()
## =============== mammal & default ( reptiles ) button#

## =============== pack 2 label showing result of clicking the event =====#
## it changes dynamically accordingly to the clicking event ==============#
## ## clicked under mammals, it turns colors, grey =======================#
label = Label(root)
label.config(bg="white")
label.config(pady=5)
label.config(font=(None, 1))
label.config(height=10)
label.config(width=720)
label.pack()

## =============== pack 2 label showing result of clicking the event =====#


##===============================================##
##==== Input from the user who triggers events ==##
##===============================================##

btn = Button(root)                
btn.config(text= "Start Dementia Test")           
btn.config(width=30)
btn.config(height=2)              
btn.config(command=testStart) # click generate testStart function
btn.config(cursor='hand2') #moseover change cursor shape
btn.config(font=("Arial",25))    
btn.pack()            
   
### === This is edited by collaborator ===#### 
### ===================================#######
### === it is not important code. just trying to adopting the main function, update question ====#
### by stackoverflow.com, collaborator found potential code which will do tkinter dynamic label update ==#
### it works.. so let's use the code ###
### by presenting this code and result on the screen, it represent how the main function, update question works ### 
  
status = Label(root, text="ready")
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

## ========================================##
### === This is edited by collaborator ===#### 





## ========== collaborated code ==========##
## =======================================##
## Qset : Dictionary Type Right Question Word List 
## ans : Dictionary Type answer choice 1 ~ 4 
## Qnum : 1 : Qset first Key for Dictionary  
## itx : How many Words ( mammal name, color, true of false ) set in this question set dictionary

def update_question(Qset, Qnum, itx, ans ): # 
    (questionName, colors, Logic) = Qset.get(Qnum) # disect list into three items
    print(questionName) # debug
    question_Label.config(text = questionName) # Showing word only  
    question_Label.config(bg = colors) # Show the background color 
    Qnum = Qnum + 1 # 2nd Key
    id = root.after(100, update_question, Qset, Qnum, itx, ans) # update next words after 1500 miliseconds
    if Qnum > itx : # check whether key number exceeds the many words (itx); it means every words shows ; Showing question is done
        root.after_cancel(id) # no more repeating function execution
        question_Label.config(text = 'Click~!') # sign changed
        question_Label.config(bg = 'white') # 
        showChoices(ans) # Question presenting has done. It is time to show choices. bottom below, there is definition of function showChoices
## =======================================##
## ========== collaborated code ==========##




## ======= housekeeping codes ============##
## ======= housekeeping codes ============##
## ======= housekeeping codes ============##

## ## ==== clicked, reset the number of words for one set of question to 6 == ###
def resetAll():
    global NextQuestionLength
    NextQuestionLength = 6
    stopToGo.config(text = 'ready')
## ## ==== clicked, reset the number of words for one set of question to 6 == ###

## ## ==== correct answer clicked, test start again with new length of words list == ###
def goFuther():
    global NextQuestionLength
    NextQuestionLength = NextQuestionLength + 1
    testStart()
    print('new test')# debug
## ## ==== correct answer clicked, test start again with new length of words list == ###

## ## ==== User CANNOT stop the test, if it stops by code, whole code intergrity is getting more sound == ###
def stop_test():
    global NextQuestionLength
    out = 'Stop Stop: ' + str(NextQuestionLength) + ''
    stopToGo.config(text = out) # reset level
    update_status('') # keep in mind update_status keeps running, it doesn't have any kill ( cancel ) code. It doensn't matter for the integrity
    openNewWindow(NextQuestionLength) # showing result by opening new windows
    print('stopped')# debug
## ## ==== User CANNOT stop the test, if it stops by code, whole code intergrity is getting sounder == ###

## ## ==== for stop_test(), it determines the trial failure and go next or stop  == ###
def checkWhetherGoOrStop():
    beReadyForTest() # set initialization
    global trialLeft
    if trialLeft > 0: goFuther()# trial left ==> more trial
    if trialLeft == 0: stop_test()# trial zero ==> trigger function stop_test
## ## ==== for stop_test(), it determines the trial failure and go next or stop  == ###

## ## ==== for checkWheterGoOrStop, if failed, trial should decrese  == ###    
def decreaseTrialNumber():
    global trialLeft
    trialLeft = trialLeft - 1    
    out = 'Wrong ' + str(trialLeft) + ' Left '
    stopToGo.config(text = out)
## ## ==== for checkWheterGoOrStop, if failed, trial should decrese  == ###

## ## ==== By USER CLICK EVENT, wrong, right answer fire distinct function  == ###
def wrongAnswer():# clicing wrong answer
    print("wrongAnswer")#debug
    decreaseTrialNumber()# check to find the function (above)
    checkWhetherGoOrStop()# check to find the function (above)
    
def rightAnswer():# clicking correct answer
    global NextQuestionLength
    stopToGo.config(text = NextQuestionLength)
    checkWhetherGoOrStop()# check to find the function (above). 
## ## ==== By USER CLICK EVENT, wrong, right answer fire distinct function  == ###    
    
## ======= housekeeping codes ============##
## ======= housekeeping codes ============##
## ======= housekeeping codes ============##


## tkinter, sign pack ================================##
## show the housekeeping result signs ==========##
stopToGo = Label(root, text="Please, Click which is NOT displayed")
stopToGo.pack()
stopToGo.config(width="30")
stopToGo.config(height="2")
stopToGo.config(font=("Arial",25))
## tkinter, sign pack ================================##


## tkinter, Answer Choice pack ================================##
## ## Dynamic Change Label and Color ==========================##
def showChoices(ans):
    print(ans)
    (a1, c1, k1) = ans.get(1)
    (a2, c2, k2) = ans.get(2)
    (a3, c3, k3) = ans.get(3)
    (a4, c4, k4) = ans.get(4)
    #mac acting weird on showing background color, rest of them are working fine #     
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
    #mac acting weird on showing background color, rest of them are working fine #     
## ## Dynamic Change Label and Color ==========================##    



## ## initial answer buttons ==================================##
## ## ## answer button 1 ==================##
a1Btn = Button(root, text="answer1")
a1Btn.pack()
a1Btn.config(width="15")
a1Btn.config(height="2")
a1Btn.config(font=("Arial",25))
## ## ## answer button 1 ==================##
## ## ## answer button 2 ==================##
a1Btn.config(cursor='hand2')
a2Btn = Button(root, text="answer2")
a2Btn.pack()
a2Btn.config(width="15")
a2Btn.config(height="2")
a2Btn.config(font=("Arial",25))
a2Btn.config(cursor='hand2')
## ## ## answer button 2 ==================##
## ## ## answer button 3 ==================##
a3Btn = Button(root, text="answer3")
a3Btn.pack()
a3Btn.config(width="15")
a3Btn.config(height="2")
a3Btn.config(font=("Arial",25))
a3Btn.config(cursor='hand2')
## ## ## answer button 3 ==================##
## ## ## answer button 4 ==================##
a4Btn = Button(root, text="answer4")
a4Btn.pack()
a4Btn.config(width="15")
a4Btn.config(height="2")
a4Btn.config(font=("Arial",25))
a4Btn.config(cursor='hand2')
## ## ## answer button 4 ==================##
## ## initial answer buttons ==================================##

## ===================================##
## tkinter, Answer Choice pack ================================##



## tkinter new window showing results ===========##
## ==============================================##

def openNewWindow(level_str):
    result_popup = Toplevel(root)# above root, showing popup
    result_popup.title("Dementia Test Result")
    result_popup.geometry("400x400")
    #result_popup.config(font=("Arial",25))
    
    # determine the Dementia by Level<- switcher 
    textLines = {
        
        6: 'You are dementia',
        7: 'You may be dementia',
        8: 'You are very close to dementia',
        9: 'You may be very close to dementia',
        10: 'You may not close to dementia',
        11: 'You are not close to dementia',
        12: 'You are not definitely close to dementia',
        13: 'You are far from close to dementia'
    }
            
    result = textLines.get(level_str, 'Your brain function sound and normal')# determine the Dementia by Level 
        
    text_result = 'Your test result is\n'    
    text_result += str(level_str)
    text_result += '\n'+result
    #text_result += '\nSoomin\'s Board supports test result STRONGLY'  
    
    pLable = Label(result_popup) # showing result on label
    pLable.config(text = text_result)
    pLable.pack()# pack
    
    pLable = Button(result_popup) # close window button
    pLable.config(text = 'Close Window')
    pLable.config(command = result_popup.destroy) # close event will close popup window
    pLable.pack()# pack
#btn_result = Button(root, text ="Click to open a new window")
#btn_result.config(command = openNewWindow)

## ==============================================##
## tkinter new window showing results ===========##


## tkinter Spacer ===========##
## ## No Funcational Properties
label_spacer = Label(root)
label_spacer.config(bg="white")
label_spacer.config(pady=5)
label_spacer.config(font=(None, 1))
label_spacer.config(height=10)
label_spacer.config(width=720)
label_spacer.pack()
## tkinter tkinter Spacer ===========##


## tkinter Close Dementia Test ===========##

exit_button = Button(root)
exit_button.config(text = 'Close Dementia Test')
exit_button.config(width=30)
exit_button.config(height=2)            
exit_button.config(cursor='hand2') #moseover change cursor shape
exit_button.config(font=("Arial",25))   
exit_button.config(command = root.destroy)
exit_button.pack()# pack
## tkinter Close Dementia Test ===========##
    
root.mainloop()

### Code End ###
### Code End ###
### Code End ###
### Code End ###
### Code End ###