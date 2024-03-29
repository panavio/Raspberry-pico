import time
import board
import digitalio

button1out = digitalio.DigitalInOut(board.GP16)
button1out.direction = digitalio.Direction.OUTPUT
button1out.value = True

green = digitalio.DigitalInOut(board.GP15)
green.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP13)
button.switch_to_input(pull=digitalio.Pull.DOWN)

while True:
    if button.value:
        print("You pressed the button!")
        green.value = True # Turn on the LED
        time.sleep(5) # wait 0.5 seconds
        green.value = False # Turn off the LED
