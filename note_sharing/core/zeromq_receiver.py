# zeromq_receiver.py
import zmq

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.bind("tcp://127.0.0.1:5555")

try:
    while True:
        # Veriyi al
        data = socket.recv_json()
        print("Received:", data)
except KeyboardInterrupt:
    pass
finally:
    socket.close()
    context.term()
