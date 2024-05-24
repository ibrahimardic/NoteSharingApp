import zmq


def send_post_via_zeromq(post_data):
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    # Örnek olarak localhost'ta 5555 portunu kullanıyoruz
    socket.connect("tcp://127.0.0.1:5555")

    socket.send_json(post_data)
    socket.close()
    context.term()
