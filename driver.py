#!/usr/bin/env python3

import ev3dev.ev3 as ev3
import ev3dev.fonts as fonts
import time

left = ev3.LargeMotor('outB')
right = ev3.LargeMotor('outC')
sensor = ev3.ColorSensor()
button = ev3.Button()
screen = ev3.Screen()

setpoint = 16
Kp = 7

def adjust_speed(left_speed, right_speed, sensor):
    error = setpoint - sensor
    speed_change = Kp * error
    return left_speed - speed_change, right_speed + speed_change


def stop():
    left.stop()
    right.stop()
    exit()

if __name__ == "__main__":
    left_speed = 200
    right_speed = 200
    try:
        while(True):
            light = sensor.ambient_light_intensity
            new_left, new_right = adjust_speed(left_speed, right_speed, light)
            print("sensor: {}, new_left: {}, new_right: {}".format(light, new_left, new_right))
            left.run_forever(speed_sp=new_left)
            right.run_forever(speed_sp=new_right)
            time.sleep(0.2)
    finally:
        left.stop()
        right.stop()




