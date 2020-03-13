from ai.action.movement.movements.basic import move_head
from ai.action.movement.movements.poweron import *
from ai.action.movement.movements.sit import *
import ai.actionplanner

def playToy(mars, times=5):
    leg_num = random.choice([1, 2])
    sit(mars)

    for _ in range(times):
        for i in range(random.choice([1,2])):
            mars.setLegAngle(leg_num, 1, 20, get_rand_speed(1, 1))
            mars.setLegAngle(leg_num, 2, 40, get_rand_speed(1, 1))
            mars.setLegAngle(leg_num, 3, 30, get_rand_speed(1, 1))
            ai.actionplanner.ActionPlanner.sleep(0.3)

            mars.setLegAngle(leg_num, 1, -20, get_rand_speed(1, 1))
            mars.setLegAngle(leg_num, 2, 40, get_rand_speed(1, 1))
            mars.setLegAngle(leg_num, 3, -70, get_rand_speed(1, 1))
            get_rand_delay_time(0.3, 0.5)

        mars.setLegAngle(leg_num, 1, -10, 0.5)
        mars.setLegAngle(leg_num, 2, 0, 0.5)
        mars.setLegAngle(leg_num, 3, 0, 0.5)
        move_head_tail(mars)
