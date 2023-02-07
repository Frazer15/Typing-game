import keyboard


def key_function(yek):
    letter_input = keyboard.read_key()
    if letter_input == yek:
        pass
    else:
        return "you failed"

