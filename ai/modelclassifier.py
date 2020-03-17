import sys
sys.path.append(".")
import ai.parameters

class ModelClassifier:
    def __init__(self):
        self.low_power = ai.parameters.LOW_POWER_TTH
        self.times = [0, 0, 0, 0, 0]     # vision / voice / touch / distance / freemode

    def getMode(self, sensor_input):
        if len(sensor_input) != 4:
            return -1, -1

        vision   = sensor_input[0]    #{'data':,}
        voice    = sensor_input[1]    #mars
        touch    = sensor_input[2]    #[0,0,0,0,0,0]
        distance = sensor_input[3]    #number

        print("MC ---")
        print(vision)
        print(voice)
        print(touch)
        print(distance)
        print('MC ---')

        mode, data = self.modelClassfier(vision, voice, touch, distance)
        return mode, data
        #return 0,0

    def modelClassfier(self, _vision, _voice, _touch, _distance):
        mode = ''
        data = []
        update_index = 4

        if _distance < 80 and _distance > 0:
            mode = ai.parameters.MODELS[0]
            data = _distance
            update_index = 3
        elif self.getSum(_touch) > 0:
            mode = ai.parameters.MODELS[1]    # touch sensor
            data = _touch
            update_index = 2
        elif len(_voice) > 0:
            mode = ai.parameters.MODELS[2]    # voice
            data = _voice['word'] 
            update_index = 1
        elif len(_vision) > 0:
            mode = ai.parameters.MODELS[3]    # vision
            data = _vision
            update_index = 0
        else:
            mode = ai.parameters.MODELS[4]    # free move
            data = None

        # update times to check if there is something wrong
        #mode = self.updateTimes(update_index, mode)

        print('MC ---')
        print (mode)
        print (data)
        print('MC ---')

        return mode, data

    def getSum(self, data_input):
        _sum = 0
        for i in data_input:
            _sum += i
        return _sum

    def getSize(self, data_input):
        count = 0

        if type(data_input) != list:
            return 1
        else:
            for i in data_input:
                count += self.getSize(i)
        return count

    def updateTimes(self, update_index, mode):
        _mode = mode

        self.times[0] -= 7/10.0    # vision
        self.times[1] -= 7/10.0    # voice
        self.times[2] -= 7/10.0    # touch
        self.times[3] -= 7/10.0    # distance
        self.times[4] -= 1         # distance

        self.times[update_index] += 1

        for i in range(4):
            self.times[i] = max(self.times[i], 0)
            if self.times[i] > 4:
                _mode = ai.parameters.MODELS[4]            # treat it is broken ???
        return _mode

        # vision / voice / touch / distance / freemode
