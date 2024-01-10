from .ultrasonic_listener import setup_bin, get_bin_level
from .ir_listener import eye_setup, see
import RPi.GPIO as GPIO

def cleanup():
    GPIO.cleanup()

if __name__ == "__main__":
    setup_bin(TRIG_PIN=16, ECHO_PIN=40)
    setup_bin(TRIG_PIN=18, ECHO_PIN=32)
    setup_bin(TRIG_PIN=22, ECHO_PIN=36)
    
    bin1_chk = get_bin_level(TRIG_PIN=16, ECHO_PIN=40)
    bin2_chk = get_bin_level(TRIG_PIN=18, ECHO_PIN=32)
    bin3_chk = get_bin_level(TRIG_PIN=22, ECHO_PIN=36)
    
    if bin1_chk is not None and bin2_chk is not None and bin3_chk is not None:
        print("bin 01 status - OK \n bin 02 status - OK \n bin 03 status - OK ")
        
    eye_setup(pin_no=13)
    eye_setup(pin_no=15)

    val1 = see(pin_no=13) 
    val2 = see(pin_no=15) 

    if val1 is not None and val2:
        print("eye 01 status - OK \n eye 02 status - OK")
    
    print("Everything Works fine")
    
    cleanup()