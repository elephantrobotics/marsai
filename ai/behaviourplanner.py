import time
import numpy as np
import copy

import sys
sys.path.append(".")
import ai.parameters
import ai.actionplanner
import ai.energyplanner

# get/set/update/check/
# random.choice(d.keys())

class BehaviourPlanner:
    def __init__(self):
        self.energy = ai.energyplanner.EnergyClass()
        self.last_behaviour = ''
        self.last_behaviour_count = 0
        self.last_behaviour_time_spend = 0
        self.last_behaviour_time_left = 0

        self.last_time = self.get_time()

    def get_time(self):
        return time.time()

    def get_time_gap(self):
        return self.get_time() - self.last_time

    def get_time_cons(self, behaviour):
        if behaviour in ai.parameters.TIME_MIN_CONS:
            return ai.parameters.TIME_MIN_CONS[behaviour]
        else:
            return 0

    def update_last_time(self):
        self.last_time = self.get_time()

    def update_last_time_left(self):
        print (self.last_behaviour_time_left)
        self.last_behaviour_time_left -= self.get_time_gap()
        print (self.last_behaviour_time_left)
        self.update_last_time()

    def update_last_behaviour(self, this_behaviour):
        # update time left
        self.last_behaviour_time_left = self.get_time_cons(this_behaviour)

        # update behaviour count
        if self.last_behaviour == this_behaviour:
            self.last_behaviour_count +=1

        # check times
        self.check_behaviour_times()

        # udpate last behaviour to this behaviour
        self.last_behaviour = this_behaviour

    def check_behaviour_times(self):
        if self.last_behaviour_count > 10:
            print ("too many times")

    def updateBehaviour(self,input_mode, input_data):
        # 1 Pre-processBehaviour
        behaviour, processed_data = self.getBehaviourFromMode(input_mode, input_data)    # could be None
        #print ('1 initial behaviour ' + behaviour)
        #print ('processed data' + str(processed_data))

        # 2 directly use 
        if self.checkBehaviourInBehaviours(behaviour, ['relax','move','play']):
            #print ('2.1 in relax, move play')
            if self.last_behaviour_time_left > 0:
                #print ('2.11 time left ' + str(self.last_behaviour_time_left))
                self.update_last_time_left()
                behaviour = self.last_behaviour
            else:
                #print ('2.12 new behaviour ')
                self.update_last_behaviour(behaviour)
        else:
            #print ('2.2 other move')
            self.update_last_behaviour(behaviour)

        print ('3 behaviour ' + behaviour)
        print ('4 time left ' + str(self.last_behaviour_time_left))
        if self.last_behaviour_time_left <= 5:
            ai.actionplanner.ActionPlanner.need_stop = True
            ai.actionplanner.ActionPlanner.need_start = True
        print ('---')
        return behaviour,processed_data

    def setLastBehaviour(self, behaviour):
        if (self.last_behaviour == behaviour):
            self.last_behaviour_count += 1
        else:
            self.last_behaviour_count = 0

        self.last_behaviour = copy.deepcopy(behaviour)
        pass

    def getBehaviourFromMode(self, input_mode, input_data):
        _behaviour = None
        _data = input_data

        if input_mode == ai.parameters.MODELS[0]:    # ds
            _behaviour = "run_away"
        elif input_mode == ai.parameters.MODELS[1]:    #tc
            if input_data[0] == 1:
                _behaviour = "touch_head"
            elif input_data[2] == 1:
                _behaviour = "touch_jaw"
            elif input_data[4] == 1:
                _behaviour = "touch_back"
            pass
        elif input_mode == ai.parameters.MODELS[2]:    #voice
            _behaviour = self.processVoice(input_data)
        elif input_mode == ai.parameters.MODELS[3]:    #vision
            _behaviour,_data = self.processVision(input_data)
        else:
            _behaviour = self.processRandomBehaviour()

        return _behaviour, _data

    def processVoice(self,input_data):
        '''
            1. kitten
            2. mars
            3. cat
            4. mimi
            5. hello
            6. how are you
            7  be quiet
            8  look at me
            9  sit
            10 run
            11 walk
            12 turn
            13 relax
            14 stop
            15 come here
        '''
        command = input_data
        _behaviour = None

        if command == "MARS" or command == "KITTEN" or command == "CAT":     # call
            _behaviour = 'start_listen'
            pass
        elif command == "MIMI" or command == "HELLO" or command == "HOW ARE YOU":     # hello
            _behaviour = 'make_sound'
            pass
        elif command == "BE QUIET":     # be quiet
            _behaviour = 'lower_sound'
            # be quite
            pass
        elif command == "LOOK AT ME":     # look at me
            _behaviour = 'stare_at'
            # look at me
            pass
        elif command == "SIT":     # Go to your charger
            _behaviour = 'sit'
            pass
        elif command == "RUN":     # Play with me
            _behaviour = 'run'
            pass
        elif command == "WALK":     # Look at me
            _behaviour = 'walk'
            pass
        elif command == "TURN":     # Go foward/ left/ right/ stop
            _behaviour = 'turn'
            pass
        elif command == "RELAX":     # Are you sleepy?
            _behaviour = 'lie_down'
            pass
        elif command == "STOP":     # Be quiet
            _behaviour = 'stop'
            pass
        elif command == "COME HERE":     # Find your toy
            _behaviour = 'walk_towards'
            pass
        else:
            _behaviour = "lower_sound"
            pass

        return _behaviour

    def processVision(self, input_data):
        if type(input_data) != dict or len(input_data)!= 1:
            return "error process vision", 0

        command = ''
        for i in input_data:
            command = i

        _behaviour = None
        _data = None

        if command == 'human':
            _behaviour = ai.parameters.BEHAVIOURS['ita_human'][self.getRand(4,2)]
            _data = input_data[command][0][0] # coords

        elif command == 'qrcode':
            _behaviour = 'qrcode'
            _data = command[1]

        elif command == 'obj':
            obj_id = input_data[command][0]
            if obj_id == 0:    #high and teaser
                _behaviour = 'flap_obj'
            else:
                _behaviour = 'pre_attack'
            _data = input_data[command][1]    #coord

        return _behaviour,_data

    def processRandomBehaviour(self):
        _behaviour = None

        _rad = self.getRand()
        _rad_2 = self.getRand()

        if _rad > 0.15:         # relax
            if _rad_2 > 0.75:    # sit
                _behaviour = 'lie_down'
            elif _rad_2 < 0.7:    # lie_down
                _behaviour = 'sit'
            else:                # stand
                _behaviour = 'stand'

        elif _rad < 0.1:    # move
            if _rad_2 > 0.3:    # walk 
                _behaviour = 'walk'
            elif _rad_2 <0.1:
                _behaviour = 'turn'
            else:
                _behaviour = 'run'
        else:                # play 
            _behaviour = ai.parameters.BEHAVIOURS['play'][self.getRand(4,3)]

        return _behaviour

    def getRand(self, num_type = 0, _data=0):
        # 0 is for random
        # 1 is for normal
        # 4 is for choice / swtich
        if num_type == 0:
            return np.random.random()    # 0~1 percentage
        elif num_type == 1:
            return abs(np.random.normal(0,1))    # 68% in 1; 95% in 2
        elif num_type == 2:
            return np.random.normal(0,1)    # 68% in 1; 95% in 2
        elif num_type == 3:
            return np.random.gamma(1,1)        # 90% 0~2;  10% bigger than 2
        elif num_type == 4:
            return int(np.random.random()*_data)     # 0,1,2 .. data-1
        else:
            return 0

    def checkBehaviourInBehaviours(self,_behaviour, _behaviour_group):
        if type(_behaviour_group) is str: 

            if _behaviour in ai.parameters.BEHAVIOURS[_behaviour_group]:
                return True
            else:
                return False
        elif type(_behaviour_group) is list:

            for i in _behaviour_group:
                if _behaviour in ai.parameters.BEHAVIOURS[i]:
                    return True
            return False
        else:
            print ('Not in the group')
            return False
        pass
