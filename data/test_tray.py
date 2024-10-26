import pystray
from PIL import Image
import runner

# Create an instance of runner/main_app
main_app = runner.Runner()


# Sample functions
def hello_world(args: list[str]) -> int:
    print("Hello World")
    return 0


def hi_world(args: list[str]) -> int:
    print("Hi World")
    return 0


# Register your functions with the runner
main_app.register_function("Hello World", hello_world)
main_app.register_function("Hi World", hi_world)


# When a menu item is clicked
def on_clicked(icon, item):
    menu_text = str(item)

    if menu_text == "Exit":
        icon.stop()
    else:
        main_app.run(menu_text, [])


# Load the icon image
image = Image.open("app_icon.png")

# The system tray menu
icon = pystray.Icon("Application", image, menu=pystray.Menu(
    pystray.MenuItem("Hello World", on_clicked),
    pystray.MenuItem("Hi World", on_clicked),
    pystray.Menu.SEPARATOR,
    pystray.MenuItem("Start Backup", on_clicked),
    pystray.Menu.SEPARATOR,
    pystray.MenuItem("Select Source Directory", on_clicked),
    pystray.MenuItem("Select Target Directory", on_clicked),
    pystray.Menu.SEPARATOR,
    pystray.MenuItem("Settings", on_clicked),
    pystray.Menu.SEPARATOR,
    pystray.MenuItem("Exit", on_clicked)
))

# Run the application
icon.run()
