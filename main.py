import pyautogui
import winsound
import time
from pynput.keyboard import Listener
import os
from playsound import playsound

folder = "C:\\Users\\sattw\\Desktop\\Screenshot"  # Create a new folder on Desktop and provide path
if not os.path.exists(folder):
    print("screenshot folder created.")
    os.mkdir(folder)

start = False
shift = False


def beep():
    freq = 500  # Set frequency to 2500Hz pp
    duration = 100  # Set duration to 1000ms == 1 second pp
    winsound.Beep(freq, duration)


def start_sound():
    playsound("start_sound_effect.mp3")


def app_off_sound():
    playsound("stop_sound.wav")


def screen_capture_sound():
    playsound("Camera_shutter.wav")


def on_press(key):
    global start, shift
    key_press = None

    try:
        shift_key = key.name
        if shift_key == 'shift_r':
            shift = True
    except:
        pass

    try:
        key_press = key.char.lower()
        key = key.vk
    except:
        pass

    if shift and key_press == 'p':
        if not start:
            print('Screenshot taker on ----')
            start_sound()
            start = True
        else:
            start = False
            print('Screen shot taker off ')
            app_off_sound()

    if start:
        if key == 192:
            img = pyautogui.screenshot()
            filename = "\\" + str(time.strftime("%H_%M_%S")) + '.png'
            img.save(folder + filename)
            screen_capture_sound()


def on_release(key):
    global shift
    try:
        shift_key = key.name
        if shift_key == 'shift_r':
            shift = False
    except:
        pass


with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
