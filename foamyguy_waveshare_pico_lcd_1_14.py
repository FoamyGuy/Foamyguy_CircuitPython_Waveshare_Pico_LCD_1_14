# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2021 Tim Cocks for foamyguy
#
# SPDX-License-Identifier: MIT
"""
`foamyguy_waveshare_pico_lcd_1_14`
================================================================================

Helper library for WaveShare Pico LCD + Joystick + Buttons addon device.
ST7789 display 240px by 135px.


* Author(s): Tim Cocks

Implementation Notes
--------------------

**Hardware:**

  * `WaveShare Documentation <https://www.waveshare.com/wiki/Pico-LCD-1.14>`_
  * `Amazon Purchase <https://www.amazon.com/Waveshare-1-14inch-Raspberry-Interface-Embedded/dp/B08VRDF27G/>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

* Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
* Adafruit's Register library: https://github.com/adafruit/Adafruit_CircuitPython_Register
"""

# imports

__version__ = "0.0.0-auto.0"
__repo__ = (
    "https://github.com/foamyguy/Foamyguy_CircuitPython_Waveshare_Pico_LCD_1_14.git"
)

import busio
import board
import displayio
import keypad
from adafruit_st7789 import ST7789


class WavesharePicoLCD114:
    """Class representing a `WaveShare Pico LCD 1.14
    <https://www.waveshare.com/wiki/Pico-LCD-1.14>`_.

    """

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    ENTER = 4
    A = 5
    B = 6

    KEY_DICT = {
        UP: "Up",
        RIGHT: "Right",
        DOWN: "Down",
        LEFT: "Left",
        A: "A",
        B: "B",
        ENTER: "Enter",
    }

    def __init__(self, spi=None, cs=board.GP9, dc=board.GP8, reset=board.GP12):
        displayio.release_displays()
        if not spi:
            self._spi = busio.SPI(board.GP10, board.GP11)

        self._display_bus = displayio.FourWire(
            self._spi, command=dc, chip_select=cs, reset=reset
        )

        self.display = ST7789(
            self._display_bus,
            rotation=270,
            width=240,
            height=135,
            rowstart=40,
            colstart=53,
        )
        self._keys = keypad.Keys((
            board.GP2,
            board.GP20,
            board.GP18,
            board.GP16,
            board.GP3,
            board.GP15,
            board.GP17,
        ), value_when_pressed=False, pull=True)

    def key_events(self):
        event = self._keys.events.get()
        if event:
            #print(event)
            if event.pressed:
                print("{} pressed".format(self.KEY_DICT[event.key_number]))
            if event.released:
                print("{} released".format(self.KEY_DICT[event.key_number]))
