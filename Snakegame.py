import turtle
import random
import time

hiz = 0.10
puan = 0

yaz = turtle.Turtle()
yaz.speed(0)
yaz.shape("square")
yaz.color("white")
yaz.penup()
yaz.goto(0, 260)
yaz.hideturtle()
yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))

pencere = turtle.Screen()
pencere.title("Snake Game")
pencere.bgcolor("black")
pencere.setup(width=600, height=600)
pencere.tracer(0)

kafa = turtle.Turtle()
kafa.speed(0)
kafa.shape("square")
kafa.color("red")
kafa.penup()
kafa.goto(0, 100)
kafa.direction = "stop"

yemek = turtle.Turtle()
yemek.speed(0)
yemek.shape("circle")
yemek.color("yellow")
yemek.penup()
yemek.goto(0, 0)
yemek.direction = "stop"
yemek.shapesize(0.60, 0.60)

kuyruk = []

def goUp():
    if kafa.direction != "down":
        kafa.direction = "up"

def goDown():
    if kafa.direction != "up":
        kafa.direction = "down"

def goRight():
    if kafa.direction != "left":
        kafa.direction = "right"

def goLeft():
    if kafa.direction != "right":
        kafa.direction = "left"

def move():
    if kafa.direction == "up":
        y = kafa.ycor()
        kafa.sety(y + 20)
    if kafa.direction == "down":
        y = kafa.ycor()
        kafa.sety(y - 20)
    if kafa.direction == "right":
        x = kafa.xcor()
        kafa.setx(x + 20)
    if kafa.direction == "left":
        x = kafa.xcor()
        kafa.setx(x - 20)

def add_segment():
    segment = turtle.Turtle()
    segment.speed(0)
    segment.shape("square")
    segment.color("green")
    segment.penup()
    kuyruk.append(segment)

pencere.listen()
pencere.onkey(goUp, "Up")
pencere.onkey(goDown, "Down")
pencere.onkey(goRight, "Right")
pencere.onkey(goLeft, "Left")

while True:
    pencere.update()

    if kafa.xcor() > 300 or kafa.xcor() < -300 or kafa.ycor() > 300 or kafa.ycor() < -300:

        time.sleep(1)
        kafa.goto(0, 0)
        kafa.direction = "stop"

        for segment in kuyruk:
            segment.goto(1000, 1000)
        
        kuyruk.clear()  
        puan = 0
        yaz.clear()
        yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))
        hiz = 0.08

    if kafa.distance(yemek) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        yemek.goto(x, y)
        add_segment()
        hiz = hiz - 0.009 
        puan = puan + 10
        yaz.clear()
        yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))

    for i in range(len(kuyruk) - 1, 0, -1):
        x = kuyruk[i - 1].xcor()
        y = kuyruk[i - 1].ycor()
        kuyruk[i].goto(x, y)

    if len(kuyruk) > 0:
        x = kafa.xcor()
        y = kafa.ycor()
        kuyruk[0].goto(x, y)
    
    move()
    time.sleep(hiz)
