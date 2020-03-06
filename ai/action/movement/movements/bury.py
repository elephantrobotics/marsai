from ai.action.movement.movements.basic import *
from ai.action.movement.movements.poweron import *
import numpy as np


def stand_in_three(mars):
    mars.setLegAngle(2, 1, 10, get_rand_speed(0.4, 0.6))
    mars.setLegAngle(2, 2, 25, get_rand_speed(0.3, 0.5))

    mars.setLegAngle(4, 1, 10, get_rand_speed(0.4, 0.6))
    get_rand_delay_time(0.5, 0.8)
    mars.setLegAngle(3, 1, -20, get_rand_speed(0.4, 0.6))
    # mars.setLegAngle(2, 2, 20, get_rand_speed(0.4, 0.6))
    mars.setLegAngle(3, 3, 30, get_rand_speed(0.4, 0.6))
    get_rand_delay_time(0.5, 0.8)
    mars.setLegAngle(1, 1, -20, get_rand_speed(0.4, 0.6))
    # mars.setLegAngle(1, 2, 20, get_rand_speed(0.4, 0.6))
    mars.setLegAngle(1, 3, 30, get_rand_speed(0.4, 0.6))
    get_rand_delay_time(0.5, 0.8)


def bury_litter(mars, times):
    """
    埋猫砂
    :param mars:
    :return:
    """
    for i in range(times):
        mars.setLegAngle(1, 1, -20, get_rand_speed(0.4, 0.6))
        mars.setLegAngle(1, 2, 30, get_rand_speed(0.4, 0.6))
        mars.setLegAngle(1, 3, 30, get_rand_speed(0.6, 0.8))
        get_rand_delay_time(0.5, 0.8)

        mars.setLegAngle(1, 1, 20, get_rand_speed(0.4, 0.6))
        mars.setLegAngle(1, 2, -10, get_rand_speed(0.4, 0.6))
        mars.setLegAngle(1, 3, -60, get_rand_speed(0.6, 0.8))
        get_rand_delay_time(0.8, 1.2)

        if np.random.normal(0, 1) > 0.8:
            mars.setLegAngle(1, 1, -20, get_rand_speed(0.4, 0.6))
            # mars.setLegAngle(2, 2, 20, get_rand_speed(0.4, 0.6))
            mars.setLegAngle(1, 3, 30, get_rand_speed(0.4, 0.6))
            LookAround3(mars, 8, 40, -15, 20, -20)


def main(mars, times=6):
    stand_in_three(mars)
    bury_litter(mars, times)
    stand_in_three(mars)