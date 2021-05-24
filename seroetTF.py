from pyfirmata import Arduino, util
import time

board =Arduino('/dev/cu.usbmodem14101')
acquisition = util.Iterator(board)
acquisition.start()
servo_pin = board.get_pin('d:9:s')
ser = board.get_pin('a:0:i')
def servo(angle):
    while True:
        if angle < 10:
            angle = 10
        elif angle > 170:
            angle = 170
        servo_pin.write(angle)


def getTFminiData():
    while True:
        count = ser.in_waiting
        if count > 8:
            recv =
            ser.reset_input_buffer()
            if recv[0] == 'Y' and recv[1] == 'Y':  # 0x59 is 'Y'
                low = int(recv[2].encode('hex'), 16)
                high = int(recv[3].encode('hex'), 16)
                distance = low + high * 256
                print(distance)

try :
    getTFminiData()
except :
    board.exit()
