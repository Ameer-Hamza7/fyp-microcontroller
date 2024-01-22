import websocket
import _thread
import time
import rel
from ultrasonic_listener import get_bin_level, setup_bin, cleanup

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")

def send_websocket_message(ws, distance1, distance2, distance3):
    message = {
        "distance1": distance1,
        "distance2": distance2,
        "distance3": distance3,
    }

    ws.send(str(message))

if __name__ == "__main__":

    try:
        
        setup_bin(TRIG_PIN=16, ECHO_PIN=40)
        setup_bin(TRIG_PIN=18, ECHO_PIN=32)
        setup_bin(TRIG_PIN=22, ECHO_PIN=36)
        # setup_bin(TRIG_PIN=24, ECHO_PIN=38)

        host_ip = input("Enter Host IP: ")
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(f"http://{host_ip}:2023/devices/5/",
                                  on_open=on_open,
                                  on_message=on_message,
                                  on_error=on_error,
                                  on_close=on_close)

        while True:
            distance1 = get_bin_level(TRIG_PIN=16, ECHO_PIN=40)
            distance2 = get_bin_level(TRIG_PIN=18, ECHO_PIN=32)
            distance3 = get_bin_level(TRIG_PIN=22, ECHO_PIN=36)
            # distance4 = get_bin_level(TRIG_PIN=24, ECHO_PIN=38)
            
            print(f"Distance: {distance1:.2f} cm")
            print(f"Distance: {distance2:.2f} cm")
            print(f"Distance: {distance3:.2f} cm")
            # print(f"Distance: {distance4:.2f} cm")
            print('=============================')
            
            # Send WebSocket message
            send_websocket_message(ws, distance1, distance2, distance3)
            
            time.sleep(5)
            
    except Exception as e:
        print('Error During Process : ', e)
    except KeyboardInterrupt:
        cleanup()
