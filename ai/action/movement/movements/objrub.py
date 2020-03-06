import numpy as np
from ai.action.movement.movements.basic import *
from ai.action.movement.movements.poweron import *
from ai.actionplanner import ActionPlanner as ap

def main(mars, times=5):
    rub_object(mars, times)


def rub_object(mars, times):
    for i in range(times):
        rand_speed_1 = get_rand_speed(0.3, 0.5)
        mars.setHeadAngle(2, get_rand_angle(25), get_rand_speed(0.1, 0.3))
        mars.setHeadAngle(1, get_rand_angle(-25), get_rand_speed(0.1, 0.3))

        mars.setLegAngle(1, 1, 0, rand_speed_1)
        mars.setLegAngle(2, 1, -10, rand_speed_1)
        mars.setLegAngle(1, 2, -30, rand_speed_1)
        mars.setLegAngle(2, 2, 10, rand_speed_1)
        mars.setLegAngle(1, 3, 80, rand_speed_1)
        mars.setLegAngle(2, 3, 10, rand_speed_1)
        mars.setLegAngle(3, 1, 15, rand_speed_1)
        mars.setLegAngle(3, 2, 20, rand_speed_1)
        mars.setLegAngle(3, 3, -80, rand_speed_1)
        mars.setLegAngle(4, 1, -15, rand_speed_1)
        mars.setLegAngle(4, 2, 20, rand_speed_1)
        mars.setLegAngle(4, 3, -70, rand_speed_1)
        ap.sleep(2)

        rand_speed_2 = get_rand_speed(0.3, 0.5)
        mars.setHeadAngle(2, get_rand_angle(0), get_rand_speed(0.1, 0.3))
        mars.setHeadAngle(1, get_rand_angle(25), get_rand_speed(0.1, 0.3))
        mars.setLegAngle(1, 1, int(np.random.uniform(15, 21)), rand_speed_2)
        mars.setLegAngle(2, 1, 0, rand_speed_2)
        mars.setLegAngle(1, 2, int(np.random.uniform(10, 15)), rand_speed_2)
        mars.setLegAngle(2, 2, 20, rand_speed_2)
        mars.setLegAngle(1, 3, int(np.random.uniform(10, 15)), rand_speed_2)
        mars.setLegAngle(2, 3, 20, rand_speed_2)
        mars.setLegAngle(3, 1, 0, rand_speed_2)
        mars.setLegAngle(3, 2, 40, rand_speed_2)
        mars.setLegAngle(3, 3, -40, rand_speed_2)
        mars.setLegAngle(4, 1, 15, rand_speed_2)
        mars.setLegAngle(4, 2, 40, rand_speed_2)
        mars.setLegAngle(4, 3, -40, rand_speed_2)
        ap.sleep(2)
