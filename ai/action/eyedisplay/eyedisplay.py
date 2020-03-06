import cv2
import copy
import random

import action.eyedisplay.OLED_Driver as OLED

from PIL import Image, ImageDraw, ImageFont

from ai.actionplanner import ActionPlanner as ap

DEFAULT_SP = 0.01   # default speed / time seg
ENJOY_SP = 0.06

PIC_COUNT = 10
OPEN = 0
CLOSE = 9
NEARLY_OPEN = 3
NEARLY_CLOSE = 7


class EyeDisplay:
    def __init__(self, color = 'blue'):
        OLED.Device_Init()
        self.path = 'ai/action/eyedisplay/'
        
        self.color = color
        self.eye_output = []
        
        self.eye_raw = self.get_eye_image_raw()
        
        self.last_num = 0
        
        for i in range(PIC_COUNT):
            self.eye_output.append(self.get_eye_data(self.eye_raw, i+1))
            
        # initial
        self.display_eye(OPEN)
        
    def get_eye_image_raw(self):
        self.layer_eye_background   = Image.open(self.path + "eyeball/eye_background/" + self.color + ".png").convert("RGBA")
        self.layer_eye_puil         = Image.open(self.path + "eyeball/eye_pupil/" + self.color + ".png").convert("RGBA")
        self.layer_eye_ball         = Image.open(self.path + "eyeball/eye_ball.png").convert("RGBA")
        
        eye_raw = Image.new("RGBA", self.layer_eye_background.size)
        eye_raw.paste(self.layer_eye_background, (0, 0), self.layer_eye_background)
        eye_raw.paste(self.layer_eye_puil, (0, 0), self.layer_eye_puil)
        eye_raw.paste(self.layer_eye_ball, (0, 0), self.layer_eye_ball)
        
        return eye_raw
        
    def get_eye_data(self, eye_image_raw, lid_num):
        
        # input eye lid
        name_eye_lid = "eye_hor_" + str(lid_num) + ".png"
        eyelid_image =  Image.open(self.path + "eyeball/eyelid/" + name_eye_lid).convert("RGBA")

        # add lid
        eye_image_raw.paste(eyelid_image, (0,0), eyelid_image)
        
        # add mask
        layer_eye_mask = Image.open(self.path + "eyeball/mask.png").convert("RGBA")
        eye_image_raw.paste(layer_eye_mask, (0,0), layer_eye_mask)

        return OLED.get_display_data(eye_image_raw)
        
    def display_eye(self,num):      # display_eye (OPEN~CLOSE) 0 is open and ? is close
        num = min(num, CLOSE)
        num = max(num, OPEN)
        OLED.display_data(self.eye_output[num])
        self.last_num = num
        
    def display_ini(self):
        OLED.Device_Init()

    def blink(self,times = 1, timesleep = DEFAULT_SP):
        for i in range(times):
            self.eye_move_to(CLOSE, timesleep)
            self.eye_move_to(NEARLY_OPEN, timesleep)
            pass
        self.eye_move_to(OPEN, timesleep)
            
    def eye_move_to(self, dis_num, timesleep = DEFAULT_SP):
        ls = []
        if dis_num > self.last_num:
            a = self.last_num
            while a < dis_num:
                a += 1
                ls.append(a)
        elif dis_num < self.last_num:
            a = self.last_num
            while a > dis_num:
                a-=1
                ls.append(a)
        else:
            pass   
            
        self.display_eye_list(ls, timesleep)
        
        return ls
        pass
        
    def display_eye_list(self, ls , timesleep=0):
        if ls:
            sz = len(ls)
            i = 0
            while i < sz:
                self.display_eye(ls[i])
                i+=1
                ap.sleep(timesleep)
           
    def enjoy(self):
        a = random.random()
        b = random.random()
        self.eye_move_to(CLOSE, ENJOY_SP)
        
        if a > 0.35:
            self.eye_move_to(NEARLY_CLOSE, ENJOY_SP)
            self.eye_move_to(CLOSE, ENJOY_SP)
        ap.sleep(b)
        
    def random_move(self):
        a = random.random()
        sp = random.random()
        c = random.random()
        
        if a > 0.2:  # 80% will be 0 or 1
            b = int(random.random()*NEARLY_OPEN)
            self.eye_move_to(b)
        else:
            b = int(random.random()*3)
            self.blink(b)
        ap.sleep(c)



'''
a = EyeDisplay('blue')


a.enjoy()
ap.sleep(2)

while 1:
    a.random_move()
    #a.enjoy()
    ap.sleep(0.5)
    pass

'''


