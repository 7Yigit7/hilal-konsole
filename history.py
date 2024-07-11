# Yazan Chat gpt

import readline

def setup_input_history():
    histfile = ".input_history"
    try:
        readline.read_history_file(histfile)
    except FileNotFoundError:
        pass

    def save_history(histfile=histfile):
        readline.write_history_file(histfile)

    import atexit
    atexit.register(save_history)

def get_input(prompt=""):
    return input(prompt)

