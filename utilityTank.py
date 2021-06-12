from time import sleep

# joystick

UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

Y = "Y"
X = "X"
B = "B"
A = "A"

SELECT = "select"
START = "start"

REFRESH_RATE = 0.05

# Behaviors

def turnRight():
    print('Turning Right')

def turnLeft():
    print('Turning Left')

def forward():
    print('Moving Forward')

def reverse():
    print('Moving Backward')

while(True):
    # check the d-pad
    
    # check the buttons
    
    print('checking...')
    sleep(REFRESH_RATE)