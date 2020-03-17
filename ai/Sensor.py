# -*- coding: UTF-8 -*-

import numpy as np
import time

from Parameters import *


class SensorClass:
    def __init__(self):
        print "Sensor Created"

        self.battery_low_power_tth     = LOW_POWER_TTH    # low power threshold
        self.vision_get_obg_prob     = VISION_GET_OBG_PROB
        self.vision_get_human_prob     = VISION_GET_HUMAN_PROB
        self.vision_get_QR_TTH         = VISION_GET_QR_TTH

        self.voice_tth                 = VOICE_TTH

        self.touch_tth_1             = TOUCH_TTH_1
        self.touch_tth_2             = TOUCH_TTH_2

        self.distance_tth             = DISTANCE_TTH


    def getRand(self, num_type = 0):
        # 0 is for random
        # 1 is for normal
        if num_type == 0:
            return np.random.random()    # 0~1 percentage
        elif num_type == 1:
            return abs(np.random.normal(0,1))    # 68% in 1; 95% in 2
        elif num_type == 2:
            return np.random.normal(0,1)    # 68% in 1; 95% in 2
        elif num_type == 3:
            return np.random.gamma(1,1)        # 90% 0~2;  10% bigger than 2
        else:
            return 0

    def getVision(self):
        #print "Vision Function"
        def visionProcessor(_obj, _human, _qrcode):

            # obj human qrcode: 1 , 2 , 3
            
            if _obj == 0 and _human == 0 and _qrcode == 0:
                return 0

            _obj_human_qr = []

            if _qrcode:
                _obj_human_qr.append("qrcode")
                _obj_human_qr.append(_qrcode)
            elif _human:
                _obj_human_qr.append("human")
                _obj_human_qr.append(_human)
            elif _obj:
                _obj_human_qr.append("obj")
                _obj_human_qr.append(_obj)
            else:
                _obj_human_qr = 0
            return _obj_human_qr


        def getQRCode():
            qr_code = 0
            if(self.getRand() < self.vision_get_QR_TTH):
                qr_code = int(self.getRand()*9) + 1    
            return qr_code

        def getHuman():
            prob = self.vision_get_human_prob
            human_number = int(self.getRand(3)/prob) 
            size_step = 120

            human_coord = [0,0]
            if human_number != 0:
                human_coord = [size_step*self.getRand(2),size_step*self.getRand(2)]
                return human_coord
            else:
                return 0

        def getObj():
            prob = self.vision_get_obg_prob
            obj_id = int(self.getRand()*2)
            obj_number = int(self.getRand()) # 0 for high; 1 for low 
            size_step = 120

            obj_coord = [0,0]
            if obj_number != 0:
                obj_coord = [size_step*self.getRand(2),size_step*self.getRand(2)]
                return [obj_id, obj_coord]
            else:
                return 0



        def getVoiceID():
            voice_id = 0
            if(self.getRand() < self.voice_tth):
                voice_id = int(self.getRand(0) * number_of_commands) + 1    # 0 ~ 15th id
            return voice_id

        obj = getObj()
        human = getHuman()
        qrcode = getQRCode()

        obj_human_qr = visionProcessor(obj,human,qrcode)

        return [obj_human_qr]


    def getVoice(self):

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

        number_of_commands = NUMBER_OF_COMMANDS

        def getVoiceID():
            voice_id = 0
            if(self.getRand() < self.voice_tth):
                voice_id = int(self.getRand(0) * number_of_commands) + 1    # 0 ~ 15th id
            return voice_id

        voice_id = getVoiceID()
        
        return [voice_id]

    def getTouch(self):
        headJawBack = []
        if(self.getRand() < self.touch_tth_1):    # only 10% for touch
            for i in range(0,3):        # head, jaw and back signal
                if(self.getRand() < self.touch_tth_2):
                    headJawBack.append(1)
                else:
                    headJawBack.append(0)
            return headJawBack
        else:
            return [0,0,0]        # head, jaw , back

    def getDistance(self):
        distance = 1
        if(self.getRand()< self.distance_tth): # 50% is in the detect range 1m
            distance = self.getRand()    #0~100%

        return [distance]

    def getGyro(self):
        common_degree = 25
        gyro_value = [self.getRand(1)*common_degree,self.getRand(1)*common_degree,self.getRand(1)*common_degree]

        return gyro_value
