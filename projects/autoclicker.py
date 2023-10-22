#автокликер
import keyboard
import mouse
import time

click = False

def clicker():
    global click
    click = not click

keyboard.add_hotkey('Z + X', clicker)

while True:
    if click:
        mouse.click(button='left')
        time.sleep(0.01)