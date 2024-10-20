import pystray
from PIL import Image
import demo

# Goal: Have a system tray that executes Python functions

# Load the icon image
image = Image.open("appIcon.png")


# 1. Function repertoire
def hello_world():
    print("Hello World")

# todo running code from a different file doesn't work. Will try with a different demo file
def popup_demo():
    demo.run()
    print("Popup")


def hi_world():
    print("Hi World")


# 2. Menu that contains action
def on_clicked(icon, item):
    # Dictionary of references to functions
    actions = {
        "Hello World": hello_world,
        "Popup Demo": popup_demo,
        "Hi World": hi_world,
        "Exit": icon.stop
    }

    # Execute the action selected
    actions[str(item)]()


# The system tray menu
icon = pystray.Icon("Application", image, menu=pystray.Menu(
    pystray.MenuItem("Hello World", on_clicked),
    pystray.MenuItem("Popup Demo", on_clicked),
    pystray.MenuItem("Hi World", on_clicked),
    pystray.Menu.SEPARATOR,
    pystray.MenuItem("Exit", on_clicked)
    ))

# Run the application
icon.run()
