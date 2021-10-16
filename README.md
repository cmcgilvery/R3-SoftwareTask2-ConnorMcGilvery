# R3-SoftwareTask2-ConnorMcGilvery

Input:
The program works by first taking input from the keyboard using the keyboard.read_key() method. It stores 
the input in the direction variable then compares it to w,a,s,d to see if it is a valid direction input.
If it is a valid direction input, it is sent to the server using the send() method. If it is not, it is then 
checked if it is x, the disconnect button. Then if direction is not any of these characters, direction is then 
converted to int and set to the speed variable in a try except . If speed is between 0 and 5, it is sent to the 
sever. Otherwise if speed is not in the range of 0-5 or was not an int, the while loop restarts and accepts 
input again. The send function works by converting the data (speed or direction) into its byte form and then sending 
it to the server using client.connect((HOST, PORT)) where client is the socket.

Output:
The program works by firsr taking input from the client and decoding it to a string and storing it in the data 
variable. Data is then compared to each of the direction options, w,a,s,d, where each option confirgures 
the motors in a certain way. If data is not one of the direction options, it is then compared to "disconnect"
which is the disconnect message which ends the program. Finally if data is not the disconnect message, it is 
converted to int and speed is set to it. The motor speed and configurations are then printed out. 
