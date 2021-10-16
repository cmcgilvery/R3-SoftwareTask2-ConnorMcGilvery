# R3-SoftwareTask2-ConnorMcGilvery
The program works by first taking input from the keyboard using the keyboard.read_key() method. It stores 
the input in the direction variable then compares it to w,a,s,d to see if it is a valid direction input.
If it is a valid direction input, it is sent to the server using the send() method. If it is not, it is then 
checked if it is x, the disconnect button. Then if direction is not any of these characters, direction is then 
converted to int and set to the speed variable. 
