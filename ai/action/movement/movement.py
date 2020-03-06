import sys
import random
sys.path.append(".")

from library.pyfirmata.pyfirmata import Arduino

from ai.action.movement.movements import hug
from ai.action.movement.movements import sit
from ai.action.movement.movements import squat
from ai.action.movement.movements import liedown
from ai.action.movement.movements import objrub
from ai.action.movement.movements import playtoy
from ai.action.movement.movements import attack
from ai.action.movement.movements import touch
from ai.action.movement.movements import personrub
from ai.action.movement.movements import poweron
from ai.action.movement.movements import bury
from ai.action.movement.movements import lucky
from ai.action.movement.movements import licking
from ai.action.movement.movements import treading
from ai.action.movement.movements import stretch
from ai.action.movement.movements import basic
from ai.action.movement.movements import kneading

from ai.actionplanner import ActionPlanner as ap

class Movements:
    def __init__(self):

        dev_index = '/dev/ttyUSB0'
        self.mars = Arduino(dev_index)

        self.speed = 1

    def set_global_speed(self, speed):
        speed = max(0, speed)
        speed = min(1, speed)

        self.speed = speed
        pass

    # movability - walk/ run/ turn
    def set_walk(self, speed=-1):
        if speed == -1:
            speed = self.speed
        self.mars.setWalk(speed)

    def set_run(self, speed=-1):
        if speed == -1:
            speed = self.speed
        self.mars.setRun(speed)

    def set_turn(self, direction=1, speed=-1):
        if speed == -1:
            speed = self.speed
        self.mars.setTurn(direction, speed)

    # rest
    def set_stand(self, times = 0):
        basic.stand(self.mars,times)
    
    def set_sit(self, times = 0):
        sit.sit(self.mars, times)

    def set_squat(self, times = 0):
        pass # need to be improved
        #squat.squat(self.mars, times)

    def set_liedown(self, times = 0):
        
        liedown.lie_down(self.mars, times)

    # interaction - obj
    def set_obj_rub(self, speed=-1):
        #objrub.main(self.mars)
        pass

    def set_obj_flap(self, times = 3):  # stand
        playtoy.playToy(self.mars, times)

    def set_obj_attack(self, speed=-1):
        attack.attacking(self.mars)

    def set_obj_stare_at(self, speed=-1):
        pass

    # interaction - human
    def set_person_touch(self, position, times = 4):
        # position - head, jaw, back
        if position == 0:
            touch.touchHead(self.mars, times)
        elif position == 1:
            touch.touchJaw(self.mars, times)
        elif position == 2:
            touch.touchBody(self.mars)
        else:
            pass

    def set_person_listen(self, speed=-1):
        pass

    def set_person_stare_at(self, speed=-1):
        pass

    def set_person_rub(self, speed=-1):
        personrub.main(self.mars)

    def set_flip(self, speed=-1):
        pass

    def set_hug(self, speed=-1):
        hug.hug(self.mars)

    # play
    def set_licking(self, speed=-1):
        licking.licking(self.mars)

    def set_stretch(self, speed=-1):
        stretch.stretching(self.mars)

    def set_knead(self, speed=-1):
        kneading.kneading(self.mars)

    def set_sharpen(self, speed=-1):
        pass

    def set_bury(self, speed=-1):
        bury.main(self.mars)

    # special commands
    def set_balance_mode(self):
        self.mars.setBalance()

    def set_lucky(self, speed=-1):
        lucky.main(self.mars)

    def set_poweron(self):  # speed fixed
        poweron_list = [poweron.fullStretch, treading.main, licking.main, stretch.main, poweron.kneading]
        random.shuffle(poweron_list)
        for act in poweron_list:
            act(self.mars)

    # others commands
    def move_head_tail(self, times = 1):
        basic.move_head_tail(self.mars , times)
        # one times is 0.5 sec

    def set_stop(self):
        self.mars.setStop()

    # get commands
    def get_gyro_data(self):
        data_x = self.mars.getGyroData(1)
        data_y = self.mars.getGyroData(0)

'''
# Test
a = Movements()
while True:
    a.set_stand()
    ap.sleep(1)
    a.set_obj_attack()
    ap.sleep(2)
'''

