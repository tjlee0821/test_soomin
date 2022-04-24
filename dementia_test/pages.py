import tkinter as tk
import cv2, os, random
from tkinter import *
from turtle import *

class Page(tk.Frame): 
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 1")
        label.pack(side="top", fill="both", expand=True)
        imagePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'image')
        imageFile = os.path.join(imagePath,'1.png')
        img = tk.PhotoImage( file = imageFile )
        backgroundImage=tk.Label(self, image=img)
        backgroundImage.image = img
        backgroundImage.pack(side="top", fill="both", expand=True)
        
        global mammals
        mammals = ['Bat', 'Bear', 'Beaver', 'Cat', 'Cow', 'Coyote', 'Deer', 'Dog', 'Dolphin', 'Elephant', 'Fox', 'Gibbon', 'Giraffe', 'Goat', 'Goat', 'Gopher', 'Hedgehog', 'Hippopotamus', 'Horse', 'Horse', 'Jaguar', 'Kangaroo', 'Koala', 'Leopard', 'Lion', 'Llama', 'Lynx', 'Mole', 'Monkey', 'Mouse', 'Narwhal', 'Orangutan', 'Orca', 'Otter', 'Ox', 'Panda', 'Pig', 'Polar bear', 'Puma', 'Rabbit', 'Raccoon', 'Rat', 'Rhinoceros', 'Sheep', 'Squirrel', 'Tiger', 'Walrus', 'Weasel', 'Wolf', 'Zebra']
        global reptiles
        reptiles = ['aa']
        global target_list
        target_list= []
        
        value = "abc"
        
        def testTarget_Language():
            if chkvar == 1: return True
        
        def testTarget_Sounds():
            if chkvar2 == 1: return False
            if chkvar2 == 0: return True
            
        global chkvar
        global chkvar1
        global chkvar2
        chkvar = IntVar()                            
        chkvar1 = IntVar()
        chkvar2 = IntVar()
        
        chkbox = tk.Checkbutton(self, variable=chkvar)
        chkbox.config(text="English")
        chkbox.pack()
        
        chkbox1 = tk.Checkbutton(self, variable=chkvar1)
        chkbox1.config(text="Mammals")
        chkbox1.pack() 
        
        chkbox2 = tk.Checkbutton(self, variable=chkvar2)
        chkbox2.config(text="Text Only")
        chkbox2.pack()  
        
        def btnpress():
            a = []
            target_list = []    
            if chkvar.get() == 1:
                a.append("English")
            if chkvar1.get() == 1:
                a.append("Mammals")
                target_list.extend(random.shuffle(mammals))
            if chkvar1.get() == 0:
                a.append("Reptiles")
                target_list.extend(random.shuffle(reptiles))
            if chkvar2.get() == 1:
                a.append("Text Only")
            if chkvar2.get() == 0:
                a.append("Text with Sound")
            a.append("Selected")
            label.config(text=a)
        
        btn = tk.Button(self)                # root라는 창에 버튼 생성
        btn.config(text= "Select")          # 버튼 내용 
        btn.config(width=20)              # 버튼 크기
        btn.config(command=btnpress)      # 버튼 기능 (btnpree() 함수 호출)
        btn.pack()
       
       

class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        global width
        width = 1280
        global height
        height = 1024 
        #label = tk.Label(self, text="This is page 2")
        #label.pack(side="top", fill="both", expand=True)
        ## color ##
        global blue_color 
        blue_color = (255, 0, 0)
        global green_color
        green_color = (0, 255, 0)
        global red_color
        red_color = (0, 0, 255)
        global white_color
        white_color = (255, 255, 255)
        global dimgrey
        dimgrey = (105,105,105)
        ## mammal list
        
        
        canvas = tk.Canvas(self, width=width, height=height)
        canvas.pack(padx = 0, pady = 0, expand=YES, fill=BOTH) #padding 주고
        
        answerBox1 = canvas.create_rectangle(100,350,500,500, fill='blue')
        answerBox2 = canvas.create_rectangle(700,350,1100,500, fill='green')         
        answerBox3 = canvas.create_rectangle(100,600,500,750, fill='red')
        answerBox4 = canvas.create_rectangle(700,600,1100,750, fill='dimgrey')         
        questionBox = canvas.create_rectangle(350,100,1100,250, fill='dimgrey')
        infoBox = canvas.create_rectangle(100,100,300,250, fill='dimgrey')
        
        print(Page1.value)
             
            
            
        
        

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Settings", command=p1.show)
        b2 = tk.Button(buttonframe, text="Dementia_Test", command=p2.show)
        b3 = tk.Button(buttonframe, text="Analysis", command=p3.show)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    screenSize = str(width)+'x'+str(height) # page 2 global variable width, height
    root.wm_geometry(screenSize)
    root.title("dementia_test")   
    root.mainloop()