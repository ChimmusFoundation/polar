from prompt_toolkit.application import Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.layout import Layout, HSplit
from prompt_toolkit.widgets import TextArea
from prompt_toolkit.key_binding import KeyBindings
import threading
import time
import shutil

votes = 0
mode = "votes"
money = 0

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


dollar = ["▄▄███▄▄·",
          "█╔═█═══╝",
          "███████╗",
          "════███║",
          "███████║",
          "╚═▀▀▀══╝"
]


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
    prompt="~ ❯",
)


def get_width():
    size = shutil.get_terminal_size(fallback=(120, 24))
    return size.columns - 4


def loop():
    global votes, mode, money
    while True:
        time.sleep(0.001)
        pln1 = ""
        pln2 = ""
        pln3 = ""
        pln4 = ""
        pln5 = ""
        pln6 = ""

        mln1 = ""
        mln2 = ""
        mln3 = ""
        mln4 = ""
        mln5 = ""
        mln6 = ""

        for digits in str(votes):
            aln1, aln2, aln3, aln4, aln5, aln6 = render(digits)
            pln1 += aln1
            pln2 += aln2
            pln3 += aln3
            pln4 += aln4
            pln5 += aln5
            pln6 += aln6
        for digits in str(money): # so bad for memory safety :sob:, poor garbage collector :(
            aln1, aln2, aln3, aln4, aln5, aln6 = render(digits)
            mln1 += aln1
            mln2 += aln2
            mln3 += aln3
            mln4 += aln4
            mln5 += aln5
            mln6 += aln6


        output.text = ( f"Mode: Generating {mode}".center(get_width()) + "\n" +
                        f"»-----------------------------------------«".center(get_width()) + "\n" +
                        f"Votes:".center(get_width()) + "\n" + 
                        f"{pln1}".center(get_width()) + "\n" +
                        f"{pln2}".center(get_width()) + "\n" +
                        f"{pln3}".center(get_width()) + "\n" +
                        f"{pln4}".center(get_width()) + "\n" +
                        f"{pln5}".center(get_width()) + "\n" +
                        f"{pln6}".center(get_width()) + "\n" +
                        f"»-----------------------------------------«".center(get_width()) + "\n" +
                        f"Money:".center(get_width()) + "\n" + 
                        f"{dollar[0]}   {mln1}".center(get_width()) + "\n" +
                        f"{dollar[1]}   {mln2}".center(get_width()) + "\n" +
                        f"{dollar[2]}   {mln3}".center(get_width()) + "\n" +
                        f"{dollar[3]}   {mln4}".center(get_width()) + "\n" +
                        f"{dollar[4]}   {mln5}".center(get_width()) + "\n" +
                        f"{dollar[5]}   {mln6}".center(get_width()) + "\n" +
                        f"»-----------------------------------------«".center(get_width()) 
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
    global votes, mode, money
    width = get_width()

    text = input_box.text.strip()
    cmds = ["x", "x"]
    cmds = text.lower().split()
    if not cmds:
        if mode == "votes":
            votes += 1
        else:
            money += 1
        cmds.append("x")
    
    if cmds[0] == "m" or cmds[0] == "mode":
        if mode == "votes":
            mode = "money"
        else:
            mode = "votes"


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
