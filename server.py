import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("0.0.0.0", 8123))
serversocket.listen(5)

while True:

    (clientsocket, address) = serversocket.accept()
    clientsocket.send("HTTP/1.1 200\n\n<h1>Hello World!</h1>\n".encode("utf-8"))