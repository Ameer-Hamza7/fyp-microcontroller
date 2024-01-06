import RPi.GPIO as GPIO
import time

# Define board pin numbers
IN1 = 11  # Input 1
IN2 = 12  # Input 2
ENA = 13  # Enable A (PWM)

# Set the GPIO mode and configure pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

# Create a PWM object
pwm_motor = GPIO.PWM(ENA, 100)  # 100 Hz frequency

def motor_forward():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    pwm_motor.start(50)  # 50% duty cycle (adjust as needed)

def motor_backward():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    pwm_motor.start(50)

def motor_stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    pwm_motor.stop()

try:
    # Main loop
    while True:
        motor_forward()
        print("Motor Forward")
        time.sleep(2)

        motor_backward()
        print("Motor Backward")
        time.sleep(2)

except KeyboardInterrupt:
    pass

finally:
    # Cleanup
    motor_stop()
    GPIO.cleanup()
    print("Script terminated, GPIO cleanup complete.")
