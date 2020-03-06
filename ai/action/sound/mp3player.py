import RPi.GPIO as GPIO
import numpy as np
import random
from ai.actionplanner import ActionPlanner as ap

angry_td = 1.2  #time delay
purr_td = 1.75
meow_td = 1
ha_td = 0.8

class MP3PlayClass:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.IOlist = [5, 6, 13, 19, 26]
        for i in range(5):
            GPIO.setup(self.IOlist[i], GPIO.OUT)
            
    '''        
    003-comfortableCat          - meow quick 003
    009-fierceCat               - meow quick 
    010-sleepingCat             - meow long
    005-happyCat                - meow long
    
    006-hurryCat                - purr

    002-angrymoreCat            - angry 
    008-painCat                 - angry

    004-pitifulCat              - ha~
    '''

    def setplayer(self, audio_Num):
        for i in range(5):
            if audio_Num & 1 == 1:
                GPIO.output(self.IOlist[i], GPIO.LOW)
            else:
                GPIO.output(self.IOlist[i], GPIO.HIGH)
            audio_Num >>= 1
        ap.sleep(0.05)
        for i in range(5):
            GPIO.output(self.IOlist[i], GPIO.HIGH)
    
    # sounds
    def angry(self, intensity = 0):   # intensity can be 0,1

        angry_mp3_ls = [2,8]
        angry_mp3_index = angry_mp3_ls[intensity]
        
        self.setplayer(angry_mp3_index)
        ap.sleep(angry_td)
        
    def purr(self, intensity = 0):  # intensity can be 0,1
        purr_mp3_index = 6
        purr_times = 1 + intensity
        
        for i in purr_times:
            self.setplayer(purr_mp3_index)
            ap.sleep(purr_td)
        
    def meow(self,intensity = 0, tp ='quick',):
        
        meow_mp3_index = []
        if tp == 'quick':
            meow_mp3_index = [9,3]
        else: # long
            meow_mp3_index = [10,5]
            
        i = int(np.random.random()*2)   # choice 2
        
        self.setplayer(meow_mp3_index[i])
        ap.sleep(meow_td)
        
    def ha(self, intensity= 0):
        ha_mp3_index = 4
        self.setplayer(ha_mp3_index)
        ap.sleep(ha_td)

'''
mp3 = MP3PlayClass()

while True:
    for i in range(10):
        ls = [3,4,10,5,6,6,6,2,8,9]
        
        #print (9)
       
        mp3.setplayer(9)
        
        
        
        ap.sleep(2)
    ap.sleep(4)

'''
    
