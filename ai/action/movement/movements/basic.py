from time import sleep
import numpy as np
import random

tail_off = 90
regular_sp = 0.4

def limitValue(Input_num, max_num, min_num):
    value = Input_num
    if Input_num > max_num:
        value = max_num
    elif Input_num < min_num:
        value = min_num

    return value


def stand(mars, times = 0):
    time_sleep  = 0.6
    mars.setLegAngle(1, 1, 0, 0.5)
    mars.setLegAngle(1, 2, -15, 0.5)
    mars.setLegAngle(1, 3, 56, 0.5)

    mars.setLegAngle(2, 1, 0, 0.5)
    mars.setLegAngle(2, 2, -15, 0.5)
    mars.setLegAngle(2, 3, 56, 0.5)
    move_head(mars)
    move_tail(mars)
    
    sleep(time_sleep)

    mars.setLegAngle(3, 1, 0, 0.5)
    mars.setLegAngle(3, 2, 15, 0.5)
    mars.setLegAngle(3, 3, -54, 0.5)

    mars.setLegAngle(4, 1, 0, 0.5)
    mars.setLegAngle(4, 2, 15, 0.5)
    mars.setLegAngle(4, 3, -54, 0.5)
    sleep(time_sleep)
    
    move_head_tail(mars,times)
    
    



def init(mars):
    """
    初始化状态
    :param mars:
    :return:
    """
    speed_one = 0.7
    speed_two = 0.5
    mars.setHeadAngle(1, -50, speed_one)
    sleep(1)

    mars.setLegAngle(1, 1, 0, speed_two)
    mars.setLegAngle(1, 2, -20, speed_two)
    mars.setLegAngle(1, 3, 70, speed_two)
    mars.setLegAngle(2, 1, 0, speed_two)
    mars.setLegAngle(2, 2, -20, speed_two)
    mars.setLegAngle(2, 3, 70, speed_two)
    sleep(0.5)
    mars.setLegAngle(3, 1, 0, speed_two)
    mars.setLegAngle(3, 2, 30, speed_two)
    mars.setLegAngle(3, 3, -80, speed_two)
    mars.setLegAngle(4, 1, 0, speed_two)
    mars.setLegAngle(4, 2, 30, speed_two)
    mars.setLegAngle(4, 3, -80, speed_two)
    sleep(2)

    mars.setHeadAngle(1, 20, speed_one)
    mars.setHeadAngle(2, 0, speed_one)
    sleep(0.5)


def move_head(mars, times=1, delay_time = 0):
    rand_gau = np.random.normal(0, 1)  # 68% in 1; 95% in 2
    rand_gau_2 = np.random.normal(0, 2)
    rand_speed = np.random.random() * 0.8
    rand_time = np.random.uniform(0.5, 1)

    head_1_angle = abs(rand_gau * 20) 
    head_2_angle = rand_gau_2 * 20 - 10

    head_1_angle = limitValue(head_1_angle, 30, 0)
    head_2_angle = limitValue(head_2_angle, 20, -20)

    mars.setHeadAngle(1, head_1_angle, regular_sp)
    mars.setHeadAngle(2, head_2_angle, regular_sp)

    sleep(delay_time)

      
def move_tail(mars, delay_time = 0):
    rand_1 = np.random.normal(0, 1)
    rand_2 = np.random.normal(0, 1) 
    mars.setTailAngle(1, rand_1*10, regular_sp)
    mars.setTailAngle(2, rand_2*10 + tail_off, regular_sp)
    
    sleep(delay_time)
    
def move_body(mars, delay_time = 0):
    rand_1 = np.random.uniform(-6, 6) 
    rand_sp = np.random.uniform(0.3,0.6)
    
    mars.setLegAngle(1, 1, rand_1, rand_sp)
    mars.setLegAngle(2, 1, -rand_1, rand_sp)
    mars.setLegAngle(3, 1, rand_1, rand_sp)
    mars.setLegAngle(4, 1, -rand_1, rand_sp)
    
    sleep(delay_time)

def move_head_tail(mars, times = 1, sleep_t = 1):
    for i in range(times):
        move_head(mars)
        move_tail(mars)
        sleep(sleep_t)
    
