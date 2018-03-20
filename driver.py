#!/usr/bin/env python3

import ev3dev.ev3 as ev3
import ev3dev.fonts as fonts
import time

left = ev3.LargeMotor('outB')
right = ev3.LargeMotor('outC')
left_sensor = ev3.ColorSensor('in2')
right_sensor = ev3.ColorSensor('in3')
button = ev3.Button()
screen = ev3.Screen()

# light_setpoint = 0
left_speed = 200
right_speed = 200
Kp = 30.0
Kd = 10.0
Ki = 0.4
last_error = 0
ivalue = 0

def adjust_speed(left_speed, right_speed, error):
    global last_error, ivalue
    ivalue += error
    speed_change = Kp * error + (Ki * ivalue) + Kd * (error - last_error)
    print("error: {}, derivative: {}, integral: {}".format(e, Kd * (error - last_error),  Ki * ivalue))
    last_error = error
    return left_speed - speed_change, right_speed + speed_change


def stop():
    left.stop()
    right.stop()
    exit()

# if more than 0, going right from line, otherwise left
def error(left_sensor, right_sensor):
    return left_sensor - right_sensor

if __name__ == "__main__":
    try:
        while(True):
            left_light = left_sensor.ambient_light_intensity
            right_light = right_sensor.ambient_light_intensity
            e = error(left_light, right_light)
            new_left, new_right = adjust_speed(left_speed, right_speed, e)
            left.run_forever(speed_sp=new_left)
            right.run_forever(speed_sp=new_right)
    finally:
        left.stop()
        right.stop()




