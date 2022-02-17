import cv2
import RobotAPI as rapi
import numpy as np
import serial
import time

port = serial.Serial("/dev/ttyS0", baudrate=115200, stopbits=serial.STOPBITS_ONE)
robot = rapi.RobotAPI(flag_serial=False)
robot.set_camera(100, 640, 480)

message = ""
ii = ""
fps = 0
fps1 = 0
fps_time = 0
state = 0
speed = 0
rul = 0
sp = 0

while 1:
    frame = robot.get_frame(wait_new_frame=1)

    fps1 += 1
    if time.time() > fps_time + 1:
        fps_time = time.time()
        fps = fps1
        fps1 = 0

    if state == 0:
        message = '9999999$'
        if ii == 'B=0':
            state = 1

    if state == 1:

        key = robot.get_key()
        sp += 1
        if key != -1:
            sp = 0
            if key == 87:
                speed = 20
            if key == 83:
                speed = -20
        if sp > 20:
            speed = 0
        message = str(speed + 200) + str(rul + 1000) + '$'



    port.write(message.encode("utf-8"))

    if port.in_waiting > 0:
        ii = ""
        t = time.time()
        while 1:
            a = str(port.read(), "utf-8")
            if a != '$':
                ii += a
            else:
                break
            if t + 0.02 < time.time():
                break
        port.reset_input_buffer()


    robot.text_to_frame(frame, 'msg = ' + message + ' ii = ' + ii + ' state = ' + str(state), 20, 20)
    robot.text_to_frame(frame, 'fps = ' + str(fps), 500, 20)

    robot.set_frame(frame, 40)