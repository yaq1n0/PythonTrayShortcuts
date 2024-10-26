
import logging
import pystray
from PIL import Image
from lib.runner import Runner


logger = logging.getLogger(__name__)

runner : Runner = Runner(logger) # pass primary logger

icon = Image.open("lib/resources/icon.png")

def onClick(_app : pystray.Icon, item : pystray.MenuItem) -> object: return runner.run(item.text, [])

def quit(app : pystray.Icon, _item : pystray.MenuItem) -> None: app.stop()

menu = pystray.Menu(
    pystray.MenuItem("Hello World", onClick),
    pystray.MenuItem("Hi World", onClick),
    pystray.Menu.SEPARATOR,
    pystray.MenuItem("Start Backup", onClick),
    pystray.Menu.SEPARATOR,
    pystray.MenuItem("Select Source Directory", onClick),
    pystray.MenuItem("Select Target Directory", onClick),
    pystray.Menu.SEPARATOR,
    pystray.MenuItem("Settings", onClick),
    pystray.Menu.SEPARATOR,
    pystray.MenuItem("Quit", quit)
)

app = pystray.Icon("Application", icon, menu=menu)

app.run()
