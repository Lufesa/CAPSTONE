import serial
import time
ser = serial.Serial('COM5')  # open serial port
print(ser.name)         # check which port was really used
time.sleep(1)
#val = b'5,40'
#ser.write(val)     # write a string
print(ser.readline())
while True:
    val = input("Enter your value: ")
    print("sending this ", val.encode())
    ser.write(val.encode())
    time.sleep(1.5)
    while ser.inWaiting() > 0:
        print(ser.readline())
