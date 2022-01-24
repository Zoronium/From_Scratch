# import socket programming library
import socket

# import thread module
from _thread import *
import threading

print_lock = threading.Lock()


temp_file = {}

perf_act = {
    'get': 'GET',
    'set': 'SET',
    'mget': 'MGET',
    'mset': 'MSET',
    'flush': 'FLUSH',
    'delete': "DELETE"
}
prfix = { # to add the working here 
    '$': handler_binary,
    '-': handler_Error,
    ':': handler_int,
    '*': handler_array,
    '%': handler_dict,
    '+': handler_string,
}

# thread function
def checking(file_recv):
	if file_recv[:2] :
		pass

def handler_protocol(file_r):
	pass

def threaded(c):
    while True:

        # data received from client
        data = c.recv(1024)
        if not data:
            print('Bye')

            # lock released on exit
            print_lock.release()
            break
            # reverse the given string from client

        # send back reversed string to client
        c.send(data)

    # connection closed
    c.close()


def Main():
    host = ""

    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:

        # establish connection with client
        c, addr = s.accept()

        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()


if __name__ == '__main__':
    Main()
