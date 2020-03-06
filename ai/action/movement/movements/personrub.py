from ai.action.movement.movements.poweron import *


def body_move(mars):
    mars.setLegAngle(1, 2, -60, get_rand_speed(0.2, 0.4))
    mars.setLegAngle(1, 3, 110, get_rand_speed(0.2, 0.4))
    get_rand_delay_time(0.3, 0.5)
    mars.setLegAngle(2, 2, -40, get_rand_speed(0.2, 0.4))
    mars.setLegAngle(2, 3, 70, get_rand_speed(0.2, 0.4))
    get_rand_delay_time(0.3, 0.5)


def rubHuman(mars, times=10):
    for i in range(times):
        mars.setHeadAngle(2, get_rand_angle(20), get_rand_speed(0.1, 0.3))
        mars.setHeadAngle(1, get_rand_angle(-25), get_rand_speed(0.1, 0.3))
        # get_rand_delay_time(0.5, 0.8)
        mars.setLegAngle(1, 2, -60, get_rand_speed(0.1, 0.3))
        mars.setLegAngle(1, 3, 110, get_rand_speed(0.1, 0.3))
        get_rand_delay_time(1, 1.4)

        mars.setHeadAngle(2, get_rand_angle(0), get_rand_speed(0.1, 0.3))
        mars.setHeadAngle(1, get_rand_angle(20), get_rand_speed(0.1, 0.3))
        # get_rand_delay_time(0.5, 0.8)
        mars.setLegAngle(1, 2, -30, get_rand_speed(0.1, 0.3))
        mars.setLegAngle(1, 3, 70, get_rand_speed(0.1, 0.3))
        get_rand_delay_time(1, 1.4)


def main(mars, times=5):
    body_move(mars)
    rubHuman(mars, times)