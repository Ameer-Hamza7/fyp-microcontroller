
import RPi.GPIO as GPIO

from time import sleep

Motor2A = 31
Motor2B = 37
Motor2E = 33

GPIO.setmode(GPIO.BCM)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

print("GO forward")
GPIO.output(Motor2A,GPIO.HIGH)
GPIO.output(Motor2B,GPIO.LOW)
GPIO.output(Motor2E,GPIO.HIGH)
sleep(20)

print("Now stop")
GPIO.output(Motor2E,GPIO.LOW)
sleep(2)

print("GO backward")
GPIO.output(Motor2A,GPIO.LOW)
GPIO.output(Motor2B,GPIO.HIGH)
GPIO.output(Motor2E,GPIO.HIGH)
sleep(20)

print("Now stop")   
GPIO.output(Motor2E,GPIO.LOW)
sleep(2)

GPIO.cleanup()