from prompt_toolkit.application import Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.layout import Layout, HSplit
from prompt_toolkit.widgets import TextArea
from prompt_toolkit.key_binding import KeyBindings
import threading
import time
import shutil

utime = 1

output = TextArea(
    focusable=False,
)

input_box = TextArea(
    height=1,
    prompt="User $ ",
)


def get_width():
    size = shutil.get_terminal_size(fallback=(120, 24))
    return size.columns - 4


def loop():
    global utime # variables must be put here
    while True:
        time.sleep(1)
        utime += 1
        output.text = (f"Uptime:".center(get_width()) + "\n" + 
                        f"{utime}".center(get_width())
        ) # put text in output.text to add it
        try:
            get_app().invalidate()
        except Exception:
            pass


threading.Thread(
    target=loop,
    daemon=True
).start()

kb = KeyBindings()


@kb.add("enter")
def command(event):
    width = get_width()

    text = input_box.text.strip()
    cmds = ["x", "x"]
    cmds = text.lower().split()
    if not cmds:
        cmds.append("x")

    if cmds[0] == "quit" or cmds[0] == "q":
        # commands are written like this
        get_app().exit()
        return

    input_box.text = ""


root = HSplit([
    output,
    input_box,
])

app = Application(
    layout=Layout(root),
    key_bindings=kb,
    full_screen=True,
)

app.run()
