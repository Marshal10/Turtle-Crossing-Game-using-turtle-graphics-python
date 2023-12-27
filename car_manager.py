from turtle import Turtle
from random import choice,randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 0.6


class CarManager():
    def __init__(self):
        self.all_cars=[]
        self.speed=0.1
        
        
    def create_car(self):
        random_y=randint(-250,250)
        random_x=randint(280,300)
        new_car=Turtle("square")
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(choice(COLORS))
        new_car.setheading(180)
        new_car.goto(random_x,random_y) 
        self.all_cars.append(new_car)
        
    def starter_cars(self):
        random_y=randint(-250,250)
        random_x=randint(-300,300)
        new_car=Turtle("square")
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(choice(COLORS))
        new_car.setheading(180)
        new_car.goto(random_x,random_y)
        self.all_cars.append(new_car)
        
        
    def move(self,car):
        car.forward(STARTING_MOVE_DISTANCE)
        
    def increase_speed(self):
        self.speed*=MOVE_INCREMENT
        return self.speed
        