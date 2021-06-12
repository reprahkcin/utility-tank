#!/usr/bin/python
from evdev import InputDevice, categorize, ecodes
from PCA9685 import PCA9685
from time import sleep

gamepad = InputDevice('/dev/input/event0')

print(gamepad)

Dir = [
    'forward',
    'backward'
]

pwm = PCA9685(0x40, debug=False)
pwm.setPWMFreq(50)

class MotorDriver():
    def __init__(self):
        self.PWMA = 0
        self.AIN1 = 1
        self.AIN2 = 2
        self.PWMB = 5
        self.BIN1 = 3
        self.BIN2 = 4

    def MotorRun(self, motor, index, speed):
        if speed > 100:
            return
        if(motor == 0):
            pwm.setDutycycle(self.PWMA, speed)
            if(index == Dir[0]):
                print ("1")
                pwm.setLevel(self.AIN1, 0)
                pwm.setLevel(self.AIN2, 1)
            else:
                print ("2")
                pwm.setLevel(self.AIN1, 1)
                pwm.setLevel(self.AIN2, 0)
        else:
            pwm.setDutycycle(self.PWMB, speed)
            if(index == Dir[0]):
                print ("3")
                pwm.setLevel(self.BIN1, 0)
                pwm.setLevel(self.BIN2, 1)
            else:
                print ("4")
                pwm.setLevel(self.BIN1, 1)
                pwm.setLevel(self.BIN2, 0)

    def MotorStop(self, motor):
        if (motor == 0):
            pwm.setDutycycle(self.PWMA, 0)
        else:
            pwm.setDutycycle(self.PWMB, 0)

print("this is a motor driver test code")
Motor = MotorDriver()

def moveForward():
    print("forward")
    Motor.MotorRun(0, 'forward', 100)
    Motor.MotorRun(1, 'forward', 100)


def moveBackward():
    print("backward")
    Motor.MotorRun(0, 'backward', 100)
    Motor.MotorRun(1, 'backward', 100)
    

def turnRight():
    print("turning right")
    Motor.MotorRun(1, 'forward', 100)
    

def turnLeft():
    print("turning left")
    Motor.MotorRun(0, 'forward', 100)

def stop():
    print("stop")
    Motor.MotorStop(0)
    Motor.MotorStop(1)
    
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        print(event)
    elif event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        
        if absevent.event.code == 1 and absevent.event.value == 0:
            moveForward()
        elif absevent.event.code == 1 and absevent.event.value == 255:
            moveBackward()
        elif absevent.event.code == 1 and absevent.event.value == 128:
            stop()
            
        if absevent.event.code == 0 and absevent.event.value == 0:
            turnLeft()
        elif absevent.event.code == 0 and absevent.event.value == 255:
            turnRight()
        elif absevent.event.code == 0 and absevent.event.value == 128:
            stop()
        print(ecodes.bytype[absevent.event.type][absevent.event.code], absevent.event.value)