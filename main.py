import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

cars=[]
index=0

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player=Player()
scoreboard=Scoreboard()

screen.onkeypress(player.move,"Up")

for i in range(25):
    if i%6==0:
        cars.append(CarManager())
        
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    #Generate a new car 
    if index%6==0:
        cars.append(CarManager())  
    index+=1   
    
    #Move all the cars
    for car in cars:
        car.move()
        if player.distance(car)<20:
            scoreboard.game_over()
            game_is_on=False
            break
        
    #Detect player collision with the cars
    
        
    player.reached_finish_line()    
        

screen.exitonclick()