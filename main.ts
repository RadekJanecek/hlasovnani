let písmeno = 65
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (písmeno == 65) {
        
    } else {
        písmeno = písmeno - 1
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (písmeno == 90) {
        
    } else {
        písmeno = písmeno + 1
    }
    
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_event_pressed() {
    console.log(písmeno)
})
