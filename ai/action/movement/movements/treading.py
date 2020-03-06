import time
import numpy as np
from time import sleep
from ai.action.movement.movements.basic import *
from ai.action.movement.movements import sit


def main(mars, times=3, lookaround=True):
    sit.main(mars)
    sleep(0.2)
    treading(mars, times, lookaround=lookaround)


def treading(mars, times=3, lookaround=True):  # 踩奶
    mars.setHeadAngle(1, -30, 0.5)
    sleep(0.5)
    head_Max1 = 50
    head_Min1 = -50
    head_Max2 = 30
    head_Min2 = -30
    select_Mode = np.random.normal(0, 1)
    mode_Threshold1 = 1.5
    mode_Threshold2 = 0.8
    select_Mode = 1.6
    flag = False
    count = 0
    a = int(np.random.uniform(0, times))
    """
    if select_Mode > mode_Threshold1:
        treadingSitInit(mars)
    elif select_Mode > mode_Threshold2:
        treadingStandInit(mars)
    else:
        treadingDownInit(mars)
    """
    mars.setHeadAngle(1, 0, 0.7)
    for i in range(times):
        rand_speed_Left = np.random.random() * 0.7
        rand_speed_Right = np.random.random() * 0.7

        rand_speed_Left = limitValue(rand_speed_Left, 0.7, 0.001)
        rand_speed_Right = limitValue(rand_speed_Right, 0.7, 0.001)

        """
        a = np.random.normal(0, 1)
        if a > 2 and lookaround is True:
            rand_times = int(abs(np.random.normal(0, 2)) + 1)
            print("抬头")
            LookAround(mars, rand_times, head_Max1, head_Min1, head_Max2, head_Min2)
            mars.setHeadAngle(1, -30, 0.5)
        """

        if select_Mode > mode_Threshold1:
            treadingSitLeft(mars, rand_speed_Left)
        elif select_Mode > mode_Threshold2:
            treadingStandLeft(mars, rand_speed_Left)
        else:
            treadingDownLeft(mars, rand_speed_Left)

        # if a > -1 and lookaround is True:
        if count == a and flag is False:
            flag = True
            rand_times = int(abs(np.random.normal(0, 2)) + 1)
            print("抬头")
            LookAround(mars, rand_times, head_Max1, head_Min1, head_Max2, head_Min2)
            sleep(1)
            mars.setHeadAngle(1, -30, 0.5)
            mars.setHeadAngle(2, 0, 0.5)

        if select_Mode > mode_Threshold1:
            treadingSitRight(mars, rand_speed_Right)
        elif select_Mode > mode_Threshold2:
            treadingStandRight(mars, rand_speed_Right)
        else:
            treadingDownRight(mars, rand_speed_Right)

        count += 1


def treadingSitInit(mars):
    mars.setLegAngle(1, 1, -10, 0.4)
    mars.setLegAngle(3, 1, -10, 0.4)
    mars.setLegAngle(1, 3, 40, 0.4)
    mars.setLegAngle(3, 3, 40, 0.4)
    sleep(0.5)

    mars.setLegAngle(2, 2, 30, 0.4)
    mars.setLegAngle(4, 2, 30, 0.4)
    mars.setLegAngle(2, 3, -90, 0.4)
    mars.setLegAngle(4, 3, -90, 0.4)
    sleep(0.5)

    mars.setLegAngle(1, 2, 0, 0.4)
    mars.setLegAngle(3, 2, 0, 0.4)
    mars.setLegAngle(1, 3, 0, 0.4)
    mars.setLegAngle(3, 3, 0, 0.4)
    sleep(0.5)

    mars.setLegAngle(2, 2, 50, 0.4)
    mars.setLegAngle(4, 2, 50, 0.4)
    mars.setLegAngle(2, 3, -90, 0.4)
    mars.setLegAngle(4, 3, -90, 0.4)

    mars.setLegAngle(1, 2, 0, 0.4)
    mars.setLegAngle(3, 2, 0, 0.4)
    mars.setLegAngle(1, 3, 0, 0.4)
    mars.setLegAngle(3, 3, 0, 0.4)
    sleep(1)


def treadingSitLeft(mars, speed):
    delay = (0.5 - speed) * 2 + 0.8
    mars.setLegAngle(1, 2, -55, speed)
    mars.setLegAngle(1, 3, 80, speed)
    mars.setLegAngle(3, 2, 0, speed)
    mars.setLegAngle(3, 3, 0, speed)
    sleep(delay)

    mars.setLegAngle(1, 2, 0, speed)
    mars.setLegAngle(1, 3, 0, speed)
    mars.setLegAngle(3, 2, 0, speed)
    mars.setLegAngle(3, 3, 0, speed)
    sleep(delay)


