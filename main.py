def on_button_pressed_a():
    basic.show_number(input.light_level())
input.on_button_pressed(Button.A, on_button_pressed_a)
