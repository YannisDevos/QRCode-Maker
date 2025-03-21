from tkinter import *
from utils.generator import *
from tkinter import colorchooser
from tkinter.messagebox import *
from random import randint

BC = "white"
FC = "black"

def chooseBackColor():
    global BC
    backColor = colorchooser.askcolor(title="QoloR")
    
    strcolor = str(backColor)
    
    nvcolor = getColor(strcolor)
    
    backLabel.config(text="     ", background=nvcolor)
    BC = nvcolor


def chooseFillColor():
    global FC
    fillColor = colorchooser.askcolor(title="QoloR")
    
    strcolor = str(fillColor)
    
    nvcolor = getColor(strcolor)
    
    fillLabel.config(text="     ", background=nvcolor)
    
    FC = nvcolor


def isOnlyNumber(s):
    numberTab = ["0","1","2","3","4","5","6","7","8","9"]
    for e in s:
        if(e not in numberTab):
            return False
    
    return True
    

def sizesAreValid(s1,s2):
    
    if(s1 == "" or s2 == ""):
        return False
    
    if(not isOnlyNumber(s1) or not isOnlyNumber(s2)):
        return False      
    
    
    s1 = int(s1)
    s2 = int(s2)
    
    if(s1 <= 100 and s2 <= 100):
        return True
    else:
        return False


def goQR():
    url = urlInput.get()
    box = spin1.get()
    border = spin2.get()
    filename = filenameInput.get()
    
    radButton = var.get()
    radButtonTxt = ""
    
    if(sizesAreValid(box,border)):
        if(url == ""):
            showwarning("Warning !","You have to enter a valid URL !")
        elif(filename == ""):
            showwarning("Warning !","You have to enter a valid file name !")
        elif(radButton == 0):
            showwarning("Warning !", "You have to choose an extension for your file !")
        else:
            if(radButton == 1):
                radButtonTxt = ".png"
            else:
                radButtonTxt = ".jpg"
                
            createQrCode(url,box,border,BC,FC,filename,radButtonTxt)
            showinfo("Results","Your QR Code is ready !")
    else:
        showwarning("Warning !", "Invalid sizes !")
        
    


def printQR():
    url = urlInput.get()
    box = spin1.get()
    border = spin2.get()
    
    if(sizesAreValid(box,border)):
        if(url == ""):
            showwarning("Warning !","You have to enter a valid URL !")
        else:
            showQR(url,box,border,BC,FC)
    else:
        showwarning("Warning !", "Invalid sizes !")
    
        
    
def resetColor():
    global BC,FC
    BC = "white"
    FC = "black"
    backLabel.config(background="white")
    fillLabel.config(background="black")

    
def getRandomColor(): 
    s = "#"
    hexaLetter = ['a','b','c','d','e','f']
    
    for i in range(6):
        if(randint(0,10) > 5):
            s = s + str(randint(0,9))
        else:
            s = s + hexaLetter[randint(0,len(hexaLetter) - 1)]
            
    return s
        

def chooseRandomColor():
    global BC,FC
    BC = getRandomColor()
    FC = getRandomColor()
    
    backLabel.config(background=BC)
    fillLabel.config(background=FC)
    



window = Tk()
window.geometry("450x600")
window.resizable(width=False, height=False)
# window.iconbitmap("logo.ico") // To show Maqr logo at the app corner and taskbar (not working on .exe)
window.title("Maqr")

blank = Label(window, text="")
blank.pack()

label = Label(window, text="MaQr", font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif",25))
label.pack()

blank = Label(window, text="")
blank.pack()

# --------------------------

frame1 = Frame(window)
frame1.pack()

urlInput = Entry(frame1, width=50)
urlInput.pack(side=RIGHT)

urlLabel = Label(frame1, text="URL : ")
urlLabel.pack(side=LEFT)

blank = Label(window, text="")
blank.pack()

# --------------------------

frame2 = Frame(window)
frame2.pack()

scale1Label = Label(frame2, text="     Box size : ")
scale1Label.pack(side=LEFT)

def1 = DoubleVar(value=20)
spin1 = Spinbox(frame2,from_=0, to=100, textvariable=def1)
spin1.pack(side=RIGHT)

blank = Label(window, text="")
blank.pack()

# --------------------------

frame3 = Frame(window)
frame3.pack()

scale2Label = Label(frame3, text="Border size : ")
scale2Label.pack(side=LEFT)

def2 = DoubleVar(value=2)
spin2 = Spinbox(frame3,from_=0, to=100, textvariable=def2)
spin2.pack(side=RIGHT)

# --------------------------

blank = Label(window, text="")
blank.pack()

blank = Label(window, text="")
blank.pack()

# --------------------------

colorFrame = LabelFrame(window, text="Colors", padx=50, pady=20)
colorFrame.pack()

frame4 = Frame(colorFrame)
frame4.pack()

backColorPick = Button(frame4, text="BackGround Color", command=chooseBackColor, width=20)
backColorPick.pack(side=LEFT)

blank = Label(frame4, text="")
blank.pack(side=LEFT)

backLabel = Label(frame4,text="     ", background=BC)
backLabel.pack(side=RIGHT)

# --------------------------

blank = Label(colorFrame, text="")
blank.pack()

# --------------------------

frame5 = Frame(colorFrame)
frame5.pack()

fillColorPick = Button(frame5, text="QR Color", command=chooseFillColor, width=20)
fillColorPick.pack(side=LEFT)

blank = Label(frame5, text="")
blank.pack(side=LEFT)

fillLabel = Label(frame5,text="     ", background=FC)
fillLabel.pack(side=RIGHT)

# --------------------------

blank = Label(colorFrame, text="")
blank.pack()

blank = Label(colorFrame, text="")
blank.pack()

# --------------------------

colorButtonFrame = Frame(colorFrame)
colorButtonFrame.pack() 

resetColorButton = Button(colorButtonFrame,text="Reset", command=resetColor, background="lightgrey", width=10)
resetColorButton.pack(side=LEFT)

blank = Label(colorButtonFrame, text="")
blank.pack(side=LEFT)

randomColorButton = Button(colorButtonFrame,text="Random", command=chooseRandomColor, background="lightgrey", width=10)
randomColorButton.pack(side=RIGHT)

# --------------------------

blank = Label(window, text="")
blank.pack()

# --------------------------

frame6 = Frame(window)
frame6.pack()

filenameInput = Entry(frame6)
filenameInput.pack(side=RIGHT)

filenameLabel = Label(frame6, text="Filename : ")
filenameLabel.pack(side=LEFT)

# --------------------------

blank = Label(window, text="")
blank.pack()

# --------------------------

frame7 = Frame(window)
frame7.pack()

var = IntVar()
rb1 = Radiobutton(frame7, text= "PNG", variable=var,value=1)
rb2 = Radiobutton(frame7, text="JPG", variable=var,value=2)
rb1.pack(side=LEFT)
rb2.pack(side=RIGHT)

# --------------------------

blank = Label(window, text="")
blank.pack()

# --------------------------

frame8 = Frame(window)
frame8.pack()

showButton = Button(frame8, text="Show QRCode",width=15, height=2, command=printQR)
showButton.pack(side=LEFT)

blank = Label(frame8, text="")
blank.pack(side=LEFT)

finalButton = Button(frame8, text="Generate", width=40, height=2, background='lightgreen', command=goQR)
finalButton.pack(side=RIGHT)

window.mainloop()
