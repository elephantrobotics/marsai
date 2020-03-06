import numpy as np
from ai.action.movement.movements.basic import *
from ai.action.movement.movements.sit import *
from ai.actionplanner import ActionPlanner as ap

def licking(mars, times=5):
    sit(mars)

    if np.random.random() > 0.5:
        leg_num = 2
        head_2_angle_ = 0
        head_2_angle_2 = -30
    else:
        leg_num = 1
        head_2_angle_ = 0
        head_2_angle_2 = 30

    ap.sleep(0.5)

    mars.setLegAngle(leg_num, 1, -25, 0.5)
    mars.setLegAngle(leg_num, 2, 30, 0.5)
    mars.setLegAngle(leg_num, 3, 70, 0.5)

    mars.setHeadAngle(1, 0, 0.5)
    ap.sleep(0.5)

    for i in range(times):
        mars.setHeadAngle(2, head_2_angle_, 0.4)
        mars.setLegAngle(leg_num, 2, 80, 0.4)

        ap.sleep(0.5)
        mars.setHeadAngle(2, head_2_angle_2, 0.4)
        mars.setLegAngle(leg_num, 2, 30, 0.4)
        ap.sleep(0.5)
