import numpy as np
from ai.action.movement.movements.basic import *
import ai.actionplanner

def attacking(mars):
    rand_speed = np.random.uniform(0.2, 0.4)

    mars.setLegAngle(1, 2, 80, rand_speed)
    mars.setLegAngle(2, 2, 80, rand_speed)
    ai.actionplanner.ActionPlanner.sleep(1)
    mars.setLegAngle(1, 3, -10, rand_speed)
    mars.setLegAngle(2, 3, -10, rand_speed)
    ai.actionplanner.ActionPlanner.sleep(1)
    mars.setLegAngle(1, 1, -20, rand_speed)
    mars.setLegAngle(2, 1, -20, rand_speed)
    move_head_tail(mars,1)

    times = int(np.random.uniform(3, 5))

    for i in range(times):
        rand_speed_2 = 0.8
        rand_angle = 8

        mars.setLegAngle(3, 1, 0, rand_speed_2)
        mars.setLegAngle(4, 1, rand_angle, rand_speed_2)
        move_tail(mars)
        ai.actionplanner.ActionPlanner.sleep(0.5)
        mars.setLegAngle(3, 1, rand_angle, rand_speed_2)
        mars.setLegAngle(4, 1, 0, rand_speed_2)
        move_tail(mars)
        ai.actionplanner.ActionPlanner.sleep(0.5)

    ai.actionplanner.ActionPlanner.sleep(0.5)
    mars.setLegAngle(3, 2, -30, rand_speed)
    mars.setLegAngle(4, 2, -30, rand_speed)
    move_head_tail(mars,1)
    mars.setLegAngle(3, 3, -50, rand_speed)
    mars.setLegAngle(4, 3, -50, rand_speed)

    move_head_tail(mars,1)
