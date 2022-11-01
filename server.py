import time
import zmq
import requests
import json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:

    byte_isbn = socket.recv()
    
    isbn = byte_isbn.decode('ASCII')
    print(f"Received request: {isbn}")

    api = "https://www.googleapis.com/books/v1/volumes?q=ibsn:"

    response = requests.get(api + str(isbn))

    # destructuring the JSON object from the google books API
    thumbnail_link = response.json()['items'][0]['volumeInfo']['imageLinks']['thumbnail']

    print(f"Found the following link: {thumbnail_link}")
    time.sleep(1)

    print("Returning resource link to client")
    socket.send_string(thumbnail_link)