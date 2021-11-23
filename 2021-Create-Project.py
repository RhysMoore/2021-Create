# imports
import turtle as trtl
import random as rand

# game setup
x_offset = -20
y_offset = -47
screen_width = 400
screen_height = 400
meteor_image = "flaming_meteor.gif"
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(meteor_image)
wn.bgpic("galaxy-space.gif")
meteor = trtl.Turtle()
wn.tracer(False)
letter_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
current_letter = "G"

# functions
def reset_meteor(active_meteor):
    global current_letter
    length = len(letter_list)
    if(length != 0):
        index = rand.randint(0, length-1)
        active_meteor.goto(rand.randint(-screen_width/2, screen_width/2), rand.randint(-screen_height/2, screen_height/2))
        current_letter = letter_list.pop(index)
        draw_meteor(active_meteor, current_letter)

def draw_meteor(active_meteor, letter):
    active_meteor.penup()
    active_meteor.shape(meteor_image)
    active_meteor.showturtle()
    draw_letter(letter, active_meteor)

def meteor_drop():
    wn.tracer(True)
    meteor.penup()
    meteor.goto(meteor.xcor(), -250)
    meteor.hideturtle
    meteor.clear()
    wn.tracer(False)
    reset_meteor(meteor)

def draw_lettter(letter, active_meteor):
    active_meteor.color("white")
    remember_pos





wn.listen()
wn.mainloop()
