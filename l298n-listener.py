import RPi.GPIO as GPIO
import time

# Define board pin numbers
IN1 = 29  # Input 1
IN2 = 37  # Input 2
ENA = 31  # Enable A (PWM)

# Set the GPIO mode and configure pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

# Create a PWM object
pwm_motor = GPIO.PWM(ENA, 100)  # 100 Hz frequency

def motor_forward(speed):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    pwm_motor.start(speed)

def motor_backward(speed):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    pwm_motor.start(speed)

def motor_stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    pwm_motor.stop()

try:
    # Main loop
    while True:
        motor_forward(10)  # 50% speed
        print("Motor Forward")
        time.sleep(2)

        motor_backward(75)  # 75% speed
        print("Motor Backward")
        time.sleep(2)

except KeyboardInterrupt:
    pass

finally:
    # Cleanup
    motor_stop()
    GPIO.cleanup()
    print("Script terminated, GPIO cleanup complete.")