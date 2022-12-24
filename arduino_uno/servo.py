import pyfirmata
from pyfirmata import util
from tkinter import *

# don't forget to change the serial port to suit
board = pyfirmata.Arduino('COM5')

# start an iterator thread so
# serial buffer doesn't overflow
iter8 = util.Iterator(board)
iter8.start()

# set up pin D9 as Servo Output
pin9 = board.get_pin('d:9:s')


def move_servo(angle):
    pin9.write(angle)


# set up GUI
root = Tk()

# draw a nice big slider for servo position
scale = Scale(root,
              command=move_servo,  # the function to invoke
              to=175,
              orient=HORIZONTAL,
              length=400,
              label='Angle')
scale.pack(anchor=CENTER)

# run Tk event loop
root.mainloop()
