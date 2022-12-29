# Communicating parties shall be represented as processes running on
# two separate computers connected via some channel.
# Note that you can develop your application by the python programming language you wish. 
# To implement the communicating parties as processes running on two separate computers
# connected via a network in a Python application, you can use the socket module.
# The socket module provides a low-level networking interface in Python,
# which allows you to create and use sockets for communicating over a network. 

# Here is an example of how you can use the socket module to create a client-server application
# in which the communicating parties are represented as processes running on two separate computers: 

import socket 

# Create a socket object 
s = socket.socket() 

# Get the local machine name 
host = socket.gethostname() 

# Set the port number 
port = 12345 

# Bind the socket to the specified host and port 
s.bind((host, port)) 

# Listen for incoming connections 
s.listen(5) 

while True: 
    # Accept a connection 
    c, addr = s.accept() 
    print("Got connection from", addr) 
    # Send a message to the client 
    c.send(b"Thank you for connecting") 
    # Close the connection 
    c.close() 
    
# On the client side, you can use the socket module to connect to the server and send and receive data: 

import socket 

# Create a socket object 
s = socket.socket() 

# Get the local machine name 
host = socket.gethostname() 

# Set the port number 
port = 12345 

# Connect to the server 
s.connect((host, port)) 

# Receive data from the server 
data = s.recv(1024) 

# Print the received data 
print(data) 

# Close the connection 
s.close() 
# This is just a basic example of how you can use the socket module to create a client-server
# application in Python.
# You can use this as a starting point and build upon it to create a more advanced network application
# for testing block ciphers in different modes of operation.




