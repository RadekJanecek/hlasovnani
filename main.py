písmeno = 65



def on_button_pressed_a():
    global písmeno
    if písmeno == 65:
        pass
    else:
        písmeno = písmeno - 1
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_button_pressed_b():
    global písmeno
    if písmeno == 90:
        pass
    else:
        písmeno = písmeno + 1
input.on_button_pressed(Button.B, on_button_pressed_b)


def on_logo_event_pressed():
    print(písmeno)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)