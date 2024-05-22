import speech_recognition as sr
import time
import pyautogui
from ttgLib.TextToGcode import ttg


def click(x, y):
    pyautogui.moveTo(x, y, .7)
    pyautogui.leftClick()


def double_click(x, y):
    pyautogui.moveTo(x, y, 1)
    pyautogui.doubleClick()


def speech_to_text():
    r = sr.Recognizer()
    try:
        with sr.Microphone(device_index=2) as source:
            r.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio = r.listen(source)
            MyText = r.recognize_google(audio)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")
    return MyText


def change_tab():
    pyautogui.keyDown('alt')
    time.sleep(.5)
    pyautogui.press('tab')
    time.sleep(.5)
    pyautogui.keyUp('alt')


def gcode_converter(file):
    gcode = ttg(file, 1, 0, "file", 1000).toGcode("M03 S90", "M03 S50", "G0", "G1")
    print(gcode)