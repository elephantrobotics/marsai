import numpy as np
from ai.action.movement.movements.basic import *
from ai.action.movement.movements.sit import *
import ai.actionplanner

def kneading(mars, times=6):
    sit(mars)

    _speed = 0.7

    l = 0
    for i in range(times):
        l += 1
        leg_num = (l % 2 + 1)
        _sign = (l % 2) *2 - 1

        angle_2_ges1 = 0
        angle_3_ges1 = 0

        angle_2_ges2 = -20
        angle_3_ges2 = 60

        j1_angles = -5 * _sign

        mars.setLegAngle(1, 1, j1_angles, _speed)
        mars.setLegAngle(2, 1, -j1_angles, _speed)
        mars.setLegAngle(3, 1, j1_angles, _speed)
        mars.setLegAngle(4, 1, -j1_angles, _speed)
        ai.actionplanner.ActionPlanner.sleep(0.2)

        move_head_tail(mars,1,0)

        mars.setLegAngle(leg_num, 2, angle_2_ges1, _speed)
        mars.setLegAngle(leg_num, 3, angle_3_ges1, _speed)
        ai.actionplanner.ActionPlanner.sleep(0.6)

        mars.setLegAngle(leg_num, 2, angle_2_ges2, _speed)
        mars.setLegAngle(leg_num, 3, angle_3_ges2, _speed)
        move_head_tail(mars,1,0)

        ai.actionplanner.ActionPlanner.sleep(0.6)

        mars.setLegAngle(leg_num, 2, angle_2_ges1, _speed*0.8)
        mars.setLegAngle(leg_num, 3, angle_3_ges1, _speed*0.8)
        ai.actionplanner.ActionPlanner.sleep(0.6)
