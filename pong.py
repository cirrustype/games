#simple pong game


#libraries 
import turtle #comes with python?

wn = turtle.Screen() #creates screen
wn.title('PyPong')
wn.bgcolor('blue') #sets background color 
wn.setup(width = 800, height = 600)

#stops the window from automaticaly updatingl, lets the game run
#faster
wn.tracer(0)


#score keeping
score_A = 0
score_B = 0

#paddle A
pada = turtle.Turtle()
pada.speed(0) #sets speed of the paddle, 0 is max
pada.shape('square') #20x20
pada.color('white')
pada.shapesize(stretch_wid=5, stretch_len=1)
pada.penup() #stops the turtle from drawing a line w/ movment
pada.goto(-350, 0)

#paddle B
padb = turtle.Turtle()
padb.speed(0) #sets speed of the paddle, 0 is max
padb.shape('square') #20x20
padb.color('white')
padb.shapesize(stretch_wid=5, stretch_len=1)
padb.penup() #stops the turtle from drawing a line w/ movment
padb.goto(350, 0)



#ball
ball = turtle.Turtle()
ball.speed(0) #sets speed of the paddle, 0 is max
ball.shape('square') #20x20
ball.color('white')
ball.penup() #stops the turtle from drawing a line w/ movment
ball.goto(0, 0)
ball.dx = .1 # horizontal movment by 2 pix
ball.dy = .1 # vertical movment by 2 pix
# to move the ball put in main loop
#make random???

#obstical
speedbump = turtle.Turtle()
speedbump.speed(0)
speedbump.shape('square')
speedbump.shapesize(stretch_wid = 4, stretch_len = 1)
speedbump.color('yellow')
speedbump.penup()
speedbump.goto(-20,0)
speedbump.dy = .2
speedbump.dx = 0

#score board
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup() # so the turtle does not draw a line when it leaves the origin
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align = "center", font =("Courier", 24, "normal"))

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


#main game loop
while True: 
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #move the speedbump
    
    
    #border checking
    # height 600, top y is 300
    if ball.ycor() > 290:
        ball.sety(290) #stops at border
        ball.dy *= -1 # reverses direction of the ball.
        
        
        
    if ball.ycor() < -290:
        ball.sety(-290) #stops at border
        ball.dy *= -1 # reverses direction of the ball.


#hitting right side
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_A += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_A, score_B), align = "center", font =("Courier", 24, "normal"))


#hitting left side
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_B +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_A, score_B), align = "center", font =("Courier", 24, "normal"))

    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < padb.ycor()+ 40 and ball.ycor() > padb.ycor() - 40):
        ball.setx(340) #why????
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < pada.ycor() + 40 and ball.ycor() > pada.ycor() - 40):
        ball.setx(-340) #why????
        ball.dx *= -1

    

##add in sound and non controlable turtles to mix it up

    
    
    
