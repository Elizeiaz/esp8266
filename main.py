from machine import Pin
import neopixel

import fancy

LED_COUNT = 3
pixels = neopixel.NeoPixel(Pin(4), LED_COUNT)

palette = [
    fancy.CRGB(172, 182, 229),
    fancy.CRGB(134, 253, 232),
    fancy.CRGB(172, 182, 229),
    fancy.CRGB(134, 253, 232)
]

offset = 0

if __name__ == '__main__':
    while True:
        for i in range(LED_COUNT):
            color = fancy.palette_lookup(palette, i + offset / LED_COUNT)
            color = fancy.gamma_adjust(color)
            pixels[i] = color.pack()
        pixels.write()
        offset += 0.05
