import time                 # Time and such
import RPi.GPIO as GPIO     # GPIO for the Raspberry
import random               # Math module for generating random numbers.
import threading            # Module for threading as in asyncronous parallel computing.
import pygame               # Game engine for making games, but used for playing sound.

from pygame import mixer    # Import specific component from module instead of the entire package.

listnen_pin = 18 #On board
#scared = 0

#reakativa ljud
snd = ["snd1.wav","snd2.wav","snd3.wav","snd4.wav","snd5.wav","snd6.wav","snd7.wav","snd8.wav",
        "snd9.wav","snd10.wav","snd11.wav","snd12.wav","snd13.wav","snd14.wav"]
#Omgivningsljud
amb = ["amb1.wav","amb2.wav","amb3.wav","amb4.wav","amb5.wav","amb6.wav"]

# This function sets up the Raspberry and the software.
#   sertwarnings - Turns of warnings
#   setmode - Sets the RPi GPIO to either pin number at the board or the CPU.
#       It is set to the board number.
#   Setup - tells which pin does what,

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(listnen_pin, GPIO.IN)
    mixer.pre_init()
    mixer.init()
    mixer.set_num_channels(3) # Standard �tta st.

# This and the following function play the sounds.
# Both of these plays different sound based of the random number that's generated.
# 

def ambient():
    while True:
        try:
            rnd_amb = random.randint(0,5)
            #print (f'Ambient sound = {rnd_amb}\n')
            ambient_sound = mixer.Sound(f'PATH TO WHERE YOUR FILES ARE{amb[rnd_amb]}')
            ambient_sound.set_volume(0.25)
            mixer.find_channel(True).play(ambient_sound, loops=0, fade_ms=1500)
            time.sleep(360)
        except FileNotFoundError as FNF: print (f"File not found: {FNF}")
# Denna funktion spelar skr�mselljuden
def scream():
    while True:
        try:
            rnd_snd = random.randint(0,14)
            #print (f"Scare sound = {rnd_snd}\r")
            if GPIO.input(18) == GPIO.LOW:
                #print("AAAAAAAAAAAAAAAAAAAAAH!!!!!!!!!!!")
                time.sleep(0.2)
                sound = mixer.Sound(f'PATH TO WHERE YOUR FILES ARE{snd[rnd_snd]}')
                time.sleep(0.3)
                mixer.find_channel(True).play(sound)
                time.sleep(5)
            else: time.sleep(0.2);
        except FileNotFoundError as FNF: print (f"File not found: {FNF}")


# The main function start each thread and runs the setup.

def main():
    t_amb = threading.Thread(target = ambient)
    t_snd = threading.Thread(target = scream)
    setup()
    try:
        #while True:
            # scream()
            t_amb.start()
            t_snd.start()
    except KeyboardInterrupt:
        t_amb.join()
        t_snd.join()
        print(scream())
        GPIO.cleanup()


if __name__ == '__main__':
    main()
