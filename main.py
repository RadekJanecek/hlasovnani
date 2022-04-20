abeceda = ["A","B","C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "U", "V", "W", "X", "Y", "Z"]
písmeno = abeceda[0]
basic.show_string(písmeno)
def on_forever():
    
    def on_button_pressed_a():
        písmeno = abeceda[-1]
        basic.clear_screen()
        basic.show_string(písmeno)
    input.on_button_pressed(Button.A, on_button_pressed_a)
    def on_button_pressed_b():
        písmeno = abeceda[+1]
        basic.clear_screen()
        basic.show_string(písmeno)
    input.on_button_pressed(Button.B, on_button_pressed_b)
basic.forever(on_forever)

def on_logo_event_pressed():
    radio.send_string(písmeno)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)
