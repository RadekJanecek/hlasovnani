let abeceda = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "U", "V", "W", "X", "Y", "Z"]
let písmeno = abeceda[0]
basic.showString(písmeno)
basic.forever(function on_forever() {
    input.onButtonPressed(Button.A, function on_button_pressed_a() {
        let písmeno = abeceda[-1]
        basic.clearScreen()
        basic.showString(písmeno)
    })
    input.onButtonPressed(Button.B, function on_button_pressed_b() {
        let písmeno = abeceda[+1]
        basic.clearScreen()
        basic.showString(písmeno)
    })
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_event_pressed() {
    radio.sendString(písmeno)
})
