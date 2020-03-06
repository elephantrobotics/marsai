from ai.action.movement.movements.basic import *
from ai.actionplanner import ActionPlanner as ap

speed_one = 0.6

def main(mars, times=6):
    stretchingInit(mars)
    for i in range(times):
        stretching(mars)
        #init(mars)
    stretchingEnd(mars)


def stretchingInit(mars):
    mars.setHeadAngle(1, 20, speed_one)
    mars.setHeadAngle(2, 0, speed_one)

    mars.setLegAngle(1, 1, 0, speed_one)
    mars.setLegAngle(1, 2, -20, speed_one)
    mars.setLegAngle(1, 3, 70, speed_one)

    mars.setLegAngle(2, 1, 0, speed_one)
    mars.setLegAngle(2, 2, -20, speed_one)
    mars.setLegAngle(2, 3, 70, speed_one)

    mars.setLegAngle(3, 1, 0, speed_one)
    mars.setLegAngle(3, 2, 30, speed_one)
    mars.setLegAngle(3, 3, -80, speed_one)

    mars.setLegAngle(4, 1, 0, speed_one)
    mars.setLegAngle(4, 2, 30, speed_one)
    mars.setLegAngle(4, 3, -80, speed_one)
    ap.sleep(1)

def full_stretching(mars):
    # 向前伸懒腰
    # 左前腿伸直
    mars.setLegAngle(1, 2, 80, 0.3)
    mars.setLegAngle(1, 3, -30, 0.3)
    mars.setLegAngle(2, 2, 80, 0.3)
    mars.setLegAngle(2, 3, -30, 0.3)
    ap.sleep(1)
    # 右前腿伸直

    # 前腿下压，后腿上抬，同时抬头
    mars.setLegAngle(1, 2, 80, 0.5)
    mars.setLegAngle(1, 3, 0, 0.5)
    mars.setLegAngle(2, 2, 80, 0.5)
    mars.setLegAngle(2, 3, 0, 0.5)
    ap.sleep(4)

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

def stretching(mars):
    speed_one = 0.3
    speed_two = 0.3
    
    
    # 向前伸懒腰
    # 左前腿伸直# 右前腿伸直

    mars.setLegAngle(1, 1, 20, speed_two)
    mars.setLegAngle(1, 2, 80, speed_two)
    mars.setLegAngle(1, 3, -30, speed_two)

    mars.setLegAngle(2, 1, 20, speed_two)
    mars.setLegAngle(2, 2, 80, speed_two)
    mars.setLegAngle(2, 3, -30, speed_two)
    ap.sleep(2)
    # 前腿下压，后腿上抬，同时抬头
    
    mars.setLegAngle(1, 2, 70, speed_one)
    mars.setLegAngle(1, 3, 30, speed_one)
    mars.setLegAngle(2, 2, 70, speed_one)
    mars.setLegAngle(2, 3, 30, speed_one)
    ap.sleep(1)
    mars.setLegAngle(3, 2, 30, speed_one)
    mars.setLegAngle(3, 3, -30, speed_one)
    mars.setLegAngle(4, 2, 30, speed_one)
    mars.setLegAngle(4, 3, -30, speed_one)
    # 头左右晃动,然后回到正常
    move_head_tail(mars, 4)
    
    # 向后伸懒腰
    # 前腿站立，后腿弯曲， 头回到正常

    mars.setLegAngle(1, 1, 0, speed_two)
    mars.setLegAngle(1, 2, -20, speed_two)
    mars.setLegAngle(1, 3, 50, speed_two)
    mars.setLegAngle(2, 1, 0, speed_two)
    mars.setLegAngle(2, 2, -20, speed_two)
    mars.setLegAngle(2, 3, 50, speed_two)
    ap.sleep(0.8)
    mars.setLegAngle(3, 2, 0, speed_two)
    mars.setLegAngle(4, 2, 0, speed_two)
    mars.setLegAngle(3, 3, -60, speed_two)
    mars.setLegAngle(4, 3, -60, speed_two)
    move_head_tail(mars, 2)



def stretchingEnd(mars):
    mars.setHeadAngle(1, 20, speed_one)
    mars.setHeadAngle(2, 0, speed_one)

    mars.setLegAngle(1, 1, 0, speed_one)
    mars.setLegAngle(1, 2, -20, speed_one)
    mars.setLegAngle(1, 3, 70, speed_one)
    mars.setLegAngle(2, 1, 0, speed_one)
    mars.setLegAngle(2, 2, -20, speed_one)
    mars.setLegAngle(2, 3, 70, speed_one)
    mars.setLegAngle(3, 1, 0, speed_one)
    mars.setLegAngle(3, 2, 30, speed_one)
    mars.setLegAngle(3, 3, -80, speed_one)
    mars.setLegAngle(4, 1, 0, speed_one)
    mars.setLegAngle(4, 2, 30, speed_one)
    mars.setLegAngle(4, 3, -80, speed_one)
    ap.sleep(1)
