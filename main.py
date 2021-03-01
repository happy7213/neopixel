def on_button_pressed_a():
    global range2
    strip.set_pixel_color(range2, neopixel.colors(NeoPixelColors.BLACK))
    strip.show()
    range2 += - 1
    strip.set_pixel_color(range2, neopixel.colors(NeoPixelColors.RED))
    strip.show()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global range2
    strip.set_pixel_color(range2, neopixel.colors(NeoPixelColors.BLACK))
    strip.show()
    range2 += 5
    strip.set_pixel_color(range2, neopixel.colors(NeoPixelColors.RED))
    strip.show()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global range2
    strip.set_pixel_color(range2, neopixel.colors(NeoPixelColors.BLACK))
    strip.show()
    range2 += 1
    strip.set_pixel_color(range2, neopixel.colors(NeoPixelColors.RED))
    strip.show()
input.on_button_pressed(Button.B, on_button_pressed_b)

range2 = 0
strip: neopixel.Strip = None
images.icon_image(IconNames.HEART).show_image(0, 400)
strip = neopixel.create(DigitalPin.P2, 24, NeoPixelMode.RGB)
range2 = 0
strip.clear()

def on_forever():
    pass
basic.forever(on_forever)
