import random
import socket
import time

from datetime import datetime

#FIXME: dirty hack to import sibling modules (cause python imports do not work)
import sys
sys.path.append(".")

import ai.feature
from ai.feature import Feature
from ai import common
from vision import Vision

class VisionFeatureGenerator:

    def __init__(self):
        self.vision = Vision()
        
    def start_vision(self):
        while True:
            start_time = time.time()
            
            features = []
            #brightness = self.vision.get_brightness()
            #if brightness is not None:
            #    features.append(brightness)
            #qrcode = self.vision.get_qrcode()
            #if qrcode is not None:
            #    features.append(qrcode)
            
            obj = self.vision.get_moving_object()
            #print (obj)
            
            if obj is not None:
                features.append(obj)
            face = self.vision.get_face_recognition()
            
            #print (face)
            
            if face is not None:
                features.append(face)

            for ft in features:
                while True:
                    try:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.connect((common.HOST, common.PORT))
                        break
                    except ConnectionRefusedError:
                        time.sleep(1)
                        continue
                
                sock.sendall(bytes(ft.to_json() + "\n", "utf-8"))
                received = str(sock.recv(1024), "utf-8")
                sock.close()

            end_time = time.time()
            #if (end_time - start_time) < 0.2:
            #    time.sleep(end_time - start_time)

    def generate_vision_feature(self):
        ft = Feature()
        ft.type = ai.feature.Type.Object.value 
        ft.received_time = int((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds() * 1000)
        ft.timeout = int(random.uniform(100, 5000))
        vision_data = {}
        vision_data['type'] = int(random.uniform(1, 3)) * 10 # 10 - people, 20 - object, 30 - QR code
        vision_data['id'] = int(random.uniform(1, 20))
        vision_data['coords'] = [int(random.uniform(0, 360)), int(random.uniform(0, 240))]
        ft.data = vision_data
        return ft

    def simulate_data_flow_forever(self):
        while True:
            #FIXME: cannot put connect() outside loop ???
            #FIXME: sendall() throws exception BrokenPipeError: [Errno 32] Broken pipe
            while True:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.connect((common.HOST, common.PORT))
                    break
                except ConnectionRefusedError:
                    time.sleep(1)
                    continue
                    
            ft = self.generate_vision_feature()
            sock.sendall(bytes(ft.to_json() + "\n", "utf-8"))
            print("SEND: " + ft.to_json())
            received = str(sock.recv(1024), "utf-8")
            print("RECV: " + received)
            time.sleep(random.uniform(0.1, 2.0))
            sock.close()

if __name__ == "__main__":
    VisionFeatureGenerator().start_vision()
    #VisionFeatureGenerator().simulate_data_flow_forever()
