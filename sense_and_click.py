import mouse
import time

def click_with(click_amt,time_between):
    (x,y) = mouse.get_position()
    for i in range(click_amt):
        mouse.click("left")
        time.sleep(time_between)