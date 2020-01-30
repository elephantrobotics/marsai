#!/usr/bin/python3
# coding=utf-8
import pyaudio
from os import environ, path
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
import threading
import queue
import os
import copy
import socket
import audioop

class Voice():

    def __init__(self):

        self.path = '/home/pi/marsai/voice/corpus'
        self.stream = None

        pass

    def speak_config(self):
        """
        基本设置
        :return: 一个具有特定模型的解码器
        """

        # 创建一个默认的模型
        config = Decoder.default_config()  ### 是用来配置识别的模型文件
        config.set_string('-hmm',   self.path + '/en-us')  # -hmm声音模型，声音到音标的库
        config.set_string('-lm',    self.path + '/2313.lm')  # -lm是语法库，各个词的使用频率，这个词和另一个词同时出现的几率
        config.set_string('-dict',  self.path + '/2313.dic')  # -dict是字典，音标到词(文字)的库
        config.set_string('-logfn', '/dev/null')  # 路径
        # config.set_string('-sampling_rate', '16000')
        decoder = Decoder(config)  # 将config配置文件加载到解码器上
        return decoder  # 返回一个具有特定配置解码器

    def load_word(self):
        try:
            file = open(self.path + "/corpus.txt", 'r')  # 以只读的方式打开corpus.txt文件  待修改！！！
        except FileNotFoundError:
            file = open('corpus.txt', 'r')
        name_all = file.read()  # 读取文件并存入name_all变量中
        command = []  # 实例化一个空的列表
        for i in range(15):  # 循环15次
            swp = name_all.split('\n')[i]  # 以‘\n’将name_all分割，并获取元素
            command.append(str(swp))  # 将元素转化为字符串格式，并添加到command列表中
        print(command)
        return command  # 返回command列表

    def get_speak_queue(self):
        return queue.Queue(maxsize = 1)  # 先实例化一个长度为5的队列
        
    
    def get_commands(self, speak_queues):
        if not speak_queues.empty():
            return speak_queues.get()
        return ''

    def speak_monitor(self, speak_queue, decoder, command):
        p = pyaudio.PyAudio()  # 实例化一个pyAudio()

        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)  
        """
            打开声音输出流
            format :取样值的量化格式
            channels :声道数
            rate :取样频率
            input :输入流标志，如果为True的话则开启输入流
            frames_per_buffer :底层的缓存的块的大小，底层的缓存由N个同样大小的块组成
        """
        stream.start_stream()  # 开始数据流
        in_speech_bf = False  # 定义一个标志位
        decoder.start_utt()  # 开始话语处理

        while True:  # 定义一个无限循环时刻接受音频输入
            buf = stream.read(1024, False)
            """
            stream.read(num_frames, exception_on_overflow=True) 
            从流中读取样本数据 
            num_frames 是要读取的帧数，
            exception_on_overflow 是指定输入缓冲区溢出时是否应该抛出IOError异常(或默认忽略)
            """
            if buf:  # 如果有语音产生
                decoder.process_raw(buf, False, False)  # 解码原始音频数据
                """ process_raw(buffer, size, no_search = false, full_utt = false)
                    no_search :如果非零，执行特征提取，但不做任何识别
                    full_utt :如果非零，这个数据块就是一个完整的数据语句
                """
                buf_volumn = copy.deepcopy(buf)
                rms_data = audioop.rms(buf_volumn, 2)
                db = int(rms_data/20)+10
                if decoder.get_in_speech() != in_speech_bf:
                    # decoder.get_in_speech()检查最后一个音频缓冲区是否包含语音,就是判断语音是否录制完毕
                    in_speech_bf = decoder.get_in_speech()  # 如果最后一个音频缓冲区包含语音，改变in_speech_bf的值
                    if not in_speech_bf:  # 如果in_speech_bf为False,则说明最后一个音频缓冲区不包含语音
                        decoder.end_utt()  # 结束语音处理
                        word = decoder.hyp().hypstr  # 进行语音识别处理,获取假设字符
                        if word in command:
                            commands = {'type':1, 'word':word, 'db':db}
                        else:
                            commands = {'type':2, 'word':'', 'db':db}
                        if not speak_queue.empty():
                            speak_queue.get()
                            speak_queue.task_done()
                        speak_queue.put(commands)
                        decoder.start_utt()  # 继续语音处理，循环接受语音
                        
        decoder.end_utt()  # 结束语音处理




if __name__ == '__main__':
    

    vc = Voice()
    command = []  # 实例化一个空的列表
    command = vc.load_word()  # 指令列表
    decoder = vc.speak_config()  # 一个解码器

    speak_queue = vc.get_speak_queue()

    p = threading.Thread(target=vc.speak_monitor, args=(speak_queue, decoder, command))
    # 定义一个线程，线程函数是speak_monitor，传入参数是(speak_queue, decoder, command)
    p.start()
    
    i = 0
    
    while True:
        #print ("process " + str(i))
        i += 1
        if i%10000 == 0:
            print ("process " + str(i))
            
        commands = vc.get_commands(speak_queue)
        if commands != '':
            print(commands)
    

