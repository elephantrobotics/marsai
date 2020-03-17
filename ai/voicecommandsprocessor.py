import random
import time

#"consider time / sequencey / "
'''
def processVoice(self,input_data):
        '        
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
        
        command = input_data[0]
        _behaviour = None

        if command == 1 or command == 2 or command == 3:     # call
            _behaviour = 'start_listen'
            pass
        elif command == 4 or command == 5 or command == 6:     # hello
            _behaviour = 'make_sound'
            pass
        elif command == 7:     # be quiet
            _behaviour = 'lower_sound'
            # be quite
            pass
        elif command == 8:     # look at me
            _behaviour = 'stare_at'
            # look at me 
            pass
        elif command == 9:     # Go to your charger
            _behaviour = 'sit'
            pass
        elif command == 10:     # Play with me
            _behaviour = 'run'
            pass
        elif command == 11:     # Look at me
            _behaviour = 'walk'
            pass
        elif command == 12:     # Go foward/ left/ right/ stop
            _behaviour = 'turn'
            pass
        elif command == 13:     # Are you sleepy?
            _behaviour = 'lie_down'
            pass    
        elif command == 14:     # Be quiet
            _behaviour = 'stop'
            pass    
        elif command == 15:     # Find your toy
            _behaviour = 'walk_towards'
            pass    
        else:
            pass

        return _behaviour
'''
COMMANDS = ["kitten","mars","cat", "mimi","hello","how are you",
"be quiet","look at me","sit","run","walk","turn","relax","stop","come here"]

COMMANDS_START = ["kitten","mars","cat"]
COMMANDS_MAKESOUND = ["mimi","hello","how are you"]
COMMANDS_RELAX = 'relax'


class VoiceCommandProcessor:
    def __init__(self):
        print "class created "
        self.this_command = -1

        self.commands_count = 15
        self.blank_data_pro = 0.1

        self.start_to_listen = False

        self.this_time = time.time()
        self.last_time = 0

        self.time_gap_max = 1.5

    def get_randomcommand(self):
        psb = random.random()
        if psb > (1-self.blank_data_pro):
            self.clear_this_command()
        else:
            num = int (random.random() * self.commands_count)
            if num > self.commands_count-1:
                self.clear_this_command()
            self.this_command = COMMANDS[num]
        return self.this_command

    def clear_this_command(self):
        self.this_command = ' '

    def get_time_gap(self):
        # read current time
        self.this_time = time.time()
        # get gap time
        gap_time = self.this_time - self.last_time
        # refresh once
        self.last_time = self.this_time 

        return gap_time

    def process_command(self, input_command):

        time_gap = self.get_time_gap()
        print 'time gap ' + str(time_gap)

        if input_command in COMMANDS_START:
            # start to process
            self.start_to_listen = True
            return ''
        else:
            if self.start_to_listen == True: # ready to listen new command
                if time_gap < self.time_gap_max:
                    self.start_to_listen = False
                    return input_command
            self.start_to_listen = False
            return ''

a = VoiceCommandProcessor()
while 1:
    data = a.get_randomcommand()
    print '---'
    print data
    print 'output is : ' + a.process_command(data)
    print a.start_to_listen
    time.sleep(1 + random.random())