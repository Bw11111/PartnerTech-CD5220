import serial
import time
import sys
serialPort = serial.Serial(
    port="COM3", baudrate=9600, bytesize=8, timeout=0, stopbits=serial.STOPBITS_ONE
)

serialPort.write(b"!#9\r\n")

sys.exit(0)
