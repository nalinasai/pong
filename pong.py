#ready to make public

import turtle
#import winsound
window = turtle.Screen()
window.bgcolor("black")
window.title("PONG GAME!!")
window.setup(width=800,height=600)
window.tracer(0) 

#score
score_a = 0
score_b = 0


#paddle a
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.speed(0)
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


#paddle b
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.penup()
paddle_b.speed(0)
paddle_b.shapesize(stretch_len=1,stretch_wid=5)
paddle_b.goto(350,0)
paddle_b.color("white")

#ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.speed(0)
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

#pen
pen = turtle.Turtle()
pen.penup()
pen.color("white")
pen.goto(0,260)

pen.speed(0)
pen.hideturtle()
pen.write("Player A: 0   Player B: 0",align="center",font=("Arial",24,"bold"))


#function
def paddle_a_up():
    y = paddle_a.ycor()
    y = y + 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y = y - 20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y=y+20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y=y-20
    paddle_b.sety(y)


window.listen()
window.onkeypress(paddle_a_up,"u")
window.onkeypress(paddle_a_down,"d")
window.onkeypress(paddle_b_up,"Up")
window.onkeypress(paddle_b_down,"Down")


while True:
    window.update()

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #boarder checking
    if(ball.ycor()>290):
        ball.sety(290)
        ball.dy *=-1
        #winsound.PlaySound("ball-bounce-94853",winsound.SND_ASYNC)

    if(ball.ycor()<-290):
        ball.sety(-290)
        ball.dy *=-1
        #winsound.PlaySound("ball-bounce-94853",winsound.SND_ASYNC)

    if(ball.xcor()>390):
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a,score_b),align="center",font=("Arial",24,"bold"))
        #winsound.PlaySound("ball-bounce-94853",winsound.SND_ASYNC)

    if(ball.xcor()<-390):
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a,score_b),align="center",font=("Arial",24,"bold"))
        #winsound.PlaySound("ball-bounce-94853",winsound.SND_ASYNC)


    if(ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()> paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    
    if(ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()> paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1

