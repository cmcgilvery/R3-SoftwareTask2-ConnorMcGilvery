import socket
import keyboard
import time

PORT = 5030 #port that the server runs on
HOST = socket.gethostbyname(socket.gethostname()) #get local ip address
speed = 10
direction = ""
validdirection = False
endprogram = False

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #create client socket
client.connect((HOST, PORT)) #connect client socket to port and host ip address

def send(input):
    data = input.encode('utf-8') #encodes data into byte form
    client.send(data) #sends data to server

while endprogram == False:
    print("Enter a digit from 0-5 to choose the speed or a,d,s,w to go left, right, backward or forward respectivly or x to exit")

    direction = keyboard.read_key()  # reads key into direction variable
    if (direction == "d") | (direction =="a") | (direction =="s") | (direction =="w") :  # determines if direction input is valid
        validdirection = True
    if keyboard.read_key() == "x":  # if x then program ends and a disconnect message is sent to the server
        send("disconnect")
        endprogram = True
    if validdirection:  # if direction input is valid, then send it to the server
        send(direction)
    else:
        try:
            speed = int(direction) #converts key pressed to int then writes it to variable speed
            if if (speed >=0) & (speed <6):  # send speed to server if valid:  # send speed to server if valid
                send(str(speed))
        except:
            print ('')

    validdirection = False



