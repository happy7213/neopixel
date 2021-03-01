input.onButtonPressed(Button.A, function () {
    strip.setPixelColor(range, neopixel.colors(NeoPixelColors.Black))
    strip.show()
    range += -1
    if (range < 0) {
    	
    }
    strip.setPixelColor(range, neopixel.colors(NeoPixelColors.Yellow))
    strip.show()
})
input.onButtonPressed(Button.AB, function () {
    strip.setPixelColor(range, neopixel.colors(NeoPixelColors.Black))
    strip.show()
    range += 5
    if (range >= 24) {
        range = 0
    }
    strip.setPixelColor(range, neopixel.colors(NeoPixelColors.Yellow))
    strip.show()
})
input.onButtonPressed(Button.B, function () {
    strip.setPixelColor(range, neopixel.colors(NeoPixelColors.Black))
    strip.show()
    range += 1
    if (range >= 24) {
        range = 0
    }
    strip.setPixelColor(range, neopixel.colors(NeoPixelColors.Yellow))
    strip.show()
})
let range = 0
let strip: neopixel.Strip = null
images.iconImage(IconNames.Heart).showImage(0, 400)
strip = neopixel.create(DigitalPin.P2, 24, NeoPixelMode.RGB)
range = 0
strip.clear()
basic.forever(function () {
	
})
