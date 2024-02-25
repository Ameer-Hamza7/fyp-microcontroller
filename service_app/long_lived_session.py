import websocket
import rel
import json

def on_message(ws, message):
    try:
        message = json.loads(message)
        print(message)
        with open('mode.txt', 'w') as f:
            f.write(message['message']['mode'])
            
    except Exception as e:
        print('message ====> ', e)
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://158.220.114.235:2023/ws/devices/1/",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever(dispatcher=rel, reconnect=5)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()