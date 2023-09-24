import turtle
import time
import random
delay = 0.1
# Score
score = 0
high_score = 0

# Set up the screen
s = turtle.Screen()

s.title("Turtle Dance")

s.bgcolor("white")

s.setup(width=700, height=600)

s.tracer(0)

# Turns off the screen updates

#border
mistri=turtle.Turtle()
mistri.color("green","green")
mistri.penup()
mistri.goto(-310,310)
mistri.pendown()
mistri.begin_fill()
mistri.left(90)
mistri.backward(620)
mistri.right(90)
mistri.forward(620)
mistri.left(90)
mistri.forward(620)
mistri.left(90)
mistri.forward(620)
mistri.end_fill()
mistri.penup()
mistri.forward(1000)






# Saap


saap = turtle.Turtle()

saap.speed(0)

saap.shape("square")

saap.color("yellow")

saap.penup()

saap.goto(0,0)

saap.direction = "stop"



# Saap ka khaana

food = turtle.Turtle()

food.speed(0)

food.shape("circle")

food.color("red")

food.penup()

food.goto(0,100)



segments = []



# Pen

pen = turtle.Turtle()

pen.speed(0)

pen.shape("turtle")

pen.color("white")

pen.penup()

pen.hideturtle()

pen.goto(0, 260)

pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))



# Functions

def go_up():

    if saap.direction != "down":

        saap.direction = "up"



def go_down():

    if saap.direction != "up":

        saap.direction = "down"



def go_left():

    if saap.direction != "right":

        saap.direction = "left"



def go_right():

    if saap.direction != "left":

        saap.direction = "right"



def move():

    if saap.direction == "up":

        y = saap.ycor()

        saap.sety(y + 20)



    if saap.direction == "down":

        y = saap.ycor()

        saap.sety(y - 20)



    if saap.direction == "left":

        x = saap.xcor()

        saap.setx(x - 20)



    if saap.direction == "right":

        x = saap.xcor()

        saap.setx(x + 20)



# Key binding

s.listen()
s.onkeypress(go_up, "w")
s.onkeypress(go_down, "s")
s.onkeypress(go_left, "a")
s.onkeypress(go_right, "d")

# Main game loop

while True:
    s.update()
    # Check for a collision with the border

    if saap.xcor()>290 or saap.xcor()<-290 or saap.ycor()>290 or saap.ycor()<-290:

        time.sleep(1)

        saap.goto(0,0)

        saap.direction = "stop"

        # Hide the segments

        for segment in segments:

            segment.goto(1000, 1000)

                # Clear the segments list

        segments.clear()

        # Reset the score

        score = 0

        # Reset the delay

        delay = 0.1

        pen.clear()

        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # Check for a collision with food

    if saap.distance(food) < 20:

        # Move the food to random spot

        x = random.randint(-290, 290)

        y = random.randint(-290, 290)

        food.goto(x,y)

        # Add segment

        new_segment = turtle.Turtle()

        new_segment.speed(0)

        new_segment.shape("square")

        new_segment.color("grey")

        new_segment.penup()

        segments.append(new_segment)

        # Shorten the delay

        delay -= 0.001

        # Increase the score

        score += 10

        if score > high_score:

            high_score = score

        pen.clear()

        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # Move the end segments first in reverse order

    for index in range(len(segments)-1, 0, -1):

        x = segments[index-1].xcor()

        y = segments[index-1].ycor()

        segments[index].goto(x, y)

    # Move segment 0 to where the saap is

    if len(segments) > 0:

        x = saap.xcor()

        y = saap.ycor()

        segments[0].goto(x,y)

    move()    

    # Check for saap collision with the body segments

    for segment in segments:

        if segment.distance(saap) < 20:

            time.sleep(1)

            saap.goto(0,0)

            saap.direction = "stop"

            # Hide the segments

            for segment in segments:

                segment.goto(1000, 1000)
        

            # Clear the segments list

            segments.clear()

            # Reset the score

            score = 0

            # Reset the delay

            delay = 0.1

    
            # Update the score display

            pen.clear()

            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

s.mainloop()
