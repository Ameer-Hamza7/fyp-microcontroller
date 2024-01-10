import RPi.GPIO as GPIO
import time

# Define the GPIO pins for the sensors
eye_pin_1 = 13
eye_pin_2 = 15

# Setup GPIO mode and configure the pins as input
GPIO.setmode(GPIO.BOARD)
GPIO.setup(eye_pin_1, GPIO.IN)
GPIO.setup(eye_pin_2, GPIO.IN)

try:
    while True:
        # Read data from sensor 1
        eye_1_value = GPIO.input(eye_pin_1)
        
        # Read data from sensor 2
        eye_2_value = GPIO.input(eye_pin_2)

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
