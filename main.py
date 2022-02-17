from pyb import delay, Pin, ADC, Timer, UART
import pyb
uart = UART(6, 115200, stop=1)
message = "123$"
inn = ''
serv_deg = ADC("X4")

pic = Pin('Y10', Pin.OUT_PP)
# p_out.high()
# p_out.low()

button = Pin('Y9', Pin.IN, Pin.PULL_UP)
# p_in.value()


M1 = Pin('X5', Pin.OUT_PP)
M2 = Pin('X6', Pin.OUT_PP)
MS = Pin('X10')
tim = Timer(4, freq = 10000)
ch = tim.channel(2, Timer.PWM, pin = MS)

def Motor(sp):
    global ch, M1, M2
    if sp < 0:
        M1.low()
        M2.high()
        sp = -sp
        print(sp)
    else:
        M2.low()
        M1.high()
    ch.pulse_width_percent(sp)

flag_start = True
speed = 0
rul = 0



while True:
    if uart.any():
        a = chr(uart.readchar())
        if a != '$':
            inn += a
            if len(inn) > 9:
                inn = ""
        else:
            if flag_start:
                if inn == "9999999":
                    flag_start = False
                    pic.high()
                    delay(500)
                    pic.low()
            else:
                message = 'B=' + str(button.value()) + '$'
                try:
                    if len(inn) == 7 and inn != '9999999':
                        speed = int(inn[:3])-200
                        rul = int(inn[3:])-1000
                        print(speed, rul)
                        Motor(30)
                except ValueError:
                    print("err")

            # print(inn)
            inn = ""
            uart.write(message)
