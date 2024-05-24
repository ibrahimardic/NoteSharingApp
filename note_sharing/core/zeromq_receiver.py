import zmq

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.bind("tcp://127.0.0.1:5555")

while True:
    # Veriyi al
    data = socket.recv_json()
    print("Received:", data)
    socket.close()
    context.term()
