#program used to make rotary encoder act as a scroll wheel
import time
import digitalio
import board
import rotaryio
import usb_hid

from adafruit_hid.mouse import Mouse
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

# Rotary encoder connections to board
encoder = rotaryio.IncrementalEncoder(board.GP4, board.GP3)
button = digitalio.DigitalInOut(board.GP2)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
lastPosition = 0

#Volume increase, volume decrease, play/pause
increaseSw = digitalio.DigitalInOut(board.GP10)
increaseSw.direction = digitalio.Direction.INPUT
increaseSw.pull = digitalio.Pull.UP

decreaseSw = digitalio.DigitalInOut(board.GP11)
decreaseSw.direction = digitalio.Direction.INPUT
decreaseSw.pull = digitalio.Pull.UP

playSw = digitalio.DigitalInOut(board.GP12)
playSw.direction = digitalio.Direction.INPUT
playSw.pull = digitalio.Pull.UP

# LED flashes when a movement is made
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

# USB device
m = Mouse(usb_hid.devices)
consumer_control = ConsumerControl(usb_hid.devices)

# button delay
delay = 0.2

# loop
while True:
    # poll encoder position
    position = encoder.position
    if position != lastPosition:
        led.value = True
        if lastPosition < position:
            m.move(0,0,-1)
        else:
            m.move(0,0,1)
        lastPosition = position
        led.value = False
    
    #encoder button
    if button.value == 0:
        m.click(Mouse.LEFT_BUTTON)
        led.value = True
        time.sleep(delay)
        led.value = False
    #mechanical switch buttons
    if increaseSw.value == 0:
        consumer_control.send(ConsumerControlCode.VOLUME_INCREMENT)
        led.value = True
        time.sleep(delay)
        led.value = False
        
    if decreaseSw.value == 0:
        consumer_control.send(ConsumerControlCode.VOLUME_DECREMENT)
        led.value = True
        time.sleep(delay)
        led.value = False
        
    if playSw.value == 0:
        consumer_control.send(ConsumerControlCode.PLAY_PAUSE)
        led.value = True
        time.sleep(delay)
        led.value = False
        
    time.sleep(0.1)