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

m_u = 1 # amount of upgrades on money
v_u = 1 # amount of upgrades on votes
uv_cost = 0
mv_cost = 0
pv = 100000
rank = "Local"
pn = 1
pb = 1

screen = "main" # too lazy to do enumerators and uh im lazy thanks

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
    global votes, mode, money, mv_cost, uv_cost, screen, v_u, m_u, pv, rank, pn, pb
    while True:
        if pn == 1:
            pb = 1
        if pn >= 2:
            pb = pn*10
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
        mv_cost = 50 * m_u * 2
        uv_cost = 100 * v_u * 2
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

        if screen == "main":
            output.text = ( f" | Votes needed for prestige: {pv} | Rank: {rank} | ".center(get_width()) + " \n" +
                            f"Mode: Generating {mode}".center(get_width()) + "\n" +
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
                            f"»-----------------------------------------«".center(get_width()) + "\n" +
                            f" | [s] shop | [p] prestige | [main] this menu | [q] quit | ".center(get_width())
            ) # put text in output.text to add it
        if screen == "shop":
            output.text = ( f"| Money: ${money} | Votes: {votes} |".center(get_width()) + "\n" +
                            f"Super realistic shop".center(get_width()) + "\n" +
                            f"»-----------------------------------------«".center(get_width()) + "\n" +
                            f"[uv1] +{pb} vote per - ${uv_cost}".center(get_width()) + "\n" +
                            f"»-----------------------------------------«".center(get_width()) + "\n" +
                            f"[mv1] +{pb} money per - ${mv_cost}".center(get_width()) + "\n" +
                            f"»-----------------------------------------«".center(get_width()) + "\n" +
                            f"Type 'main' to exit".center(get_width())
            )
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
    global votes, mode ,money ,screen ,mv_cost ,uv_cost ,v_u ,m_u , pv, rank,pn , pb
    width = get_width()

    text = input_box.text.strip()
    cmds = ["x", "x"]
    cmds = text.lower().split()
    if not cmds:
        if mode == "votes":
            votes += 1*v_u*pb
        else:
            money += 1*m_u*pb
        cmds.append("x")

    


    if cmds[0] == "m" or cmds[0] == "mode":
        if mode == "votes":
            mode = "money"
        else:
            mode = "votes"
    if cmds[0] == "shop" or cmds[0] == "s":
        screen = "shop"

    if cmds[0] == "main":
        screen = "main"

    if cmds[0] == "uv1":
        if money >= uv_cost:
            money -= uv_cost
            v_u += 1
    if cmds[0] == "mv1":
        if money >= mv_cost:
            money -= mv_cost
            m_u += 1
    if cmds[0] == "p" or cmds[0] == "prestige":
        if votes >= pv:
            votes = 0
            money = 0
            v_u = 0
            m_u = 0
            pn += 1
            pv *= 10
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
