from ai.action.movement.movements.poweron import *
from ai.action.movement.movements.basic import *


def move_foot(mars):
    rand_speed_one = get_rand_speed(0.4, 0.6)
    mars.setLegAngle(1, 2, -40, rand_speed_one)
    mars.setLegAngle(1, 3, 70, rand_speed_one)
    get_rand_delay_time(0.5, 0.8)
    mars.setLegAngle(1, 3, 45, rand_speed_one)
    # mars.setLegAngle(1, 2, -10, rand_speed_one)
    get_rand_delay_time(0.3, 0.6)
    mars.setLegAngle(1, 2, -30, rand_speed_one)
    mars.setLegAngle(1, 3, 30, rand_speed_one)
    get_rand_delay_time(0.6, 0.9)

    rand_speed_one = get_rand_speed(0.4, 0.6)
    mars.setLegAngle(3, 2, -40, rand_speed_one)
    mars.setLegAngle(3, 3, 90, rand_speed_one)
    get_rand_delay_time(0.5, 0.8)
    mars.setLegAngle(3, 3, 45, rand_speed_one)
    mars.setLegAngle(1, 2, -10, rand_speed_one)
    get_rand_delay_time(0.3, 0.6)
    mars.setLegAngle(3, 2, -30, rand_speed_one)
    mars.setLegAngle(3, 3, 30, rand_speed_one)


def sit(mars, times = 0):
    mars.setHeadAngle(1, 0, 0.5)  # 低头

    rand_speed_one = get_rand_speed(0.3, 0.6)
    mars.setLegAngle(1, 1, -10, rand_speed_one)
    mars.setLegAngle(2, 1, -10, rand_speed_one)
    mars.setLegAngle(1, 3, 40, rand_speed_one)
    mars.setLegAngle(2, 3, 40, rand_speed_one)

    rand_speed_two = get_rand_speed(0.3, 0.6)
    
    mars.setLegAngle(3, 2, 30, rand_speed_two)
    mars.setLegAngle(4, 2, 30, rand_speed_two)
    mars.setLegAngle(3, 3, -90, rand_speed_two)
    mars.setLegAngle(4, 3, -90, rand_speed_two)
    
    move_head_tail(mars,1)


    rand_speed_three = get_rand_speed(0.3, 0.6)
    mars.setLegAngle(1, 2, 0, rand_speed_three)
    mars.setLegAngle(2, 2, 0, rand_speed_three)
    mars.setLegAngle(1, 3, 0, rand_speed_three)
    mars.setLegAngle(2, 3, 0, rand_speed_three)

    rand_speed_four = get_rand_speed(0.3, 0.6)

    mars.setLegAngle(3, 2, 50, rand_speed_four)
    mars.setLegAngle(4, 2, 50, rand_speed_four)
    mars.setLegAngle(3, 3, -90, rand_speed_four)
    mars.setLegAngle(4, 3, -90, rand_speed_four)

    mars.setLegAngle(1, 2, 0, rand_speed_four)
    mars.setLegAngle(2, 2, 0, rand_speed_four)
    mars.setLegAngle(1, 3, 0, rand_speed_four)
    mars.setLegAngle(2, 3, 0, rand_speed_four)
    
    move_head_tail(mars,times+1)
    

    
    
