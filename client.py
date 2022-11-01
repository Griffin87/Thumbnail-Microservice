import zmq

context = zmq.Context()

print("Connecting to CS361 Server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Hyperion, Guermante's Way, Fluent Python
isbn_list = ["0553283685", "0143039229", "1491946008"]

for isbn in isbn_list:
    print(f"Sending message {isbn}")
    socket.send_string(isbn)

    byte_link = socket.recv()

    # links are returned in bytes and must be decoded
    working_link = byte_link.decode('ASCII')
    print(f"Received the following thumbnail link: {working_link}")