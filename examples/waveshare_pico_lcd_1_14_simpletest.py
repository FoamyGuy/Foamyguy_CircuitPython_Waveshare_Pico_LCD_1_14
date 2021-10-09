# SPDX-FileCopyrightText: Copyright (c) 2021 Tim Cocks
#
# SPDX-License-Identifier: MIT

from displayio import Group, TileGrid, Bitmap, Palette
from adafruit_display_text import bitmap_label as label
import terminalio
from foamyguy_waveshare_pico_lcd_1_14 import WavesharePicoLCD114

# First set some parameters used for shapes and text
BORDER = 20
FONTSCALE = 2
BACKGROUND_COLOR = 0x00FF00  # Bright Green
FOREGROUND_COLOR = 0xAA0088  # Purple
TEXT_COLOR = 0xFFFF00

main_group = Group()

lcd = WavesharePicoLCD114()

display = lcd.display
display.show(main_group)

color_bitmap = Bitmap(display.width, display.height, 1)
color_palette = Palette(1)
color_palette[0] = BACKGROUND_COLOR

bg_sprite = TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
main_group.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = Bitmap(display.width - BORDER * 2, display.height - BORDER * 2, 1)
inner_palette = Palette(1)
inner_palette[0] = FOREGROUND_COLOR
inner_sprite = TileGrid(inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER)
main_group.append(inner_sprite)

# Draw a label
text = "Hello World"
text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
text_width = text_area.bounding_box[2] * FONTSCALE
text_group = Group(
    scale=FONTSCALE,
    x=display.width // 2 - text_width // 2,
    y=display.height // 2,
)
text_group.append(text_area)  # Subgroup for text scaling
main_group.append(text_group)

# loop forever so you can see the display
while True:
    pass
