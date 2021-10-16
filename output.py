import socket

PORT = 5030 #port that the server runs on
SERVER = socket.gethostbyname(socket.gethostname()) #get local ip address
speed = 0

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #create server socket
server.bind((SERVER, PORT)) #connect server socket to port and host ip address
m1 = '' #motor states
m2 = ''
m3 = ''
m4 = ''
server.listen()
conn, addr = server.accept()  # recieves data from client
endprogram = False
while endprogram == False:
    data = conn.recv(16).decode('utf-8') #decodes data from byte form to string

    if data == "disconnect": #ends program if a disconnect message is recieved
        endprogram = True
    if data == "a":
        m1 = 'r'
        m2 = 'r'
        m3 = 'f'
        m4 = 'f'
    if data == "d":
        m1 = 'f'
        m2 = 'f'
        m3 = 'r'
        m4 = 'r'
    if data == "w":
        m1 = 'f'
        m2 = 'f'
        m3 = 'f'
        m4 = 'f'
    if data == "s":
        m1 = 'r'
        m2 = 'r'
        m3 = 'r'
        m4 = 'r'
    elif (endprogram == False) & (data != 'a') & (data !='d') & (data !='w') & (data !='s'):
        speed = 51*int(data) #scales speed input of 0-5 to 0-255 which represents pwm value

    print(f"[{m1}{speed}][{m2}{speed}][{m3}{speed}][{m4}{speed}]") #display motor configuration determined by speed and direction input
conn.close()





