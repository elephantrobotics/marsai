import numpy as np
from ai.action.movement.movements.poweron import *
from ai.actionplanner import ActionPlanner as ap

def wagging(mars):
    rand_speed = get_rand_speed(0.5, 0.7)
    mars.setLegAngle(1, 1, 0, rand_speed)
    mars.setLegAngle(2, 1, 0, rand_speed)
    ap.sleep(0.5)
    mars.setLegAngle(1, 2, 0, rand_speed)
    mars.setLegAngle(2, 2, 0, rand_speed)
    ap.sleep(0.5)
    mars.setLegAngle(1, 3, 80, rand_speed)
    mars.setLegAngle(2, 3, 80, rand_speed)
    ap.sleep(0.5)
    mars.setLegAngle(3, 1, 10, rand_speed)
    mars.setLegAngle(4, 1, 10, rand_speed)
    ap.sleep(0.5)
    mars.setLegAngle(3, 3, -25, rand_speed)
    mars.setLegAngle(4, 3, -25, rand_speed)
    ap.sleep(0.5)
    mars.setLegAngle(3, 2, 0, rand_speed)
    mars.setLegAngle(4, 2, 0, rand_speed)
    ap.sleep(0.5)
    mars.setHeadAngle(1, 20, rand_speed)
    mars.setHeadAngle(2, 0, rand_speed)
    ap.sleep(0.5)

    # 开始晃屁股
    times = int(np.random.uniform(8, 10))
    for i in range(times):
        # rand_speed_2 = act_PowerOn.get_rand_speed(0.7, 1)
        rand_speed_2 = 0.8
        rand_angle = get_rand_angle(20)
        mars.setLegAngle(3, 1, 0, rand_speed_2)
        mars.setLegAngle(4, 1, rand_angle, rand_speed_2)
        ap.sleep(0.5)
        mars.setLegAngle(3, 1, rand_angle, rand_speed_2)
        mars.setLegAngle(4, 1, 0, rand_speed_2)
        ap.sleep(0.5)