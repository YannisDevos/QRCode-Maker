from tkinter import *
from utils.generator import *
from tkinter import colorchooser
from tkinter.messagebox import *
from random import randint
from utils.Saver import *
import webbrowser;
from tkinter.filedialog import askopenfilename

SAVEFILE = "project/utils/csv/save.csv"
BC = "white"
FC = "black"
defaultDatas = qrDatas("default", 20,2, "white", "black")

def chooseBackColor():
    global BC
    backColor = colorchooser.askcolor(title="QoloR")
    
    if(backColor[1] != None):
        backLabel.config(text="     ", background=backColor[1])
        BC = backColor[1]
    
    return


def chooseFillColor():
    global FC
    fillColor = colorchooser.askcolor(title="QoloR")
    
    if(fillColor[1] != None):
        fillLabel.config(text="     ", background=fillColor[1])
        FC = fillColor[1]
    return
    


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
    
    if(sizesAreValid(box,border)):
        if(url == ""):
            showwarning("Warning !","You have to enter a valid URL !")
        else :
            createQrCode(url,box,border,BC,FC)
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
    
    
# MenuBar Functions
    
def openHelp():
    webbrowser.open("https://github.com/YannisDevos/QRCode-Maker")

def changeEntryText(widget, text):
    widget.delete(0, len(widget.get()))
    widget.insert(0, text)
    return

def loadMenu():
    objectdatas = readSavedDatas(SAVEFILE)
    
    datasListToLoad = Toplevel(window)
    
    datasListToLoad.minsize(200,100)
    
    for elt in objectdatas :
        aFrame = Frame(datasListToLoad)
        Label(aFrame, text=elt.url).pack(side=LEFT)
        Label(aFrame, background=elt.bgColor, width=2).pack(side=LEFT)
        Label(aFrame, background=elt.fillColor, width=2).pack(side=LEFT)
        Button(aFrame, text="Load", command=lambda data=elt: loaddata(data)).pack(side=RIGHT)
        aFrame.pack()

def loaddata(datas):
    global BC
    global FC
    
    changeEntryText(urlInput, datas.url)
    
    spin1.config(textvariable=DoubleVar(value=datas.boxSize))
    spin2.config(textvariable=DoubleVar(value=datas.borderSize))
    
    BC = datas.bgColor
    backLabel.config(background=BC)

    FC = datas.fillColor
    fillLabel.config(background=FC)

def resetLoadedDatas():
    loaddata(defaultDatas)




# ----------------FRONTEND----------------

window = Tk()
window.geometry("450x525")
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

urlLabel = Label(frame1, text="URL : ")
urlLabel.pack(side=LEFT)

urlInput = Entry(frame1, width=50)
urlInput.pack(side=RIGHT)


blank = Label(window, text="")
blank.pack()

# --------------------------

frame2 = Frame(window)
frame2.pack()

scale1Label = Label(frame2, text="     Box size : ")
scale1Label.pack(side=LEFT)

def1 = DoubleVar(value=defaultDatas.boxSize)
spin1 = Spinbox(frame2,from_=0, to=100, textvariable=def1)
spin1.pack(side=RIGHT)

blank = Label(window, text="")
blank.pack()

# --------------------------

frame3 = Frame(window)
frame3.pack()

scale2Label = Label(frame3, text="Border size : ")
scale2Label.pack(side=LEFT)

def2 = DoubleVar(value=defaultDatas.borderSize)
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

backLabel = Label(frame4,text="     ", background=defaultDatas.bgColor)
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

fillLabel = Label(frame5,text="     ", background=defaultDatas.fillColor)
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

frame8 = Frame(window)
frame8.pack()

showButton = Button(frame8, text="Show QRCode",width=15, height=2, command=printQR)
showButton.pack(side=LEFT)

blank = Label(frame8, text="")
blank.pack(side=LEFT)

finalButton = Button(frame8, text="Generate", width=40, height=2, background='lightgreen', command=goQR)
finalButton.pack(side=RIGHT)



# -------------MENU-------------
    
menubar = Menu(window)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Load", command=loadMenu)
menu1.add_command(label="Reset", command=resetLoadedDatas)
menu1.add_separator()
menu1.add_command(label="Quit", command=window.quit)
menubar.add_cascade(label="File", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="About", command=openHelp)
menubar.add_cascade(label="Help", menu=menu2)

window.config(menu=menubar)


# -------------END-------------



window.mainloop()
