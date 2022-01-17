# -*- coding: utf-8 -*-
import subprocess
from PIL import Image
import telebot
import face_detector #any face detection program here 
import os


TOKEN = "$token"

def listener(messages):
    user_base_audio = dict()
    user_base_photo = dict()
    for m in messages:
        name = str(m.from_user.id)
        if name not in user_base_audio:
            user_base_audio[name] = 0
            os.mkdir(name+str('_audio'))
        if name not in user_base_photo:
            user_base_photo[name] = 0
            os.mkdir(name+str('_photo'))

        if m.content_type == 'audio':
            file_name = name+str('_audio')+'/audio_message_'+str(user_base[name])+'.wav'
            user_base_audio[name] += 1
            s = subprocess.Popen(['ffmpeg', '-i', m.audio, '-ar', '16000', file_name])

        if m.content_type == 'photo':
            if face_detector.detect_face(m.photo):
                file_name = name+str('_photo')+'/photo_message_'+str(user_base[name])+'.jpg'
                user_base_photo[name] += 1
                with Image.open(m.photo) as im:
                    im.save(file_name, "JPEG")

if __name__ == '__main__':
     bot = telebot.TeleBot(TOKEN)
     bot.set_update_listener(listener)
     bot.polling(none_stop=True)
     while True:
         time.sleep(10)
