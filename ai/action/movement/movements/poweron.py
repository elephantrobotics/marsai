import numpy as np
from time import sleep
from ai.action.movement.movements.basic import *
from ai.action.movement.movements.sit import *



def get_rand_angle(angle):
    if angle > 80:
        rand_angle = np.random.randint(1, 10)
    elif 50 < angle < 80:
        rand_angle = np.random.randint(1, 8)
    else:
        rand_angle = np.random.randint(1, 4)

    if np.random.normal(0, 1) > 0.5:
        rand_angle = -rand_angle
    return angle + rand_angle


def get_rand_delay_time(min_time, max_time):
    rand_delay_time = abs(float(str(np.random.uniform(min_time, max_time))[:4]))
    sleep(rand_delay_time)


def get_rand_speed(min_speed, max_speed):
    rand_speed = float(str(np.random.uniform(min_speed, max_speed))[:3])
    return rand_speed


def prone(mars):  # 趴下
    mars.setLegAngle(1, 1, 0, 0.5)
    mars.setLegAngle(1, 2, 70, 0.5)
    mars.setLegAngle(1, 3, 10, 0.5)
    mars.setLegAngle(2, 1, 0, 0.5)
    mars.setLegAngle(2, 2, 70, 0.5)
    mars.setLegAngle(2, 3, 10, 0.5)

    mars.setLegAngle(3, 1, 0, 0.5)
    mars.setLegAngle(3, 2, 50, 0.5)
    mars.setLegAngle(3, 3, 110, 0.5)
    mars.setLegAngle(4, 1, 0, 0.5)
    mars.setLegAngle(4, 2, 50, 0.5)
    mars.setLegAngle(4, 3, 110, 0.5)
    sleep(1)


def fullStretch(mars):  # 全伸展
    # 向前伸懒腰
    # 左前腿伸直
    mars.setLegAngle(1, 2, 80, 0.3)
    mars.setLegAngle(1, 3, -30, 0.3)
    mars.setLegAngle(2, 2, 80, 0.3)
    mars.setLegAngle(2, 3, -30, 0.3)
    sleep(1)
    # 右前腿伸直

    # 前腿下压，后腿上抬，同时抬头
    mars.setLegAngle(1, 2, 80, 0.5)
    mars.setLegAngle(1, 3, 0, 0.5)
    mars.setLegAngle(2, 2, 80, 0.5)
    mars.setLegAngle(2, 3, 0, 0.5)
    sleep(4)

    # 后腿先抬
    rand_speed_1 = get_rand_speed(0.2, 0.7)
    mars.setLegAngle(3, 2, -60, rand_speed_1)
    mars.setLegAngle(4, 2, -60, rand_speed_1)
    get_rand_delay_time(0.3, 0.7)
    mars.setLegAngle(3, 3, -30, rand_speed_1)
    mars.setLegAngle(4, 3, -30, rand_speed_1)
    get_rand_delay_time(0.3, 0.7)

    # 后腿进一步抬
    rand_speed_2 = get_rand_speed(0.2, 0.7)
    mars.setLegAngle(3, 2, -80, rand_speed_2)
    mars.setLegAngle(3, 3, -30, rand_speed_2)
    get_rand_delay_time(0.3, 0.7)
    mars.setLegAngle(4, 2, -80, rand_speed_2)
    mars.setLegAngle(4, 3, -30, rand_speed_2)

    get_rand_delay_time(0.7, 1)

  








def kneading1(mars, times=3):
    mars.setHeadAngle(1, 30, 0.5)
    
    _sign = 0
    angle_2_ges1 = 40
    angle_3_ges1 = 30
    angle_2_ges2 = 0  # -10
    angle_3_ges2 = 70  # 80
    _speed = 1.0
    
    mars.setLegAngle(3, 2, 10, _speed)
    mars.setLegAngle(3, 3, -60, _speed)
    mars.setLegAngle(4, 2, 10, _speed)
    mars.setLegAngle(4, 3, -60, _speed)
    sleep(1)

    for i in range(3):
        leg_num = _sig
        n*2 + 1
        _sign = 1 -_sign
        j1_angles = (_sign*2 - 1) * 7
        mars.setLegAngle(1, 1, j1_angles, _speed)
        mars.setLegAngle(2, 1, -j1_angles, _speed)
        mars.setLegAngle(3, 1, j1_angles, _speed)
        mars.setLegAngle(4, 1, -j1_angles, _speed)

        if leg_num == 2: leg_num = 3
        if leg_num == 3: leg_num = 2
        mars.setLegAngle(leg_num, 2, angle_2_ges1, _speed)
        mars.setLegAngle(leg_num, 3, angle_3_ges1, _speed)
        sleep(0.5)

        mars.setLegAngle(leg_num, 2, angle_2_ges2, _speed)
        mars.setLegAngle(leg_num, 3, angle_3_ges2, _speed)
        sleep(0.5)
        
        mars.setLegAngle(leg_num, 2, angle_2_ges1, _speed*0.7)
        mars.setLegAngle(leg_num, 3, angle_3_ges1, _speed*0.7)
        sleep(0.6)
        

