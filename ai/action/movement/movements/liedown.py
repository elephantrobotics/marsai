from time import sleep

from ai.action.movement.movements.basic import *


def lie_down(mars, times = 0):
    speed_one = 0.7
    mars.setLegAngle(1, 1, 0, speed_one)
    mars.setLegAngle(1, 2, 0, speed_one)
    mars.setLegAngle(1, 3, 65, speed_one)

 

    mars.setLegAngle(2, 1, 0, speed_one)
    mars.setLegAngle(2, 2, 0, speed_one)
    mars.setLegAngle(2, 3, 65, speed_one)
    sleep(0.5)

    mars.setLegAngle(3, 1, 20, speed_one)
    mars.setLegAngle(3, 2, 50, speed_one)
    mars.setLegAngle(3, 3, -70, speed_one)

    mars.setLegAngle(4, 1, 20, speed_one)
    mars.setLegAngle(4, 2, 50, speed_one)
    mars.setLegAngle(4, 3, -70, speed_one)
    sleep(1)
    
    mars.setLegAngle(1, 1, 0, speed_one)
    mars.setLegAngle(1, 2, 0, speed_one)
    mars.setLegAngle(1, 3, 35, speed_one)
 
    mars.setLegAngle(2, 1, 0, speed_one)
    mars.setLegAngle(2, 2, 0, speed_one)
    mars.setLegAngle(2, 3, 35, speed_one)

    
    
    
    move_head_tail(mars,times)
  
