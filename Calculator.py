
from tkinter import *

import math


root=Tk()
root.configure(bg="white")
root.geometry("200x349")
root.title("Calculator")
frame=Frame(root,bg="white")
frame.grid(row=2,column=0)


equation=StringVar()
equation.set('0')
expression=''
place=''
placeall=''
total=''

def press(value):
    global expression
    if value=="*" or value=="+" or value=="-" or value=="+":
        ()
    elif expression==total:
        expression=''

    expression+=str(value)
    equation.set(expression)

def clear():
    global expression
    expression=''
    equation.set(0)

def equal():
    global expression
    global total
    expression = expression.replace("%", '/100')
    total=str(eval(expression))
    equation.set(total)
    expression=total

def makenegative():
    global expression
    expression=str(eval(expression)*-1)
    equation.set(expression)

def dividex():
    global expression
    expression=str(1/eval(expression))
    equation.set(expression)

def squarex():
    global expression
    expression=str(pow(eval(expression),2))
    equation.set(expression)

def rootx():
    global expression
    expression=str(math.sqrt(eval(expression)))
    equation.set(expression)

def backspace():
    global expression
    expression=expression[:-1]
    if expression=="":
        equation.set(0)
    else:
        equation.set(expression)

def ms():
    global place
    global expression
    global total
    place=''
    global placeall

    place += str(expression)
    placeall += str(expression) + " "


def mr():
    global place
    equation.set(place)

def mall():
    global placeall
    equation.set(placeall)

def mc():
    global place
    global placeall
    place=''
    placeall=''


def mplus():
    global place
    global expression
    global placeall

    place+=("+"+str(expression))
    place=str(eval(place))
    if isinstance(placeall,list):
        placeall.pop(-1)
        placeall.append(place)
    else:
        placeall = placeall.split()
        placeall[-1] = place


def mminus():
    global place
    global expression
    global placeall

    place+=("-"+str(expression))
    place=str(eval(place))
    if isinstance(placeall, list):
        placeall.pop(-1)
        placeall.append(place)
    else:
        placeall = placeall.split()
        placeall[-1] = place

def ce():
    global expression
    expression=expression[0:2]
    equation.set(expression)



field=Entry(textvariable=equation,justify='right',width=30,relief='sunken')
field.grid(row=0,column=0,columnspan=4,ipadx=7,ipady=10)
frame1=Frame()
frame1.grid(row=1,column=0,columnspan=4)


