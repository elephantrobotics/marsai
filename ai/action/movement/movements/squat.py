import sys
sys.path.append(".")
from ai.action.movement.movements.poweron import *
from ai.action.movement.movements.basic import *

def squat(mars, times = 0):
    print ("here")
    # 前腿半蹲
    mars.setLegAngle(1, 2, -40, get_rand_speed(0.3, 0.6))
    get_rand_delay_time(0.3, 0.6)
    mars.setLegAngle(2, 2, -40, get_rand_speed(0.3, 0.6))
    get_rand_delay_time(0.8, 1.2)

    print ("here1")

    mars.setLegAngle(1, 3, 50, get_rand_speed(0.3, 0.6))
    mars.setLegAngle(2, 3, 50, get_rand_speed(0.3, 0.6))

    get_rand_delay_time(0.6, 1)
    print ("here2")

    mars.setLegAngle(3, 2, 80, get_rand_speed(0.3, 0.6))
    mars.setLegAngle(4, 2, 80, get_rand_speed(0.3, 0.6))

    print ("here3")
    # 前腿全蹲
    mars.setLegAngle(1, 3, 60, get_rand_speed(0.3, 0.6))
    mars.setLegAngle(2, 3, 60, get_rand_speed(0.3, 0.6))

    get_rand_delay_time(0, 0.5)
    print ("here4")

    mars.setLegAngle(1, 2, -30, get_rand_speed(0.3, 0.6))
    mars.setLegAngle(2, 2, -30, get_rand_speed(0.3, 0.6))
    get_rand_delay_time(0.5, 0.8)
    print ("here5")

    # 晃头
    move_head_tail(mars,times)
