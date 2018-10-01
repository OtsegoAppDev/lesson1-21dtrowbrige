from guizero import App, Text, PushButton
import math
sante=""
Temp=0
TotalValue=0
CurrentOperation=""



def Button1():
    global sante
    sante+="1"
    calcul.value=sante
def Button2():
    global sante
    sante+="2"
    calcul.value=sante
def Button3():
    global sante
    sante+="3"
    calcul.value=sante
def Button4():
    global sante
    sante+="4"
    calcul.value=sante
def Button5():
    global sante
    sante+="5"
    calcul.value=sante
def Button6():
    global sante
    sante+="6"
    calcul.value=sante
def Button7():
    global sante
    sante+="7"
    calcul.value=sante
def Button8():
    global sante
    sante+="8"
    calcul.value=sante
def Button9():
    global sante
    sante+="9"
    calcul.value=sante
def Button0():
    global sante
    sante+="0"
    calcul.value=sante
def ButtonPlus():
    global sante, temp, CurrentOperation
    temp= float(sante)
    CurrentOperation = "+"
    sante = ""
    calcul.value=sante
def ButtonMinus():
    global sante, temp, CurrentOperation
    temp= float(sante)
    CurrentOperation = "-"
    sante = ""
    calcul.value=sante
def ButtonDivide():
    global sante, temp, CurrentOperation
    temp= float(sante)
    CurrentOperation = "/"
    sante = ""
    calcul.value=sante
def ButtonMultiply():
    global sante, temp, CurrentOperation
    temp= float(sante)
    CurrentOperation = "*"
    sante = ""
    calcul.value=sante
def ButtonSQRT():
    global sante, temp, CurrentOperation
    temp= float(sante)
    CurrentOperation = "sqrt"
    sante = ""
    calcul.value=sante
def ButtonSquare():
    global sante, temp, CurrentOperation
    temp= float(sante)
    CurrentOperation = "x^2"
    sante = ""
    calcul.value=sante


def ButtonEqual():
    global temp, CurrentOperation, TotalValue

    
    if CurrentOperation== "-":
        TotalValue = temp - float(calcul.value)
    elif CurrentOperation == "+":
        TotalValue = float(calcul.value) + temp
    elif CurrentOperation == "*":
        TotalValue = float(calcul.value) * temp
    elif CurrentOperation == "/":
        TotalValue = temp / float(calcul.value)
    elif CurrentOperation == "x^2":
        TotalValue =temp**2
    elif CurrentOperation == "sqrt":
        TotalValue = math.sqrt(temp)

    calcul.value = TotalValue
        



def Buttonclean():
    global sante
    sante=""
    calcul.value=sante






    
app= App(title="Calculator", layout="grid")
calcul= Text(app, text= str(sante), grid= [0,0, 4,1])

button1= PushButton(app, command= Button1, text="1", grid=[0,2])
button2= PushButton(app, command= Button2, text="2", grid=[1,2])
button3= PushButton(app, command= Button3, text="3", grid=[2,2])
button4= PushButton(app, command= Button4, text="4", grid=[0,3])
button5= PushButton(app, command= Button5, text="5", grid=[1,3])
button6= PushButton(app, command= Button6, text="6", grid=[2,3])
button7= PushButton(app, command= Button7, text="7", grid=[0,4])
button8= PushButton(app, command= Button8, text="8", grid=[1,4])
button9= PushButton(app, command= Button9, text="9", grid=[2,4])
button0= PushButton(app, command= Button0, text="0", grid=[0,5,3,1])
button0.width=10
buttonPlus = PushButton(app, command= ButtonPlus, text="+", grid=[3,2])
buttonMinus = PushButton(app, command= ButtonMinus, text="-", grid=[3,3])
buttonDivide = PushButton(app, command= ButtonDivide, text="/", grid=[3,4])
buttonMultiply = PushButton(app, command= ButtonMultiply, text="x", grid=[3,5])
buttonsqrt= PushButton(app, command= ButtonSQRT, text="√x", grid=[4,3])
button22= PushButton(app, command= ButtonSquare, text="x^2", grid=[4,4])
button22.width=1
buttonEqual= PushButton(app, command= ButtonEqual, text="=", grid=[4,5])
buttonClean= PushButton(app, command= Buttonclean, text="C", grid=[4,2])





app.display
