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
car_speed=cars[0].speed        
game_is_on = True

while game_is_on:
    time.sleep(car_speed)
    screen.update()
    
    #Generate a new car 
    if index%6==0:
        cars.append(CarManager())  
    index+=1   
    
    #Move all the cars
    for car in cars:
        car.move()
        #Detect player collision with the cars
        if player.distance(car)<20:
            scoreboard.game_over()
            game_is_on=False
            break
        
    
    
    #Check if the player has reached the finished line    
    if player.reached_finish_line():
        scoreboard.level_up()
        scoreboard.display_level()
        car_speed=cars[0].increase_speed()
        
        

screen.exitonclick()