buttonC = Button(frame, text=" C ", relief="ridge",highlightcolor="#A2A2A2",font="Arial 10", height=2, width=5, command=clear).grid(row=3, column=3)
button0 = Button(frame, text=" 0 ", relief="ridge",bg="#FFFFFF",font="Arial 10", height=2, width=5, command=lambda : press("0")).grid(row=8, column=2)
button1 = Button(frame, text=" 1 ", relief="ridge",bg="#FFFFFF",highlightcolor="#FFFFFF",font="Arial 10", height=2, width=5, command=lambda : press("1")).grid(row=7, column=1)
button2 = Button(frame, text=" 2 ", relief="ridge",bg="#FFFFFF",font="Arial 10", height=2, width=5, command=lambda : press("2")).grid(row=7, column=2)
button3 = Button(frame, text=" 3 ", relief="ridge",bg="#FFFFFF",font="Arial 10", height=2, width=5, command=lambda : press("3")).grid(row=7, column=3)
button4 = Button(frame, text=" 4 ", relief="ridge",bg="#FFFFFF",font="Arial 10", height=2, width=5, command=lambda : press("4")).grid(row=6, column=1)
button5 = Button(frame, text=" 5 ", relief="ridge",bg="#FFFFFF",font="Arial 10", height=2, width=5, command=lambda : press("5")).grid(row=6, column=2)
button6 = Button(frame, text=" 6 ", relief="ridge",bg="#FFFFFF",font="Arial 10", height=2, width=5, command=lambda : press("6")).grid(row=6, column=3)
button7 = Button(frame, text=" 7 ", relief="ridge",bg="#FFFFFF",font="Arial 10", height=2, width=5, command=lambda : press("7")).grid(row=5, column=1)
button8 = Button(frame, text=" 8 ", relief="ridge",bg="#FFFFFF",font="Arial 10", height=2, width=5, command=lambda : press("8")).grid(row=5, column=2)
button9 = Button(frame, text=" 9 ", relief="ridge",bg="#FFFFFF",font="Arial 10", height=2, width=5, command=lambda : press("9")).grid(row=5, column=3)
buttonplusminus = Button(frame, text=" +/- ", relief="ridge",bg="#FFFFFF",font="Arial 10", height=2, width=5, command=makenegative).grid(row=8, column=1)
buttonadd = Button(frame, text=" + ", relief="ridge",highlightcolor="#A2A2A2",font="Arial 10", height=2, width=5, command=lambda : press("+")).grid(row=7, column=4)
buttonsubstract = Button(frame, text=" − ", relief="ridge",highlightcolor="#A2A2A2",font="Arial 10", height=2, width=5, command=lambda : press("-")).grid(row=6, column=4)
buttondivide = Button(frame, text=" ÷ ", relief="ridge",highlightcolor="#A2A2A2",font="Arial 10", height=2, width=5, command=lambda : press("/")).grid(row=4, column=4)
buttonmultiply = Button(frame, text=" × ", relief="ridge",highlightcolor="#A2A2A2",font="Arial 10", height=2, width=5, command=lambda : press("*")).grid(row=5, column=4)
buttonpercent = Button(frame, text=" % ", relief="ridge",highlightcolor="#A2A2A2",font="Arial 10", height=2, width=5, command=lambda : press("%")).grid(row=3, column=1)
buttonequal = Button(frame, text=" = ", relief="ridge",bg="#8DCEFF",font="Arial 10", height=2, width=5, command=equal).grid(row=8, column=4)
buttondot = Button(frame, text=" . ", relief="ridge",bg="#FFFFFF",font="boldFont 10", height=2, width=5, command=lambda : press(".")).grid(row=8, column=3)
button1dvdx = Button(frame, text=" 1/x ", relief="ridge",highlightcolor="#A2A2A2",font="Arial 10", height=2, width=5, command=dividex).grid(row=4, column=1)
buttonx2 = Button(frame, text=" x"+chr(178), relief="ridge",highlightcolor="#A2A2A2",font="Arial 10", height=2, width=5, command=squarex).grid(row=4, column=2)
buttonxroot = Button(frame, text=" √x ", relief="ridge",highlightcolor="#A2A2A2",font="Arial 10", height=2, width=5, command=rootx).grid(row=4, column=3)
buttonbackspace = Button(frame, text=" ⌫ ", relief="ridge",highlightcolor="#A2A2A2",font="Arial 10", height=2, width=5, command=backspace).grid(row=3, column=4)
buttonCE = Button(frame, text="CE", relief="ridge",highlightcolor="#A2A2A2",font="Arial 10", height=2, width=5,command=ce).grid(row=3, column=2)
buttonMC = Button(frame1, text="MC", relief="ridge",highlightcolor="#A2A2A2",font="Arial 8", command=mc).grid(row=2, column=1,ipadx=8,ipady=10)
buttonMR = Button(frame1, text="MR", relief="ridge",highlightcolor="#A2A2A2",font="Arial 8", command=mr).grid(row=2, column=2,ipadx=7,ipady=10)
buttonMPLUS = Button(frame1, text="M+", relief="ridge",highlightcolor="#A2A2A2",font="Arial 8",command=mplus).grid(row=2, column=3,ipadx=6,ipady=10)
buttonMMINUS = Button(frame1, text="M-", relief="ridge",highlightcolor="#A2A2A2",font="Arial 8",command=mminus).grid(row=2, column=4,ipadx=6,ipady=10)
buttonMS = Button(frame1, text="MS", relief="ridge",highlightcolor="#A2A2A2",font="Arial 8", command=ms).grid(row=2, column=5,ipadx=5,ipady=10)
buttonMALL = Button(frame1, text="M", relief="ridge",highlightcolor="#A2A2A2",font="Arial 8",command=mall).grid(row=2, column=6,ipadx=3,ipady=10)


root.mainloop()





