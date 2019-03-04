#Asaf Davidov
#Project Assignment 3
from graphics import *

def decoder(words):#decode Function
    totalWord = " "

    for ch in words:
        if ord(ch)>68 and ord(ch)<91:
            dcode1 = ord(ch) - 4
            totalWord = str(totalWord) + str(chr(dcode1))
        elif ord(ch) == 65:
            totalWord = str(totalWord)+ str('W')
        elif ord(ch) == 66:
            totalWord = str(totalWord)+ str('X')
        elif ord(ch) == 67:
            totalWord = str(totalWord)+ str('Y')
        elif ord(ch) == 68:
            totalWord = str(totalWord)+ str('Z')

        if ord(ch)>100 and ord(ch)<123:
            dcode2 = ord(ch) - 4
            totalWord = str(totalWord) + str(chr(dcode2))

        elif ord(ch) == 97:
            totalWord = str(totalWord)+ str('w')
        elif ord(ch) == 98:
            totalWord = str(totalWord)+ str('x')
        elif ord(ch) == 99:
            totalWord = str(totalWord)+ str('y')
        elif ord(ch) == 100:
            totalWord = str(totalWord)+ str('z')

           

    return totalWord
    

def encoder(words):#encode Function
    totalWord = " "
    for ch in words:
        if ord(ch)>64 and ord(ch)<87:
            ecode1 = ord(ch)+4
            totalWord = str(totalWord) + str(chr(ecode1))#if statements in order to cover all letters
        elif ord(ch) == 87:
            totalWord = str(totalWord)+ str('A')
        elif ord(ch) == 88:
            totalWord = str(totalWord)+ str('B')
        elif ord(ch) == 89:
            totalWord = str(totalWord)+ str('C')
        elif ord(ch) == 90:
            totalWord = str(totalWord)+ str('D')
        elif ord(ch) == 32:
            totalWord = str(totalWord) + str(" ")

        if ord(ch)>96 and ord(ch)<119:
            dcode2 = ord(ch) + 4
            totalWord = str(totalWord) + str(chr(dcode2))

        elif ord(ch) == 119:
            totalWord = str(totalWord)+ str('a')
        elif ord(ch) == 120:
            totalWord = str(totalWord)+ str('b')
        elif ord(ch) == 121:
            totalWord = str(totalWord)+ str('c')
        elif ord(ch) == 122:
            totalWord = str(totalWord)+ str('d')

    return totalWord
    
def drawButton(gwin, pt1, pt2, words, color):
    button = Rectangle(pt1, pt2)
    button.setFill(color)
    button.draw(gwin)

    #find the x and y coords of the middle of the button
    labelx = (pt1.getX() + pt2.getX())/2.0 
    labely = (pt1.getY() + pt2.getY())/2.0

    #use these coords for the position of the label
    label = Text(Point(labelx,labely),words)
    label.setFill("white")
    label.draw(gwin)

    return button

def isClicked(button, pt):
    x0 = button.getP1().getX()
    x1 = button.getP2().getX()
    y0 = button.getP1().getY()
    y1 = button.getP2().getY()
    if ((pt.getX() >= x0 and pt.getX() <= x1) and \
            (pt.getY() >= y0 and pt.getY() <= y1)):
        return True
    else:
        return False

    #isClicked function is the one we created in class

def main():
    win = GraphWin("Decoder/Encoder", 500, 500)#created window
    intro = Text(Point(250,20), "My encoder/decoder has a cipher key of 4")
    intro.draw(win)
    dtext = Text(Point(110,50), "Text you would like to decode:")#text before decode entry box
    dtext.draw(win)
    etext = Text(Point(110,450), "Text you would like to encode:")#text before encode entry box
    etext.draw(win)
    messaged = Text(Point(150,90), "Decoded text:")
    messaged.draw(win)
    messagee = Text(Point(160, 420), "Encoded Text:")
    messagee.draw(win)
    
    dinput = Entry(Point(355,50), 30)#entry box for decode
    dinput.setText("Input Text here")
    dinput.draw(win)
    einput = Entry(Point(355,450), 30)#entry box for encode
    einput.setText("Input Text here.")
    einput.draw(win)

    
    ExitButton = drawButton(win, Point(450,470), Point(490, 490), "Exit", "red")

    DecodeButton = drawButton(win, Point(100,200), Point(200, 300), "Decode", "blue3")

    EncodeButton = drawButton(win, Point(300, 200), Point(400, 300), "Encode", "blue3")


    pt = win.getMouse()

#same while for loop as in the other two programs
        
    while isClicked(DecodeButton, pt) or isClicked(EncodeButton, pt) or isClicked(ExitButton, pt):
        if isClicked(DecodeButton, pt):
            dstr = str(dinput.getText())
            dwords = decoder(dstr)
            doutput = Text(Point(250, 90), dwords)
            doutput.draw(win)
            pt = win.getMouse()
            doutput.undraw()

        if isClicked(EncodeButton, pt):
            estr = str(einput.getText())
            ewords = encoder(estr)
            eoutput = Text(Point(250, 420), ewords)
            eoutput.draw(win)
            pt = win.getMouse()
            eoutput.undraw()
        
        if isClicked(ExitButton, pt):
            win.close()
    

main()
