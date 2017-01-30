from syslog import syslog

import cfg
import motor
import time
import RPi.GPIO as GPIO # Import the GPIO Library

gear    = motor.MOTOR_GEAR1

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7

# Set the GPIO Pin mode
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

# Turn all motors off
def stop():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 0)

# Turn both motors forwards
def goForward():
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 1)
    GPIO.output(pinMotorBBackwards, 0)

# Turn both motors backwards
def goBackward():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 1)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 1)

def goLeft():
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 0)

def goRight():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 1)
    GPIO.output(pinMotorBBackwards, 0)

stop()

button_delay = 0.2

#def goForward():
    #print "move forward"
    
    #cfg.drive.forward(gear)

    
#def goBackward():
    #print "move backward"    
    #cfg.drive.backward(gear)

    
#def goRight():
    #print "move right"
    #cfg.drive.right(gear)

    
#def gosoftRight():
    #print "move soft right"
    #cfg.drive.softright(gear)

    
#def goLeft():
    #print "move left"
    #cfg.drive.left(gear)

    
#def gosoftLeft():
    #print "move soft left"
    #cfg.drive.softleft(gear)


#def stop():
    #print "move stop"
    #cfg.drive.stop()

def setGear1():
    print "move gear1"
    gear = motor.MOTOR_GEAR1
   

def setGear2():
    print "move gear2"
    gear = motor.MOTOR_GEAR2

def setGear3():
    print "move gear3"
    gear = motor.MOTOR_GEAR3

def setGear4():
    print "move gear4"
    gear = motor.MOTOR_GEAR4


handler = {cfg.FOR : goForward, cfg.BACK : goBackward, cfg.RIGHT : goRight, cfg.LEFT : goLeft, cfg.STOP : stop,\
           }


def updateRemote(command):
    
    if cfg.isRemoteSubCommand(command):
        # execute next move...
        handler[command]()
        #time.sleep(button_delay)

    else:
        # handle protocol error
        syslog("unknown subcommand")
