import cv2
import RobotAPI as rapi
import numpy as np
import serial
import time

port = serial.Serial("/dev/ttyS0", baudrate=115200, stopbits=serial.STOPBITS_ONE)
robot = rapi.RobotAPI(flag_serial=False)
robot.set_camera(100, 640, 480)

lowbBlue=np.array([95,147,0])
upbBlue=np.array([105,255,255])

lowbOrange=np.array([20,70,50])
upbOrange=np.array([60,255,200])

pos = (620, 640, 200, 460)
pos2 = (0, 20, 200, 460)
pos1 = (280, 360, 420, 450)
message = ""
ii = ""
fps = 0
fps1 = 0
fps_time = 0
state = 0
speed = 0
rul = 1800
sp = 0
max1 = 0
max2 = 0
e = 0
e_old = 0
tim = time.time()
tim11 = time.time()
deg = rul
start = True
prov = False
cvet = 0
line = 0
blue = False
orange = False
timer, timer2 = 0, 0

def datchikHsv():
    global frame, orange, blue, timer, timer2

    datb1 = frame[pos1[2]:pos1[3], pos1[0]:pos1[1]]
    dat1 = cv2.GaussianBlur(datb1, (5, 5), cv2.BORDER_DEFAULT)
    hsv1 = cv2.cvtColor(dat1.copy(), cv2.COLOR_BGR2HSV)
    hsv2 = cv2.cvtColor(dat1.copy(), cv2.COLOR_BGR2HSV)
    maskdB = cv2.inRange(hsv1, lowbBlue, upbBlue)
    maskdO = cv2.inRange(hsv2, lowbOrange, upbOrange)

    _, contoursdB, _ = cv2.findContours(maskdB, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    _, contoursdO, _ = cv2.findContours(maskdO, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contorb1 in contoursdB:
        x, y, w, h = cv2.boundingRect(contorb1)
        a1 = cv2.contourArea(contorb1)
        if a1 > 500:
            blue =True
            timer2 = time.time()
            cv2.rectangle(datb1, (x, y), (x + w, y + h), (255, 0, 0), 2)




    for contorb1 in contoursdO:
        x, y, w, h = cv2.boundingRect(contorb1)
        a1 = cv2.contourArea(contorb1)

        if a1 > 500:
            orange = True
            timer = time.time()
            cv2.rectangle(datb1, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.rectangle(frame, (pos1[0], pos1[2]), (pos1[1], pos1[3]), (255, 0, 255), 2)


def datchik():
    global frame, max1, max2
    dat1b = frame[pos[2]:pos[3], pos[0]:pos[1]]
    dat1 = cv2.GaussianBlur(dat1b, (5, 5), cv2.BORDER_DEFAULT)
    grey = cv2.cvtColor(dat1, cv2.COLOR_BGR2GRAY)
    _, maskd1 = cv2.threshold(grey, 40, 255, cv2.THRESH_BINARY_INV)
    gray1 = cv2.cvtColor(maskd1, cv2.COLOR_GRAY2BGR)
    frame[pos[2]:pos[3], pos[0]:pos[1]] = gray1
    _, contoursd1, _ = cv2.findContours(maskd1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    max1 = 0

    for contorb1 in contoursd1:
        x, y, w, h = cv2.boundingRect(contorb1)
        a1 = cv2.contourArea(contorb1)
        if a1 > 200:
            if y+h > max1:
                max1 = y + h
            cv2.rectangle(dat1b, (x, y), (x + w, y + h), (0, 255, 0), 2)



    dat2b = frame[pos2[2]:pos2[3], pos2[0]:pos2[1]]
    dat2 = cv2.GaussianBlur(dat2b, (5, 5), cv2.BORDER_DEFAULT)
    grey2 = cv2.cvtColor(dat2, cv2.COLOR_BGR2GRAY)
    _, maskd2 = cv2.threshold(grey2, 40, 255, cv2.THRESH_BINARY_INV)
    gray3 = cv2.cvtColor(maskd2, cv2.COLOR_GRAY2BGR)
    frame[pos2[2]:pos2[3], pos2[0]:pos2[1]] = gray3
    _, contoursd2, _ = cv2.findContours(maskd2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    max2 = 0

    for contorb2 in contoursd2:
        x1, y1, w1, h1 = cv2.boundingRect(contorb2)
        a1 = cv2.contourArea(contorb2)
        if a1 > 200:
            if y1 + h1 > max2:
                max2 = y1 + h1
            cv2.rectangle(dat2b, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 2)

while 1:
    frame = robot.get_frame(wait_new_frame=1)
    blue = False
    orange = False
    datchik()
    datchikHsv()

    fps1 += 1
    if time.time() > fps_time + 1:
        fps_time = time.time()
        fps = fps1
        fps1 = 0

    if state == 0:
        speed = 0
        deg = rul
        if start == True:
            message = '9999999$'
        else:
            message = str(speed + 200) + str(deg + 1000) + '$'

        if ii == 'B=0' and tim + 1 < time.time():
            start = False
            state = 2
            tim = time.time()
            line = 0


    if state == 1:
        key = robot.get_key()
        sp += 1
        if key != -1:
            sp = 0
            if key == 87:
                speed = 20
            if key == 83:
                speed = -20
            if key == 68:
                rul += 50
            if key == 65:
                rul -= 50
        if sp > 10:
            speed = 0

        message = str(speed + 200) + str(rul + 1000) + '$'

    if state == 2:
        e = max2 - max1
        # if max2 == 0 or max2 == 0:
        e = 0 if max2 == 0 or max1 == 0 else 1
        u = e * 9 + (e - e_old) * 9
        e_old = e
        deg = rul - u
        speed = 30
        if blue == True:
            cvet = 1
            state = 3
        if orange == True:
            cvet = 2
            state = 3
        message = str(speed + 200) + str(deg + 1000) + '$'
        if ii == 'B=0' and tim + 1 < time.time():
            state = 0
            tim = time.time()

    if state == 3:

        if cvet == 1:
            deg = 2600
            if time.time() > timer2 + 1:
                blue = False
                line += 1
                state = 4

        if cvet == 2:
            deg = 1300
            if time.time() > timer + 1.3:
                orange = False
                line += 1
                state = 4

        if ii == 'B=0' and tim + 1 < time.time():
            state = 0
            tim = time.time()

        message = str(speed + 200) + str(deg + 1000) + '$'

    if state == 4:
        if cvet == 1:
            e = 180 - max1
            if blue == True:
                state = 3
        if cvet == 2:
            e = max2 - 180
            if orange == True:
                state = 3

        u = e * 10 + (e - e_old) * 10
        e_old = e
        deg = rul - u
        speed = 30


        if line == 12:
            tim11 = time.time()
            state = 5

        message = str(speed + 200) + str(deg + 1000) + '$'
        if ii == 'B=0' and tim + 1 < time.time():
            state = 0
            tim = time.time()

    if state == 5:
        if cvet == 1:
            e = 180 - max1
        if cvet == 2:
            e = max2 - 180

        u = e * 10 + (e - e_old) * 10
        e_old = e
        deg = rul - u
        speed = 30


        if tim11 + 1.5 < time.time():
            state = 0

        message = str(speed + 200) + str(deg + 1000) + '$'
        if ii == 'B=0' and tim + 1 < time.time():
            state = 0
            tim = time.time()


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
    # robot.text_to_frame(frame, 'fps = ' + str(fps), 0, 460)
    robot.text_to_frame(frame,
                        'msg = ' + message + ' ii = ' + ii + ' state = ' + str(state) + ' ' + str(max1) + ' ' + str(
                            max2) + ' ' + str(cvet) + '  ' + str(line), 20, 20)
    robot.set_frame(frame, 40)