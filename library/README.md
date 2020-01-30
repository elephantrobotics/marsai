<!--
Copyright (c) 2019 Elephant Robotics, Inc. All rights reserved.

Using this MarsAI source code is subject to the terms and conditions of Apache 2.0 License. Check LICENSE for more information
-->

# Pyfirmata

Pyfirmata is the API for controlling micro-controller of all 16 servos and gyro sensor. You can use the it to commnicate with each servo motor and control marscat move, run and turn. 

## API
 * `setTailAngle(servo_no, angle, speed)` : 

# da
    def setHeadAngle(self, servo_no, angle, speed): # 0x12
        data = [SET_HEAD_ANGLE]
        data += [servo_no]
        data += struct.pack("f", angle)
        data += self.getSpeedBytesData(speed)
        self.send_sysex(MARS,data)
        pass

    def setLegAngle(self, leg_no, servo_no, angle, speed): # 0x14

        data = [SET_LEG_ANGLE]
        data += [leg_no]
        data += [servo_no]
        data += struct.pack("f", angle)
        data += self.getSpeedBytesData(speed)
        self.send_sysex(MARS,data)
        pass

    def getLegAngle(self, leg_no, servo_no): #0x15
        data = [GET_LEG_ANGLE]
        data += [leg_no]
        data += [servo_no]
        self.send_sysex(MARS, data)
        self.pass_time(0.15)  # Serial SYNC

        while self.bytes_available():
            data = self.iterate()
            if data != None:
                return data       
        return -999     # error number

    def setLegCoordOffset(self, leg_no, dx, dy, dz, speed): # 0x16
        pass


    def getGyroData(self, is_rx):
        data = [GET_GYRO]
        data += [is_rx]
        
        self.send_sysex(MARS, data)
        self.pass_time(0.15)  # Serial SYNC

        while self.bytes_available():
            data = self.iterate()
            if data != None:
                return data
        return -999     # error number

    def setIniGait(self, mode, speed): # 0x20
        data = [SET_INI_GAIT]
        data += [mode]
        data += self.getSpeedBytesData(speed)
        self.send_sysex(MARS,data)
        pass

    def setCOGOffset(self, dx, dy, dz, drx, dry, drz, speed): # 0x21
        pass

    def setBalance(self): # 0x25
        data = [SET_BALANCE]
        self.send_sysex(MARS,data)
        pass

    def setRun(self, speed): #0x31
        data = [SET_RUN]
        data += self.getSpeedBytesData(speed)
        self.send_sysex(MARS, data)
        pass

    def setTurn(self, direction, speed): # 0x32
        data = [SET_TRUN]
        if direction == 0:
            data += [0]
        else:
            data += [1]
        data += self.getSpeedBytesData(speed)

        self.send_sysex(MARS, data)
        pass

    def setWalk(self, speed): # 0x30
        data = [SET_WALK]
        data += self.getSpeedBytesData(speed)
        self.send_sysex(MARS, data)

        pass

    def setStop(self):  #0x33
        data = [SET_STOP]
        self.send_sysex(MARS, data)
        pass

    def processDataList(self,received_data):
        if len(received_data) == 4:
            data_bt = bytearray(received_data)
            stu = struct.unpack("<f", data_bt)
            return stu[0]

    def getSpeedBytesData(self, speed):