#!/usr/bin/python3
# coding=utf-8

# Copyright (c) 2019 Elephant Robotics, Inc. All rights reserved.
# File name:    voice.py
# Author:       Leonid, Joey
# Version:      1.01
# Date:         20, Jan, 2020
# Description:  voice data
# Using this MarsAI source code is subject to the terms and conditions
# of Apache 2.0 License. Check LICENSE for more information

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

        config = Decoder.default_config()
        config.set_string('-hmm',   self.path + '/en-us')
        config.set_string('-lm',    self.path + '/2313.lm')
        config.set_string('-dict',  self.path + '/2313.dic')
        config.set_string('-logfn', '/dev/null')
        decoder = Decoder(config)
        return decoder

    def load_word(self):
        try:
            file = open(self.path + "/corpus.txt", 'r')
        except FileNotFoundError:
            file = open('corpus.txt', 'r')
        name_all = file.read()
        command = []
        for i in range(15):
            swp = name_all.split('\n')[i]
            command.append(str(swp))
        print(command)
        return command

    def get_speak_queue(self):
        return queue.Queue(maxsize=1)

    def get_commands(self, speak_queues):
        if not speak_queues.empty():
            return speak_queues.get()
        return ''

    def speak_monitor(self, speak_queue, decoder, command):
        p = pyaudio.PyAudio()

        stream = p.open(format=pyaudio.paInt16, channels=1,
                        rate=16000, input=True, frames_per_buffer=8192)

        stream.start_stream()
        in_speech_bf = False
        decoder.start_utt()

        while True:
            buf = stream.read(1024, False)

            if buf:
                decoder.process_raw(buf, False, False)

                buf_volumn = copy.deepcopy(buf)
                rms_data = audioop.rms(buf_volumn, 2)

                db = int(rms_data/20)+10
                if decoder.get_in_speech() != in_speech_bf:

                    in_speech_bf = decoder.get_in_speech()
                    if not in_speech_bf:
                        decoder.end_utt()
                        word = decoder.hyp().hypstr
                        if word in command:
                            commands = {'type': 1, 'word': word, 'db': db}
                        else:
                            commands = {'type': 2, 'word': '', 'db': db}
                        if not speak_queue.empty():
                            speak_queue.get()
                            speak_queue.task_done()
                        speak_queue.put(commands)
                        decoder.start_utt()

        decoder.end_utt()


# Test voice data
def test_voice():

    vc = Voice()
    command = []
    command = vc.load_word()
    decoder = vc.speak_config()

    speak_queue = vc.get_speak_queue()

    p = threading.Thread(target=vc.speak_monitor,
                         args=(speak_queue, decoder, command))
    p.start()

    while True:
        commands = vc.get_commands(speak_queue)
        if commands != '':
            print(commands)
