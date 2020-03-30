#simple pong game

#libraries 
import turtle #comes with python?

wn = turtle.Screen() #creates screen
wn.title('PyPong')
wn.bgcolor('red') #sets background color 
wn.setup(width = 800, height = 600)

#stops the window from automaticaly updatingl, lets the game run
#faster
wn.tracer(0)

#paddle A
pada = turtle.Turtle()
pada.speed(0) #sets speed of the paddle, 0 is max
pada.shape('square') #20x20
pada.color('black')
pada.shapesize(stretch_wid=5, stretch_len=1)
pada.penup() #stops the turtle from drawing a line w/ movment
pada.goto(-350, 0)

#paddle B
padb = turtle.Turtle()
padb.speed(0) #sets speed of the paddle, 0 is max
padb.shape('square') #20x20
padb.color('black')
padb.shapesize(stretch_wid=5, stretch_len=1)
padb.penup() #stops the turtle from drawing a line w/ movment
padb.goto(350, 0)



#ball
ball = turtle.Turtle()
ball.speed(0) #sets speed of the paddle, 0 is max
ball.shape('square') #20x20
ball.color('black')
ball.penup() #stops the turtle from drawing a line w/ movment
ball.goto(0, 0)


#animating the paddles 
#function

#paddle A 
#up
def pada_up():
    y = pada.ycor()
    y += 20
    pada.sety(y)
    

#down
def pada_down():
    y = pada.ycor()
    y -= 20
    pada.sety(y)

def padb_up():
    y = padb.ycor()
    y += 20
    padb.sety(y)
    

#down
def padb_down():
    y = padb.ycor()
    y -= 20
    padb.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(pada_up, "w")
wn.onkeypress(pada_down, "s")
wn.onkeypress(padb_up, "Up")
wn.onkeypress(padb_down, "Down")



#animating the ball

    


    
    
    

#main game loop
while True: 
    wn.update()
