# Import socket module

import socket			
def Main():
    # Create a socket object
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)		

    # Define the port on which you want to connect
    port = 12345			
    # connect to the server on local computer
    s.connect(('127.0.0.1', port))

    message = "this is not a secure messaage"
    while True:
        s.send(message.encode())

        data = s.recv(1024)

        # receive data from the server and decoding to get the string.
        print ('Recived from server : ' , str(data.decode()))

        ans = input("Do you want to continue  :")
        if ans.lower() =="y":
            continue
        else:
            break

        # close the connection
    s.close()	

if __name__ == '__main__':
    Main()
