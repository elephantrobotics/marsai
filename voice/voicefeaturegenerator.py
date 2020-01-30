import random
import socket
import time
import queue
import threading

from datetime import datetime

#FIXME: dirty hack to import sibling modules (cause python imports do not work)
import sys
sys.path.append(".")

from ai.feature import Feature
from ai import common
from voice import Voice

class VoiceFeatureGenerator:
    def __init__(self):
        self.vc = Voice()
        command = []  # 实例化一个空的列表
        command = self.vc.load_word()  # 指令列表
        decoder = self.vc.speak_config()  # 一个解码器
        self.speak_queue = self.vc.get_speak_queue()
        p = threading.Thread(target=self.vc.speak_monitor, args=(self.speak_queue, decoder, command))
        # 定义一个线程，线程函数是speak_monitor，传入参数是(speak_queue, decoder, command)
        p.start()
		
    def generate_voice_feature(self):
        ft = Feature()
        ft.type = 20
        ft.received_time = int((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds() * 1000)
        ft.timeout = int(random.uniform(100, 5000))
   
        try:
            #pass
            voice_data = self.speak_queue.get(block=False)
        except:
            return None

        if voice_data['word'] == "WALK":
            return None
            
        if voice_data['word'] == '':
            return None
            
            
        if ft is not None:
            ft.data = voice_data
        return ft
        

    def simulate_data_flow_forever(self):
        while True:
            
            ft = self.generate_voice_feature()
            if ft is not None:
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
                            
                sock.sendall(bytes(ft.to_json() + "\n", "utf-8"))
                print("SEND: " + ft.to_json())
                received = str(sock.recv(1024), "utf-8")
                #print("RECV: " + received)
                sock.close()

if __name__ == "__main__":

    VoiceFeatureGenerator().simulate_data_flow_forever()
    voiceft = VoiceFeatureGenerator()
    #voiceft.simulate_data_flow_forever()
    
    '''
    while True:
        
        ft = voiceft.generate_voice_feature()
        if ft is not None:
            if ft.data['word'] != '':
                print(ft)
    '''
    
