from prompt_toolkit.application import Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.layout import Layout, HSplit
from prompt_toolkit.widgets import TextArea
from prompt_toolkit.key_binding import KeyBindings
import threading
import time
import shutil

votes = 0

i01 = ["   ██╗   ",
       "  ███║   ",
       "  ╚██║   ",
       "   ██║   ",
       "   ██║   ",
       "   ╚═╝   "]

i02 = ["██████╗  ",
       "╚════██╗ ",
       " █████╔╝ ",
       "██╔═══╝  ",
       "███████╗ ",
       "╚══════╝ "]

i03 = ["██████╗  ",
       "╚════██╗ ",
       " █████╔╝ ",
       " ╚═══██╗ ",
       "██████╔╝ ",
       "╚═════╝  "]

i04 = ["██╗  ██╗ ",
       "██║  ██║ ",
       "███████║ ",
       "╚════██║ ",
       "     ██║ ",
       "     ╚═╝ "]

i05 = ["███████╗ ",
       "██╔════╝ ",
       "███████╗ ",
       "╚════██║ ",
       "███████║ ",
       "╚══════╝ "]

i06 = [" ██████╗ ",
       "██╔════╝ ",
       "███████╗ ",
       "██╔═══██╗",
       "╚██████╔╝",
       " ╚═════╝ "]

i07 = ["███████╗ ",
       "╚════██║ ",
       "    ██╔╝ ",
       "   ██╔╝  ",
       "   ██║   ",
       "   ╚═╝   "]

i08 = [" █████╗  ",
       "██╔══██╗ ",
       "╚█████╔╝ ",
       "██╔══██╗ ",
       "╚█████╔╝ ",
       " ╚════╝  "]

i09 = [" █████╗  ",
       "██╔══██╗ ",
       "╚██████║ ",
       " ╚═══██║ ",
       " █████╔╝ ",
       " ╚════╝  "]

i00 = [" ██████╗ ",
       "██╔═████╗",
       "██║██╔██║",
       "████╔╝██║",
       "╚██████╔╝",
       " ╚═════╝ "]

ansi = [" ",
        " ", # a second one to give more spaces
        "═",
        "║",
        "╔",
        "╗",
        "╚",
        "╝",
        "█"]


index = {
    "0": "i00",
    "1": "i01",
    "2": "i02",
    "3": "i03",
    "4": "i04",
    "5": "i05",
    "6": "i06",
    "7": "i07",
    "8": "i08",
    "9": "i09",
}

def render(n):
    ntr = index[n] # number to render
    lw = globals()[ntr] # list with number
    ln1 = f"{lw[0]}"
    ln2 = f"{lw[1]}"
    ln3 = f"{lw[2]}"
    ln4 = f"{lw[3]}"
    ln5 = f"{lw[4]}"
    ln6 = f"{lw[5]}"
    return ln1, ln2, ln3, ln4, ln5, ln6

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
    global votes
    while True:
        time.sleep(0.001)
        pln1 = ""
        pln2 = ""
        pln3 = ""
        pln4 = ""
        pln5 = ""
        pln6 = ""
        for digits in str(votes):
            aln1, aln2, aln3, aln4, aln5, aln6 = render(digits)
            pln1 += aln1
            pln2 += aln2
            pln3 += aln3
            pln4 += aln4
            pln5 += aln5
            pln6 += aln6
        output.text = (f"Votes:".center(get_width()) + "\n" + 
                        f"{pln1}".center(get_width()) + "\n" +
                        f"{pln2}".center(get_width()) + "\n" +
                        f"{pln3}".center(get_width()) + "\n" +
                        f"{pln4}".center(get_width()) + "\n" +
                        f"{pln5}".center(get_width()) + "\n" +
                        f"{pln6}".center(get_width()) + "\n" +
                        f"----".center(get_width())
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
    global votes
    width = get_width()

    text = input_box.text.strip()
    cmds = ["x", "x"]
    cmds = text.lower().split()
    if not cmds:
        votes += 1
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
