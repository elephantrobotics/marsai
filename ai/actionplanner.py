# action planner

import threading
import time
from Parameters import *
from action.movement.movement import Movements
from action.sound.mp3player import *
from action.eyedisplay.eyedisplay import *

global need_stop
need_stop = False
global need_start
need_start = True
global t
t = None

class ActionPlanner:
    def __init__(self):
        self.data = 0
        self.mars = Movements()
        self.mp3 = MP3PlayClass()
        self.screen = EyeDisplay()

    @classmethod
    def sleep(cls, delay_time=0.5):
        MIN_DELAY = 0.05
        if (delay_time <= MIN_DELAY):
            time.sleep(delay_time)
        global need_stop
        print("Action Started")
        stop_time = time.time() + delay_time
        while time.time() < stop_time:
            if need_stop:
                print("Action Aborted")
                cls.mars.set_stop()
                raise Exception("Exit exception")
            print("Action running")
            current_sleep_time = stop_time - time.time()
            if current_sleep_time > MIN_DELAY:
                time.sleep(MIN_DELAY)
            else:
                time.sleep(current_sleep_time)
        print("Action completed")

    def process_action(self, action, data=None):
        global need_stop
        global need_start
        global t
        need_stop = True
        t.join()
        if need_start:
            t = threading.Thread(target=process_action_thread,
                    args=(action, data))
            t.start()

    def process_action_thread(self, action, data=None):
        global need_start
        global need_stop
        need_start = False

        try:
            do_process_action(action, data)
        except:
            pass
        finally:
            need_start = True
            need_stop = False

    def do_process_action(self, action, data=None):
        print (action, data)

        self.screen.random_move()

        # touch
        if action == 'touch_head':
            self.mp3.meow(0,'quick')
            self.screen.blink(5)
            self.process_touch(0)

        elif action == 'touch_jaw':
            self.screen.blink(5)
            self.mp3.purr()
            self.process_touch(1)
        elif action == 'touch_back':
            self.process_touch(2)

        # vision
        elif action == 'human':
            self.mp3.meow(0,'quick')
            # make sound

        elif action == 'flap_obj':
            self.mars.set_obj_flap()

        elif action == 'pre_attack':
            self.mars.set_obj_attack()

        # move
        elif action == 'walk':
            self.mars.set_walk()

        elif action == 'run':
            self.mars.set_run()

        elif action == 'turn':
            i = int(np.random.random()*2)
            self.mars.turn(i)
            self.sleep(2)
            self.mars.set_stop()

        # relax
        elif action == 'lie_down':
            self.mars.set_liedown()
            self.mp3.meow(0,'quick')

        elif action == 'sit':
            self.mars.set_sit()

        elif action == 'stand':
            self.mars.set_stand()

        # play
        elif action == 'stretch':
            self.mars.set_stand()
            self.mars.set_stretch()
            self.mp3.meow(0,'long')

        elif action == 'knead':
            self.mars.set_knead()
            self.mp3.meow(0,'long')

        elif action == 'lick':
            self.mars.set_licking()
            self.mp3.meow(0,'quick')

        # voice
        elif action == 'make_sound':
            i = int(np.random.random()*4)
            if i == 0:
                self.mp3.meow(0,'quick')
            elif i == 1:
                self.mp3.meow(0,'slow')
            elif i == 2:
                self.mp3.purr()
            else:
                self.mp3.ha()

        elif action == 'lower_sound':
            self.mp3.ha()

        elif action == 'stare_at':
            pass

        elif action == 'walk_towards':
            self.mars.set_walk()


        elif action == 'start_listen':
            pass

        # others
        elif action == 'stop':
            self.mars.set_stop()

        elif action == "gap":
            self.mars.move_head_tail()

        else:
            pass

        self.sleep(5)

    def process_touch(self, position, data=''):
        self.mars.set_person_touch(position)

    def process_vision(self, type, data):
        pass
        # qrcode
        # rub_object
        # pre_attack
        # zhuandong - gongji

    def process_move(self, type, data):
        pass
        # run_away
        # walk / walk towards?
        # run
        # turn
        # walk_towards

    def process_relax(self, type ,data):
        pass
        # lie_down
        # sit
        # stand
        # stare_at

    def process_sounds(self, type, data):
        pass
        # make_sound
        # lower_sound


    def process_play(self,play_type,data):
        pass
        #stretch            // play
        #knead            // play
        #sharpen            // play
        #bury

    def process_stop(self):
        pass
        #sttop
