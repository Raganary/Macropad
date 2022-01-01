# Macropad
Updated version of the scroll wheel. This program now includes mechanical keyboard switches that have volume control functions.

## Source Code
The encoder is programmed with Circuitpython for Pi Pico and uses the Adafruit_hid library. The class used from the library was the Mouse class that created functions of a mouse scrolling and clicking. Along with the Consumer control code class, this is used to allow the mechanical keyboard switches to be used as media functions. Three switches were used and the three functinos are volume increase/decrease and play/pause.

Note: code is inspired by Cornelius from One Transistor, (https://www.onetransistor.eu/2021/04/media-keys-rpi-pico-circuitpython.html), Thank you for making such a coherent guide.
