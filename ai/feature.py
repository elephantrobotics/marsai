import json
import enum

class Type(enum.Enum):
    Invalid = -1
    Unspecified = 0
    Touch = 10
    Voice = 20
    People = 30
    Object = 40
    QRCode = 50
    Battery = 60
    TOFDistance = 70
    Gyro = 80
    PowerOn = 90
    Brightness = 100

class Feature:
    def __init__(self):
        self.type = Type.Unspecified.value
        # Time this feature is received in ms
        self.received_time = 0
        # How many ms this feature makes sense
        self.timeout = 2.0
        # Custom additional data
        self.data = {}

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string.decode('utf-8'))
        feature = cls()
        feature.type = json_dict['type']
        feature.timeout = json_dict['timeout']
        feature.received_time = json_dict['received_time']
        feature.data = json_dict['data']
        return feature

    def __lt__(self, other):
        if self.type < other.type:
            return True
        elif self.type > other.type:
            return False
        if self.received_time > other.received_time:
            return True
        elif self.received_time < other.received_time:
            return False
        return False
