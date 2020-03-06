import numpy as np
import time
from Parameters import *
import json

from featurequeue import *

from modelclassifier import ModelClassifier
from behaviourplanner import BehaviourPlanner
from actionplanner import ActionPlanner

MC = ModelClassifier()
BP = BehaviourPlanner()
AP = ActionPlanner()

def getRandNum(num_type=0):
    # 0 is for random
    # 1 is for normal
    if num_type == 1:
        return np.random.normal(0,1)
    else:
        return np.random.random()    # 0~1 percentage

def process_data(input_dic):
    print (input_dic)

    tc = input_dic['10']
    vc = input_dic['20']

    vs_human = input_dic['30']
    vs_obj = input_dic['40']

    vs = []

    ds = input_dic['70']
    ds = 400 # distance error, so need to clearify here

    # process vision
    if len(vs_human) != 0:
        vs = vs_human
    elif len(vs_obj) != 0:
        vs = vs_obj
    else:
        pass

    # 1st - get mode
    mode , data = MC.getMode([vs,vc,tc,ds])

    # 2nd - get behaviour
    action, data = BP.updateBehaviour(mode, data)

    # 3rd - process action 
    AP.process_action(action, data)

FeatureQueue.start_server()
time_seg_gap = 0.2

while (1):
    time_start = time.time()
    gap = -1

    ft_list = []

    data_dic = {'10':[], '20':[],'30':[],'40':[],'70':[]}

    while gap < time_seg_gap:
        gap = time.time() - time_start

        ft = FeatureQueue.feature_queue.get()
        ft_type_str = str(ft[1].type)
        if ft_type_str in data_dic:
            data_dic[ft_type_str] = ft[1].data
        ft_list.append(ft)

    process_data(data_dic)

    #time.sleep(1)
    print ("-----")

    if ft is None:
        time.sleep(0.2)
        continue

mars.stop()
