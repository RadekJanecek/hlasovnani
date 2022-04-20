radio.setGroup(1)
radio.setTransmitPower(7)
radio.setTransmitSerialNumber(true)
let abeceda = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "U", "V", "W", "X", "Y", "Z"]
let pismeno = 0
let datalist = [0]
let start = false
basic.showString(abeceda[pismeno])
input.onPinPressed(TouchPin.P0, function on_pin_pressed_p0() {
    
    if (start) {
        start = false
        console.log("konec")
    } else {
        start = true
        console.log(start)
    }
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (pismeno > 0) {
        pismeno -= 1
        basic.clearScreen()
        basic.showString(abeceda[pismeno])
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (pismeno < abeceda.length) {
        pismeno += 1
        basic.clearScreen()
        basic.showString(abeceda[pismeno])
    }
    
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_event_pressed() {
    radio.sendString(abeceda[pismeno])
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    let odpoved = radio.receivedPacket(RadioPacketProperty.SerialNumber)
    if (start) {
        if (datalist.indexOf(odpoved) < 0) {
            datalist.push(odpoved)
            console.log(receivedString)
            console.log(odpoved)
        }
        
    }
    
})
