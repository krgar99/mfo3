import keyboard
import time

short = 0.5
long = 0.7
timeout = 260
timeout_start = time.time()

while time.time() < timeout_start + timeout:

    keyboard.press('left')
    time.sleep(long)
    keyboard.press_and_release('grave')
    keyboard.release('left')
    time.sleep(short)

    keyboard.press_and_release('grave')

    keyboard.press('right')
    time.sleep(long)
    keyboard.release('right')

    keyboard.press_and_release('grave')

    test = 0
    if test == 5:
        break
    test -= 1
