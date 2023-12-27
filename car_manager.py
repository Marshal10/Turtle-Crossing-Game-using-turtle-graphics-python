from turtle import Turtle
from random import choice,randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 0.6


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.speed=0.1
        self.create_car()
        
        
    def create_car(self):
        random_y=randint(-250,250)
        random_x=randint(280,300)
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(choice(COLORS))
        self.setheading(180)
        self.goto(random_x,random_y)    
        
        
    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)
        
    def increase_speed(self):
        self.speed*=MOVE_INCREMENT
        return self.speed
        