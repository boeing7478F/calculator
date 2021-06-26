def on_button_pressed_a():
    global counter
    counter += 1
    basic.show_number(counter)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global _2ndnumber
    if operator == counter + _2ndnumber:
        _2ndnumber = counter + _2ndnumber
        basic.show_number(_2ndnumber)
    elif operator == counter - _2ndnumber:
        _2ndnumber = counter - _2ndnumber
        basic.show_number(_2ndnumber)
    elif operator == counter / _2ndnumber:
        pass
    elif operator == counter * _2ndnumber:
        pass
input.on_button_pressed(Button.B, on_button_pressed_b)

operator = 0
_2ndnumber = 0
counter = 0
counter = 0
_2ndnumber = 0
operator = 0

def on_forever():
    global operator
    if input.button_is_pressed(Button.AB):
        operator = counter + _2ndnumber
        basic.show_leds("""
            . . # . .
            . . # . .
            # # # # #
            . . # . .
            . . # . .
            """)
    else:
        operator = counter - _2ndnumber
        if input.button_is_pressed(Button.AB):
            basic.show_leds("""
                . . . . .
                . . . . .
                # # # # #
                . . . . .
                . . . . .
                """)
        elif input.button_is_pressed(Button.AB):
            operator = counter / _2ndnumber
            basic.show_leds("""
                . . # . .
                . . . . .
                # # # # #
                . . . . .
                . . # . .
                """)
        if input.button_is_pressed(Button.AB):
            operator = counter * _2ndnumber
            basic.show_leds("""
                # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
                """)
basic.forever(on_forever)
