import numpy as np
from ai.action.movement.movements.poweron import *
from ai.action.movement.movements.basic import *
from ai.actionplanner import ActionPlanner as ap

def main(mars, times=12):
    zhaocai(mars, times)

def zhaocai(mars, times):
    mars.setHeadAngle(1, -50, 0.5)  # 低头

    rand_speed_one = get_rand_speed(0.3, 0.6)
    mars.setLegAngle(1, 1, -10, rand_speed_one)
    mars.setLegAngle(2, 1, -10, rand_speed_one)
    mars.setLegAngle(1, 3, 40, rand_speed_one)
    mars.setLegAngle(2, 3, 40, rand_speed_one)
    get_rand_delay_time(0.3, 0.6)

    rand_speed_two = get_rand_speed(0.3, 0.6)

    mars.setLegAngle(3, 2, 30, rand_speed_two)
    mars.setLegAngle(4, 2, 30, rand_speed_two)
    mars.setLegAngle(3, 3, -90, rand_speed_two)
    mars.setLegAngle(4, 3, -90, rand_speed_two)

    get_rand_delay_time(0.3, 0.6)

    rand_speed_three = get_rand_speed(0.3, 0.6)
    mars.setLegAngle(1, 2, 0, rand_speed_three)
    mars.setLegAngle(2, 2, 0, rand_speed_three)
    mars.setLegAngle(1, 3, 0, rand_speed_three)
    mars.setLegAngle(2, 3, 0, rand_speed_three)
    get_rand_delay_time(0.3, 0.6)

    rand_speed_four = get_rand_speed(0.3, 0.6)

    mars.setLegAngle(3, 2, 50, rand_speed_four)
    mars.setLegAngle(4, 2, 50, rand_speed_four)
    mars.setLegAngle(3, 3, -90, rand_speed_four)
    mars.setLegAngle(4, 3, -90, rand_speed_four)

    mars.setLegAngle(1, 2, 0, rand_speed_four)
    mars.setLegAngle(2, 2, 0, rand_speed_four)
    mars.setLegAngle(1, 3, 0, rand_speed_four)
    mars.setLegAngle(2, 3, 0, rand_speed_four)
    get_rand_delay_time(1, 1.2)

    mars.setHeadAngle(1, 10, 0.5)
    ap.sleep(1)

    a = np.random.normal(0, 1)
    if a > 0:
        leg_num = 1
        mars.setHeadAngle(2, -15, 0.5)
    else:
        leg_num = 2
        mars.setHeadAngle(2, 15, 0.5)

    rand_speed_five = get_rand_speed(0.3, 0.6)
    mars.setLegAngle(leg_num, 1, 0, rand_speed_five)
    mars.setLegAngle(leg_num, 2, 80, rand_speed_five)
    ap.sleep(1)

    for i in range(times):
        leg_angle = int(np.random.uniform(0, 81))
        # print(mars.getLegAngle(leg_num, 3))
        leg_angle_now = 45  # int(mars.getLegAngle(leg_num, 3)[0])
        if leg_angle > leg_angle_now:
            # leg_angle = leg_angle
            if leg_angle - leg_angle_now > 10:
                leg_angle = leg_angle
            else:
                leg_angle = leg_angle + abs(np.random.normal(0, 3) * 10)
                if leg_angle + 20 >= 90:
                    leg_angle = 60
                leg_angle = limitValue(leg_angle, 90, leg_angle + 20)
        else:
            leg_angle_random = leg_angle + abs(np.random.normal(0, 3) * 10 + 10)
            if leg_angle_now + 30 >= 90:
                leg_angle_now = 50
            leg_angle = limitValue(leg_angle_random, 90, leg_angle_now + 30)

        rand_speed_six = get_rand_speed(0.4, 0.7)
        mars.setLegAngle(leg_num, 3, leg_angle, rand_speed_six)
        get_rand_delay_time(0.5, 0.7)

        rand_gau = np.random.normal(0, 3)
        leg_angle_2 = leg_angle - abs(rand_gau * 10) - 10
        if leg_angle - 30 <= 0:
            leg_angle = 10
        leg_angle_2 = limitValue(leg_angle_2, leg_angle - 30, 0)
        mars.setLegAngle(leg_num, 3, leg_angle_2, rand_speed_six)

        get_rand_delay_time(0.5, 0.7)
