# imports
import turtle as trtl
import random as rand

# game setup
meteor_image = "flaming_meteor.gif"
x_offset = -20
y_offset = -47
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(meteor_image)
wn.bgpic("space_background.gif")
meteor = trtl.Turtle()
wn.tracer(False)
screen_width = 600
screen_height = 600
letter_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
current_letter = "H"

# functions
def reset_meteor(active_meteor):
    global current_letter
    length = len(letter_list)
    if(length != 0):
        index = rand.randint(0, length-1)
        active_meteor.goto(rand.randint(-screen_width/2, screen_width/2), rand.randint(-screen_height + 800, screen_height/2))
        current_letter = letter_list.pop(index)
        draw_meteor(active_meteor, current_letter)

def draw_meteor(active_meteor, letter):
    active_meteor.penup()
    active_meteor.shape(meteor_image)
    active_meteor.showturtle()
    draw_letter(letter, active_meteor)
    wn.update()

def meteor_drop():
    wn.tracer(True)
    meteor.penup()
    meteor.speed(0)
    meteor.goto(rand.randint(-screen_width/2, screen_width/2), rand.randint(-screen_height + 800, screen_height/2))
    meteor.speed(20)
    meteor.hideturtle()
    meteor.clear()
    wn.tracer(False)
    reset_meteor(meteor)

def draw_letter(letter, active_meteor):
    active_meteor.color("white")
    remember_pos = active_meteor.position()
    active_meteor.setpos(active_meteor.xcor() + x_offset, active_meteor.ycor() + y_offset)
    active_meteor.write(letter, font=("Arial", 50, "bold"))
    active_meteor.setpos(remember_pos)
    
def checkA():
  if(current_letter == "A"):
    meteor_drop()

def checkB():
  if(current_letter == "B"):
    meteor_drop()

def checkC():
  if(current_letter == "C"):
    meteor_drop()

def checkD():
  if(current_letter == "D"):
    meteor_drop()

def checkE():
  if(current_letter == "E"):
    meteor_drop()

def checkF():
  if(current_letter == "F"):
    meteor_drop()

def checkG():
  if(current_letter == "G"):
    meteor_drop()

def checkH():
  if(current_letter == "H"):
    meteor_drop()

def checkI():
  if(current_letter == "I"):
    meteor_drop()

def checkJ():
  if(current_letter == "J"):
    meteor_drop()

def checkK():
  if(current_letter == "K"):
    meteor_drop()

def checkL():
  if(current_letter == "L"):
    meteor_drop()

def checkM():
  if(current_letter == "M"):
    meteor_drop()

def checkN():
  if(current_letter == "N"):
    meteor_drop()

def checkO():
  if(current_letter == "O"):
    meteor_drop()

def checkP():
  if(current_letter == "P"):
    meteor_drop()

def checkQ():
  if(current_letter == "Q"):
    meteor_drop()

def checkR():
  if(current_letter == "R"):
    meteor_drop()

def checkS():
  if(current_letter == "S"):
    meteor_drop()

def checkT():
  if(current_letter == "T"):
    meteor_drop()

def checkU():
  if(current_letter == "U"):
    meteor_drop()

def checkV():
  if(current_letter == "V"):
    meteor_drop()

def checkW():
  if(current_letter == "W"):
    meteor_drop()

def checkX():
  if(current_letter == "X"):
    meteor_drop()

def checkY():
  if(current_letter == "Y"):
    meteor_drop()

def checkZ():
  if(current_letter == "Z"):
    meteor_drop()

# function calls
draw_meteor(meteor, "H")
wn.onkeypress(checkA, "a")
wn.onkeypress(checkB, "b")
wn.onkeypress(checkC, "c")
wn.onkeypress(checkD, "d")
wn.onkeypress(checkE, "e")
wn.onkeypress(checkF, "f")
wn.onkeypress(checkG, "g")
wn.onkeypress(checkH, "h")
wn.onkeypress(checkI, "i")
wn.onkeypress(checkJ, "j")
wn.onkeypress(checkK, "k")
wn.onkeypress(checkL, "l")
wn.onkeypress(checkM, "m")
wn.onkeypress(checkN, "n")
wn.onkeypress(checkO, "o")
wn.onkeypress(checkP, "p")
wn.onkeypress(checkQ, "q")
wn.onkeypress(checkR, "r")
wn.onkeypress(checkS, "s")
wn.onkeypress(checkT, "t")
wn.onkeypress(checkU, "u")
wn.onkeypress(checkV, "v")
wn.onkeypress(checkW, "w")
wn.onkeypress(checkX, "x")
wn.onkeypress(checkY, "y")
wn.onkeypress(checkZ, "z")



wn.listen()
wn.mainloop()
