import numpy as np 
import cv2
#print(cv2.__version__)

WIDTH = 1280
HEIGHT = 720

def draw():
    img = questionBox
    img = infoBox
    
    for box in answerBox:
        img = box    
    cv2.imshow('dementia test',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
        
        
def game_over():
    print('def game_over')
    
def correct_answer():
    print('def correct_answer')
    
def on_mouse_down(pos):
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


if __name__ == "__main__":
    draw()
    

