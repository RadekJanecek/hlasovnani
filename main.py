radio.set_group(1)
radio.set_transmit_power(7)
radio.set_transmit_serial_number(True)
abeceda = ["A","B","C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "U", "V", "W", "X", "Y", "Z"]
pismeno = 0
datalist = [0]
start = False
basic.show_string(abeceda[pismeno])

def on_pin_pressed_p0():
    global start
    if start:
        start = False
        print("konec")
    else:
        start = True
        print(start)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)


def on_button_pressed_a():
    global pismeno
    if pismeno > 0:
        pismeno -= 1
        basic.clear_screen()
        basic.show_string(abeceda[pismeno])
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_button_pressed_b():
    global pismeno
    if pismeno < len(abeceda):
        pismeno += 1
        basic.clear_screen()
        basic.show_string(abeceda[pismeno])
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_event_pressed():
    radio.send_string(abeceda[pismeno])
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)

def on_received_string(receivedString):
    odpoved = radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
    if start:
        if odpoved not in datalist:
            datalist.append(odpoved)
            print(receivedString)
            print(odpoved)
radio.on_received_string(on_received_string)