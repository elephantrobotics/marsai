from ai.action.movement.movements.poweron import *


def walk_around(mars):
    rand_speed_one = get_rand_speed(0.4, 0.6)
    mars.setWalk(rand_speed_one)
    get_rand_delay_time(8, 12)
    a = np.random.normal(0, 1)
    if a > -2:     # 10% 1.65
        mars.setStop()
        sleep(1)
        get_rand_delay_time(0.3, 0.5)

        rand_speed = get_rand_speed(0.3, 0.6)
        mars.setLegAngle(1, 2, -10, rand_speed)
        mars.setLegAngle(1, 3, 80, rand_speed)
        mars.setLegAngle(2, 2, -10, rand_speed)
        mars.setLegAngle(2, 3, 80, rand_speed)
        sleep(1)
        mars.setLegAngle(3, 2, 30, rand_speed)
        mars.setLegAngle(3, 3, -80, rand_speed)
        mars.setLegAngle(4, 2, 30, rand_speed)
        mars.setLegAngle(4, 3, -80, rand_speed)
        sleep(1)
        # init(mars)
        get_rand_delay_time(0.3, 0.5)
        LookAround(mars, 5, 0, -50, 20, -20)
        get_rand_delay_time(0.3, 0.6)