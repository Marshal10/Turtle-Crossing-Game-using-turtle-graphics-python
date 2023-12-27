import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()

screen.onkeypress(player.move,"Up")

#Spawn some cars first and then start the game
car_manager.starter_cars()
      
      
game_is_on = True
while game_is_on:
    time.sleep(car_manager.speed)
    screen.update()
    
    #Generate a new car 
    car_manager.create_car() 
    #Move all the cars    
    car_manager.move()
    
    #Detect player collision with the cars
    for car in car_manager.all_cars:
        if player.distance(car)<20:
            scoreboard.game_over()
            game_is_on=False

    #Check if the player has reached the finished line    
    if player.reached_finish_line():
        scoreboard.level_up()
        scoreboard.display_level()
        car_manager.increase_speed()
        

screen.exitonclick()