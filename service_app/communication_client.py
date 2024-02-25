import time
import json
from websocket import create_connection
import RPi.GPIO as GPIO
import time

# Define the GPIO pins for the sensors
eye_pin_1 = 13
eye_pin_2 = 15

# Setup GPIO mode and configure the pins as input

def eye_setup(pin_no):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin_no, GPIO.IN)

    return True

def see(pin_no):
    value = GPIO.input(pin_no)
    
    return value



def sensor_task():
    MACHINE_MODE = False
    
    eye_setup(pin_no=eye_pin_1)
    eye_setup(pin_no=eye_pin_2)

    try:
        while True:
            # Read data from sensor 1   
            eye_1_value = see(pin_no=eye_pin_1)
            eye_2_value = see(pin_no=eye_pin_2)
            
            with open('mode.txt', 'r') as f:
                MACHINE_MODE = f.read()
                
            print(f"Sensor 1: {eye_1_value}, Sensor 2: {eye_2_value}, Machine Mode: {MACHINE_MODE}")
                
            if (eye_1_value == 0 or eye_2_value == 0) and (MACHINE_MODE == 'halt' or MACHINE_MODE == 'release'):
                ws = create_connection("ws://158.220.114.235:2023/ws/devices/1/")
                ws.send(json.dumps({"message" : {"mode" : "scan"}}))
                print('sending scan message .............')
                
                time.sleep(5)

                MACHINE_MODE = 'scan'
            
            else:
                print('------  blaa !!!')

            time.sleep(1)

            print(f"Sensor 1: {eye_1_value}, Sensor 2: {eye_2_value}")

    except KeyboardInterrupt:
        with open('mode.txt', 'w') as f:
            f.write("halt")
        print('Terminated............')
        ws = create_connection("ws://158.220.114.235:2023/ws/devices/1/")
        ws.send(json.dumps({"message" : {"mode" : "halt"}}))
        print('sending scan message .............')
                
        time.sleep(5)

    finally:
        pass
    
if __name__ == '__main__':
    print('Executing Script .........')
    sensor_task()

    
