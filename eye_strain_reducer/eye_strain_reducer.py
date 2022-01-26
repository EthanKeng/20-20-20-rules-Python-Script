import pygame, sys
import subprocess
import schedule
import time
from time import localtime, strftime

# SETTINGS:
size = (1920, 1080)   # size of your screen
check_audio = 'OFF'   # with 'ON' the script doesn't turn off the screen if your audio card is busy
duration = 1200       # the time interval in seconds

def bash_command(cmd):
    subprocess.Popen(cmd, shell=True, executable='/bin/bash')

def turnoff():
    print("")

    if ( (check_audio == 'ON')) | (check_audio != 'ON'):
         print (strftime("%H:%M:%S", localtime()) + "--> OKAY!!")
         pygame.init()
         pygame.mixer.music.load('take_a_rest.mp3')
         pygame.mixer.music.play(0)
         screen = pygame.mouse.set_visible(0)
         screen = pygame.display.set_mode((size),pygame.FULLSCREEN)
         time.sleep( 20 )
         print (strftime("%H:%M:%S", localtime()) + "--> Starting...again")
         
         pygame.mixer.music.load('notification.mp3')
         pygame.mixer.music.play(0)
         while pygame.mixer.music.get_busy(): 
             pygame.time.Clock().tick(10)
         pygame.quit()       
    else:
         print (strftime("%H:%M:%S", localtime()) + "--> NO WAY!!")

schedule.every(duration).seconds.do(turnoff)
print (strftime("%H:%M:%S", localtime()) + "--> Starting...")
t=0
while True:
    schedule.run_pending()
    time.sleep(0.5)
    t=t+1
    if t%120==0:
      print(strftime("%H:%M:%S", localtime())+"-->Still running,", t/120,"minutes")
