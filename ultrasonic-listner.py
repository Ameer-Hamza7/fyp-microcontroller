import RPi.GPIO as GPIO
import time

# Define GPIO pins
# TRIG_PIN = 16
# ECHO_PIN = 32

def setup_bin(TRIG_PIN, ECHO_PIN):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)
    
def get_bin_level(TRIG_PIN, ECHO_PIN):
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(ECHO_PIN) == 0:
        start_time = time.time()

    while GPIO.input(ECHO_PIN) == 1:
        stop_time = time.time()

    elapsed_time = stop_time - start_time
    distance = (elapsed_time * 34300) / 2  # Speed of sound is 343 m/s

    return distance

def cleanup():
    GPIO.cleanup()

if __name__ == "__main__":
    try:
        setup_bin(TRIG_PIN=16, ECHO_PIN=40)
        # setup_bin(TRIG_PIN=18, ECHO_PIN=36)
        # setup_bin(TRIG_PIN=22, ECHO_PIN=38)
        # setup_bin(TRIG_PIN=24, ECHO_PIN=40)
        while True:
            distance1 = get_bin_level(TRIG_PIN=16, ECHO_PIN=40)
            # distance2 = get_bin_level(TRIG_PIN=18, ECHO_PIN=36)
            # distance3 = get_bin_level(TRIG_PIN=22, ECHO_PIN=38)
            # distance4 = get_bin_level(TRIG_PIN=24, ECHO_PIN=40)
            print(f"Distance: {distance1:.2f} cm")
            # print(f"Distance: {distance2:.2f} cm")
            # print(f"Distance: {distance3:.2f} cm")
            # print(f"Distance: {distance4:.2f} cm")
            time.sleep(1)
    except Exception as e:
        print('Error During Process : ', e)
    except KeyboardInterrupt:
        cleanup()
