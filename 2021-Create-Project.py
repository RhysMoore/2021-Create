# imports
import turtle as trtl
import random as rand

# game setup
lives = 3
font_setup = "arial", 40, "bold"
meteor_image = "flaming_meteor.gif"
x_offset = -20
y_offset = -47
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(meteor_image)
wn.bgpic("space_background.gif")
life_counter = trtl.Turtle()
life_counter.penup()
life_counter.speed("fastest")
life_counter.goto(300, -400)
life_counter.hideturtle()
life_counter.color("white")
game_starter = trtl.Turtle()
game_starter.hideturtle()
game_starter.speed("fastest")
game_starter.goto(0, 0)
screen_width = 600
screen_height = 800
meteor = trtl.Turtle()
meteor.hideturtle()
meteor.penup()
meteor.speed("fastest")
meteor.goto(rand.randint(-screen_width/2, screen_width/2), rand.randint(-screen_height/-2, screen_height/2))
letter_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
current_letter = "F"
# functions
def start_game():
    game_starter.write("click to begin", font=font_setup)

def reset_meteor(active_meteor):
    global current_letter
    length = len(letter_list)
    if(length != 0):
        index = rand.randint(0, length-1)
        active_meteor.goto(rand.randint(-screen_width/2, screen_width/2), rand.randint(-screen_height/-2, screen_height/2))
        current_letter = letter_list.pop(index)
        draw_meteor(active_meteor, current_letter)
        meteor.penup()
        meteor.goto(meteor.xcor(), -400)
        meteor_respawn()

def draw_meteor(active_meteor, letter):
    active_meteor.penup()
    active_meteor.shape(meteor_image)
    active_meteor.speed("fastest")
    draw_letter(letter, active_meteor)
    active_meteor.showturtle()
    active_meteor.speed(2.5)
    wn.update()

def meteor_respawn():
    meteor.hideturtle()
    meteor.clear()
    reset_meteor(meteor)

def life_change():
    global lives
    lives -= 1
    life_counter.clear()
    life_counter.write(lives, font=font_setup)
    if(lives == 0):
        game_over()

def draw_letter(letter, active_meteor):
    active_meteor.color("white")
    remember_pos = active_meteor.position()
    active_meteor.setpos(rand.randint(-screen_width/2, screen_width/2), rand.randint(-screen_height/2, screen_height/2))
    active_meteor.write(letter, font=("Arial", 50, "bold"))
    active_meteor.setpos(remember_pos)

def game_over():
    if(lives == 0):
        meteor.clear()
        game_starter.write("Out of lives! CLick to play again", font=font_setup)

def checkA():
  if(current_letter == "A"):
    meteor_respawn()

def checkB():
  if(current_letter == "B"):
    meteor_respawn()

def checkC():
  if(current_letter == "C"):
    meteor_respawn()

def checkD():
  if(current_letter == "D"):
    meteor_respawn()

def checkE():
  if(current_letter == "E"):
    meteor_respawn()

def checkF():
  if(current_letter == "F"):
    meteor_respawn()

def checkG():
  if(current_letter == "G"):
    meteor_respawn()

def checkH():
  if(current_letter == "H"):
    meteor_respawn()

def checkI():
  if(current_letter == "I"):
    meteor_respawn()

def checkJ():
  if(current_letter == "J"):
    meteor_respawn()

def checkK():
  if(current_letter == "K"):
    meteor_respawn()

def checkL():
  if(current_letter == "L"):
    meteor_respawn()

def checkM():
  if(current_letter == "M"):
    meteor_respawn()

def checkN():
  if(current_letter == "N"):
    meteor_respawn()

def checkO():
  if(current_letter == "O"):
    meteor_respawn()

def checkP():
  if(current_letter == "P"):
    meteor_respawn()

def checkQ():
  if(current_letter == "Q"):
    meteor_respawn()

def checkR():
  if(current_letter == "R"):
    meteor_respawn()

def checkS():
  if(current_letter == "S"):
    meteor_respawn()

def checkT():
  if(current_letter == "T"):
    meteor_respawn()

def checkU():
  if(current_letter == "U"):
    meteor_respawn()

def checkV():
  if(current_letter == "V"):
    meteor_respawn()

def checkW():
  if(current_letter == "W"):
    meteor_respawn()

def checkX():
  if(current_letter == "X"):
    meteor_respawn()

def checkY():
  if(current_letter == "Y"):
    meteor_respawn()

def checkZ():
  if(current_letter == "Z"):
    meteor_respawn()

# function calls
wn.
draw_meteor(meteor, "F")
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
