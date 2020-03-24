import numpy as np
import time
import json

import sys
sys.path.append(".")
import ai.featurequeue
import ai.modelclassifier
import ai.behaviourplanner
import ai.actionplanner

MC = ai.modelclassifier.ModelClassifier()
BP = ai.behaviourplanner.BehaviourPlanner()
AP = ai.actionplanner.ActionPlanner()

def process_data(input_dict):
    print (input_dict)

    tc = input_dict['10']
    vc = input_dict['20']

    vs_human = input_dict['30']
    vs_obj = input_dict['40']

    vs = []

    ds = input_dict['70']
    ds = 400 # distance error, so need to clear here

    # process vision
    if len(vs_human) != 0:
        vs = vs_human
    elif len(vs_obj) != 0:
        vs = vs_obj
    else:
        pass

    # 1st - get mode
    mode, data = MC.get_mode([vs, vc, tc, ds])

    # 2nd - get behaviour
    action, data = BP.update_behaviour(mode, data)

    # 3rd - process action
    AP.process_action(action, data)

ai.featurequeue.FeatureQueue.start_server()
time_seg_duration = 0.2
data_dict = {'10':[], '20':[],'30':[],'40':[],'70':[]}

while True:
    time_start = time.time()
    print ("MAIN -----")
    curr_period = 0

    while curr_period < time_seg_duration:
        curr_period = time.time() - time_start

        ft = ai.featurequeue.FeatureQueue.feature_queue.get()
        if ft is None:
            time.sleep(0.2)
            continue
        ft_type_str = str(ft[1].type)
        if ft_type_str in data_dict:
            data_dict[ft_type_str] = ft[1].data

    process_data(data_dict)