def treadingSitRight(mars, speed):
    delay = (0.5 - speed) * 2 + 0.8

    mars.setLegAngle(1, 2, 0, speed)
    mars.setLegAngle(1, 3, 0, speed)
    mars.setLegAngle(3, 2, -55, speed)
    mars.setLegAngle(3, 3, 80, speed)
    sleep(delay)

    mars.setLegAngle(1, 2, 0, speed)
    mars.setLegAngle(1, 3, 0, speed)
    mars.setLegAngle(3, 2, 0, speed)
    mars.setLegAngle(3, 3, 0, speed)
    sleep(delay)


def treadingStandInit(mars):
    mars.setLegAngle(1, 1, 0, 0.3)
    mars.setLegAngle(3, 1, 0, 0.3)
    mars.setLegAngle(1, 2, -60, 0.3)
    mars.setLegAngle(3, 2, -60, 0.3)
    mars.setLegAngle(1, 3, 90, 0.3)
    mars.setLegAngle(3, 3, 90, 0.3)
    mars.setLegAngle(2, 1, 0, 0.3)

    """
    mars.setLegAngle(4, 1, 0, 0.3)
    mars.setLegAngle(2, 2, 20, 0.3)
    mars.setLegAngle(4, 2, 20, 0.3)
    mars.setLegAngle(2, 3, -90, 0.3)
    mars.setLegAngle(4, 3, -90, 0.3)
    sleep(1)
    """


def treadingStandLeft(mars, speed):
    delay = (0.3 - speed) + 1
    mars.setLegAngle(1, 2, -80, speed)
    mars.setLegAngle(1, 3, 110, speed)
    mars.setLegAngle(3, 2, -60, speed)
    mars.setLegAngle(3, 3, 90, speed)
    sleep(delay)

    mars.setLegAngle(1, 2, -60, speed)
    mars.setLegAngle(1, 3, 90, speed)
    mars.setLegAngle(3, 2, -60, speed)
    mars.setLegAngle(3, 3, 90, speed)
    sleep(delay)


def treadingStandRight(mars, speed):
    delay = (0.3 - speed) + 1
    mars.setLegAngle(1, 2, -60, speed)
    mars.setLegAngle(1, 3, 90, speed)
    mars.setLegAngle(3, 2, -80, speed)
    mars.setLegAngle(3, 3, 110, speed)
    sleep(delay)

    mars.setLegAngle(1, 2, -60, speed)
    mars.setLegAngle(1, 3, 90, speed)
    mars.setLegAngle(3, 2, -60, speed)
    mars.setLegAngle(3, 3, 90, speed)
    sleep(delay)


def treadingDownInit(mars):
    mars.setLegAngle(1, 1, 0, 0.3)
    mars.setLegAngle(3, 1, 0, 0.3)
    mars.setLegAngle(1, 2, -60, 0.3)
    mars.setLegAngle(3, 2, -60, 0.3)
    mars.setLegAngle(1, 3, 90, 0.3)
    mars.setLegAngle(3, 3, 90, 0.3)

    """
    mars.setLegAngle(2, 1, 0, 0.3)
    mars.setLegAngle(4, 1, 0, 0.3)
    mars.setLegAngle(2, 2, -90, 0.3)
    mars.setLegAngle(4, 2, -90, 0.3)
    mars.setLegAngle(2, 3, -30, 0.3)
    mars.setLegAngle(4, 3, -30, 0.3)
    """

    sleep(1)


def treadingDownLeft(mars, speed):
    delay = (0.3 - speed) + 1
    mars.setLegAngle(1, 2, 50, speed)
    mars.setLegAngle(1, 3, 40, speed)
    mars.setLegAngle(3, 2, 50, speed)
    mars.setLegAngle(3, 3, 40, speed)
    sleep(delay)

    mars.setLegAngle(1, 2, 80, speed)
    mars.setLegAngle(1, 3, 20, speed)
    mars.setLegAngle(3, 2, 50, speed)
    mars.setLegAngle(3, 3, 40, speed)
    sleep(delay)
    mars.setLegAngle(1, 3, 0, 0.5)
    sleep(0.3)


def treadingDownRight(mars, speed):
    delay = (0.3 - speed) + 1
    mars.setLegAngle(1, 2, 50, speed)
    mars.setLegAngle(1, 3, 40, speed)
    mars.setLegAngle(3, 2, 50, speed)
    mars.setLegAngle(3, 3, 40, speed)
    sleep(delay)

    mars.setLegAngle(1, 2, 50, speed)
    mars.setLegAngle(1, 3, 40, speed)
    mars.setLegAngle(3, 2, 80, speed)
    mars.setLegAngle(3, 3, 20, speed)
    sleep(delay)
    mars.setLegAngle(3, 3, 0, 0.5)
    sleep(0.3)
