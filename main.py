def on_button_pressed_a():
    basic.show_icon(IconNames.HOUSE)
    basic.pause(100)
    basic.show_string("You're worth it!")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    basic.show_leds("""
        . . . . .
        . . . . .
        . # . # .
        # . . . #
        . # # # .
        """)
    basic.show_leds("""
        . . . . .
        . # . # .
        . # . # .
        # . . . #
        . # # # .
        """)
    basic.show_leds("""
        . # . # .
        . # . # .
        . # . # .
        # . . . #
        . # # # .
        """)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_pressed_ab():
    basic.show_leds("""
        # # # # #
        # . . . #
        # . # . #
        # . . . #
        # # # # #
        """)
    basic.pause(100)
    basic.clear_screen()
    basic.show_string("micro:bit" + control.device_name())
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_gesture_shake():
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        # # # # #
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . # .
        # # # # #
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . # # .
        # # # # #
        """)
    basic.show_leds("""
        . . . . .
        . # . . .
        . # # . .
        . # # # .
        # # # # #
        """)
    basic.show_leds("""
        # . . . .
        # # . . .
        # # # . .
        # # # # .
        # # # # #
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_tilt_right():
    pass
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)
