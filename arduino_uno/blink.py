from pyfirmata import Arduino
import time

port = 'COM5'
board = Arduino(port)
print('connected')
for x in range(10):
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)
