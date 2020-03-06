import random
from ai.action.movement.movements.poweron import *
from ai.action.movement.movements.basic import *
from ai.actionplanner import ActionPlanner as ap

def forerake(mars):  # -20 30
    mars.setLegAngle(1, 2, -15, 0.5)
    mars.setLegAngle(2, 2, -15, 0.5)
    mars.setLegAngle(3, 2, 25, 0.5)
    mars.setLegAngle(4, 2, 25, 0.5)
    ap.sleep(0.2)
    mars.setLegAngle(1, 2, -10, 0.5)
    mars.setLegAngle(2, 2, -10, 0.5)
    mars.setLegAngle(3, 2, 20, 0.5)
    mars.setLegAngle(4, 2, 20, 0.5)
    ap.sleep(0.2)

def retreat(mars):
    mars.setLegAngle(1, 2, -15, 0.5)
    mars.setLegAngle(2, 2, -15, 0.5)
    mars.setLegAngle(3, 2, 25, 0.5)
    mars.setLegAngle(4, 2, 25, 0.5)
    ap.sleep(0.2)
    mars.setLegAngle(1, 2, -20, 0.5)
    mars.setLegAngle(2, 2, -20, 0.5)
    mars.setLegAngle(3, 2, 30, 0.5)
    mars.setLegAngle(4, 2, 30, 0.5)
    ap.sleep(0.2)

def touchHead(mars, times=4):
    move_head_tail(mars, times)
    '''
    mars.setHeadAngle(1, get_rand_angle(20), get_rand_speed(0.2, 0.4))
    get_rand_delay_time(0.3, 0.6)
    for i in range(times):
        mars.setHeadAngle(1, get_rand_angle(0), get_rand_speed(0.4, 0.7))
        forerake(mars)
        mars.setHeadAngle(1, get_rand_angle(20), get_rand_speed(0.4, 0.7))
        retreat(mars)
    '''

def touchJaw(mars, times=3):
    move_head_tail(mars, times)

    '''
    mars.setHeadAngle(1, 20, get_rand_speed(0.8, 0.99))  # 0.2~0.4
    get_rand_delay_time(0.3, 0.6)
    for i in range(times):
        mars.setHeadAngle(1, 30, get_rand_speed(0.8, 0.99))
        forerake(mars)
        mars.setHeadAngle(1, 40, get_rand_speed(0.8, 0.99))
        retreat(mars)
    '''

def touchBody(mars, times=3):
    mars.setHeadAngle(1, -20, get_rand_speed(0.1, 0.3))
    for i in range(times):
        lookaround = random.choice(list(range(10)))
        if lookaround > 7:
            LookAround3(mars, 2)
        # 前腿半蹲
        mars.setLegAngle(1, 2, -30, get_rand_speed(0.1, 0.3))
        mars.setLegAngle(1, 3, 110, get_rand_speed(0.1, 0.3))
        mars.setLegAngle(2, 2, -30, get_rand_speed(0.1, 0.3))
        mars.setLegAngle(2, 3, 110, get_rand_speed(0.1, 0.3))
        ap.sleep(0.5)

        mars.setLegAngle(1, 3, 90, get_rand_speed(0.1, 0.3))
        mars.setLegAngle(2, 3, 90, get_rand_speed(0.1, 0.3))
        mars.setLegAngle(1, 2, -40, get_rand_speed(0.1, 0.3))
        mars.setLegAngle(2, 2, -40, get_rand_speed(0.1, 0.3))

        ap.sleep(0.5)

    mars.setHeadAngle(1, get_rand_angle(40), 0.2)
    mars.setHeadAngle(1, get_rand_angle(-20), 0.2)
    mars.setHeadAngle(2, get_rand_angle(20), 0.2)
    ap.sleep(0.5)
    mars.setHeadAngle(1, get_rand_angle(60), 0.1)
    mars.setHeadAngle(2, get_rand_angle(0), 0.1)
    ap.sleep(0.5)
    mars.setHeadAngle(1, get_rand_angle(10), 0.2)
    mars.setHeadAngle(2, get_rand_angle(0), 0.2)
    ap.sleep(0.5)

def main(mars, times, port):
    """
    :param mars:
    :param times: 次数
    :param port: 传感器接口
    :return:
    """
    pass
