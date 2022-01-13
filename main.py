# -*- coding: utf-8 -*-
import subprocess
import telebot
import face_detector #any face detection program here 
import os

TOKEN = "$token"

def listener(messages):
    user_base = dict()
    for m in messages:
        name = str(m.from_user.id)
        if name not in user_base:
            user_base[name] = 0
            os.mkdir(name)

        if m.content_type == 'audio':
            file_name = name+'/audio_message_'+str(user_base[name])+'.wav'
            user_base[name] += 1
            s = subprocess.Popen(['ffmpeg', '-i', m.audio, '-ar', '16000', file_name])

        if m.content_type == 'photo':
            if face_detector.detect_face():
                file_name = name+'/photo_message_'+str(user_base[name])+'.jpg'
                user_base[name] += 1
                s = subprocess.Popen(['ffmpeg', '-i', m.photo, file_name])

if __name__ == '__main__':
     bot = telebot.TeleBot(TOKEN)
     bot.set_update_listener(listener)
     bot.polling(none_stop=True)
     while True:
         time.sleep(100)
