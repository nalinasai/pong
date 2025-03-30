import turtle
window = turtle.Screen()
window.bgcolor("black")
window.title("PONG GAME!!")
window.setup(width=800,height=600)
window.tracer(0) 


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
        ball.dy *= -1

    if(ball.ycor()<-290):
        ball.sety(-290)
        ball.dy *=-1

    if(ball.xcor()>390):
        ball.goto(0,0)
        ball.dx*=-1

    if(ball.xcor()<-390):
        ball.goto(0,0)
        ball.dx*=-1