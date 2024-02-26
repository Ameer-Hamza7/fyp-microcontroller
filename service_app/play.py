import json
import time
import RPi.GPIO as GPIO


CURRENT_POSITION = None
# Define board pin numbers
IN1 = 31  # Input 1
IN2 = 37  # Input 2
ENA = 33  # Enable A (PWM)

# Set the GPIO mode and configure pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

# Create a PWM object
pwm_motor = GPIO.PWM(ENA, 100)  # 100 Hz frequency

def motor_forward(speed):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    # pwm_motor.start(speed)

def motor_stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    pwm_motor.stop()
        
if __name__ == "__main__":
    try:
        # Main loop
        while True:
            with open('destination.txt', 'r') as f:
                BIN_POSITION = f.read()
                if BIN_POSITION == 'NOTHING':
                    time.sleep(2)
                    continue
                elif BIN_POSITION == 'Wet Waste':
                    time.sleep(2)
                elif BIN_POSITION == 'Dry Waste':
                    motor_forward(100) 
                    time.sleep(6.5)
                elif BIN_POSITION == 'Medical Waste':
                    motor_forward(100) 
                    time.sleep(13)
                elif BIN_POSITION == 'E Waste':
                    motor_forward(100) 
                    time.sleep(19.5)
                
    except KeyboardInterrupt:
        pass

    finally:
        # Cleanup
        motor_stop()
        GPIO.cleanup()
        print("Script terminated, GPIO cleanup complete.")
