from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title='Who Will Win?', prompt='Which turtle will win the race? Enter a color (ROYGBP):')

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
for i, c in enumerate(colors):
    t = Turtle(shape="turtle")
    t.color(c)
    t.penup()
    t.goto(-225, -75+i*30)
    turtles.append(t)

race_on = True
while race_on:
    for t in turtles:
        t.forward(randint(0,10))
        if t.pos()[0] > 240:
            t.goto(239, t.pos()[1])
            race_on = False
            winner = t.color()[0]

if winner == user_bet.lower():
    print(f"You've won! The {winner} turtle was the winner.")
else:
    print(f"You've lost! The {winner} turtle was the winner.")

screen.exitonclick()