import keyboard
import time

short = 0.5
long = 0.7
timeout = 260
timeout_start = time.time()
left_arrow = 'left'
right_arrow = 'right'
heal = 'grave'
while time.time() < timeout_start + timeout:

    keyboard.press(left_arrow)
    time.sleep(long)
    keyboard.press_and_release(heal)
    keyboard.release(left_arrow)
    time.sleep(short)

    keyboard.press_and_release(heal)

    keyboard.press(right_arrow)
    time.sleep(long)
    keyboard.release(right_arrow)

    keyboard.press_and_release(heal)
