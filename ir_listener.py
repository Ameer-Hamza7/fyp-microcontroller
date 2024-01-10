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

eye_setup(pin_no=eye_pin_1)
eye_setup(pin_no=eye_pin_2)

try:
    while True:
        # Read data from sensor 1
        eye_1_value = see(pin_no=eye_pin_1)
        eye_2_value = see(pin_no=eye_pin_2)

        # Print the sensor values
        print(f"Sensor 1: {eye_1_value}, Sensor 2: {eye_2_value}")

        # Wait for a short duration before reading again
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    GPIO.cleanup()

finally:
    # Clean up GPIO on program exit
    GPIO.cleanup()
