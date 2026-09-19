from prompt_toolkit.application import Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.layout import Layout, HSplit
from prompt_toolkit.widgets import TextArea
from prompt_toolkit.key_binding import KeyBindings
import threading
import time
import shutil
from datetime import datetime
import render as rn
import guess as gu

votes = 0
mode = "votes"
money = 0

m_u = 1 # amount of upgrades on money
v_u = 1 # amount of upgrades on votes
uv_cost = 0
mv_cost = 0
pv = 10000
rank = "Local"
pn = 1
pb = 1
notif = ""
gnum = 2

ranks = ["Normal",
         "Local",
         "Regional",
         "State",
         "Prime Minister"]

screen = "start" # too lazy to do enumerators and uh im lazy thanks

dollar = ["▄▄███▄▄·",
          "█╔═█═══╝",
          "███████╗",
          "════███║",
          "███████║",
          "╚═▀▀▀══╝"
]



output = TextArea(
    focusable=False,
)

input_box = TextArea(
    height=1,
    prompt="~ ❯",
)



def is_int(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

def get_width():
    size = shutil.get_terminal_size(fallback=(120, 24))
    return size.columns - 3


def loop():
    global votes, mode, money, mv_cost, uv_cost, screen, v_u, m_u, pv, rank, pn, pb, ranks, notif, gnum
    while True:
        if pn == 1:
            pb = 1
        if pn >= 2:
            pb = pn*10
        rank = ranks[pn]
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
            pln1 += rn.render(digits, 0)
            pln2 += rn.render(digits, 1)
            pln3 += rn.render(digits, 2)
            pln4 += rn.render(digits, 3)
            pln5 += rn.render(digits, 4)
            pln6 += rn.render(digits, 5)
        for digits in str(money):             
            mln1 += rn.render(digits, 0)
            mln2 += rn.render(digits, 1)
            mln3 += rn.render(digits, 2)
            mln4 += rn.render(digits, 3)
            mln5 += rn.render(digits, 4)
            mln6 += rn.render(digits, 5)
        if screen == "start":
            output.text = ( f"╭{"":─^{get_width()}}╮" + "\n│" +
                "".center(get_width()) + "│\n│" +
                "   ▄███████▄  ▄██████▄   ▄█          ▄████████    ▄████████".center(get_width()) + "│\n│" +
                "  ███    ███ ███    ███ ███         ███    ███   ███    ███".center(get_width()) + "│\n│" +
                "  ███    ███ ███    ███ ███         ███    ███   ███    ███".center(get_width()) + "│\n│" +
                "  ███    ███ ███    ███ ███         ███    ███  ▄███▄▄▄▄██▀".center(get_width()) + "│\n│" +
                "▀█████████▀  ███    ███ ███       ▀███████████ ▀▀███▀▀▀▀▀  ".center(get_width()) + "│\n│" +
                "  ███        ███    ███ ███         ███    ███ ▀███████████".center(get_width()) + "│\n│" +
                "  ███        ███    ███ ███▌    ▄   ███    ███   ███    ███".center(get_width()) + "│\n│" +
                " ▄████▀       ▀██████▀  █████▄▄██   ███    █▀    ███    ███".center(get_width()) + "│\n│" +
                "                        ▀                        ███    ███".center(get_width()) + "│\n│" +
                "                      Made with ♥  by the ChimmusFoundation".center(get_width()) + "│\n│" +
                "".center(get_width()-7) + "   v1.0│\n" +
                f"╰{"":─^{get_width()}}╯" + "\n" + "\n" +
                "╭────────────────────╮".center(get_width()) + "\n" +
                "│Click enter to start│".center(get_width()) + "\n" +
                "╰────────────────────╯".center(get_width()) + "\n" + "\n" + "Type q and then click enter to exit".center(get_width())
                
            )
        if screen == "main":
            output.text = ( f"╭{"":─^{get_width()}}╮" +
                            "\n│" + f" | Votes needed for prestige: {pv} | Rank: {rank} | Time: {datetime.now().strftime("%H:%M:%S")} |".center(get_width()) + "│\n│" +
                            f"Mode: Generating {mode}".center(get_width()) + "│\n│" +
                            f"»-----------------------------------------«".center(get_width()) + "│\n│" +
                            f"Votes:".center(get_width()) + "│\n│" + 
                            f"{pln1}".center(get_width()) + "│\n│" +
                            f"{pln2}".center(get_width()) + "│\n│" +
                            f"{pln3}".center(get_width()) + "│\n│" +
                            f"{pln4}".center(get_width()) + "│\n│" +
                            f"{pln5}".center(get_width()) + "│\n│" +
                            f"{pln6}".center(get_width()) + "│\n│" +
                            f"»-----------------------------------------«".center(get_width()) + "│\n│" +
                            f"Money:".center(get_width()) + "│\n│" + 
                            f"{dollar[0]}   {mln1}".center(get_width()) + "│\n│" +
                            f"{dollar[1]}   {mln2}".center(get_width()) + "│\n│" +
                            f"{dollar[2]}   {mln3}".center(get_width()) + "│\n│" +
                            f"{dollar[3]}   {mln4}".center(get_width()) + "│\n│" +
                            f"{dollar[4]}   {mln5}".center(get_width()) + "│\n│" +
                            f"{dollar[5]}   {mln6}".center(get_width()) + "│\n│" +
                            f"»-----------------------------------------«".center(get_width()) + "│\n│" +
                            f"{notif}".center(get_width()) + "│\n│" + 
                            f" | [s] shop | [p] prestige | [main] this menu | [q] quit | ".center(get_width()) + "│\n" 
                            f"╰{"":─^{get_width()}}╯"
            ) # put text in output.text to add it
        if screen == "shop":
            output.text = ( f"╭{"":─^{get_width()}}╮" + "\n│" + 
                            f"| Money: ${money} | Votes: {votes} |".center(get_width()) + "│\n│" +
                            f"Super realistic shop".center(get_width()) + "│\n│" +
                            f"»-----------------------------------------«".center(get_width()) + "│\n│" +
                            f"[uv1] +{pb} vote per - ${uv_cost}".center(get_width()) + "│\n│" +
                            f"»-----------------------------------------«".center(get_width()) + "│\n│" +
                            f"[mv1] +{pb} money per - ${mv_cost}".center(get_width()) + "│\n│" +
                            f"»-----------------------------------------«".center(get_width()) + "│\n│" +
                            f"Type 'main' to exit".center(get_width()) + "│\n" +
                            f"╰{"":─^{get_width()}}╯"
            )
        if screen == "ginfo":
            output.text = ( f"╭{"":─^{get_width()}}╮" + "\n│" + 
                            f"".center(get_width()) + "│\n│" +
                            f"To make a 'guess' use the guess command followed by the number of digits".center(get_width()) + "│\n│" +
                            f"For example: guess 2".center(get_width()) + "│\n│" +
                            f"Places a guess, it would use a 2 digit number and cost $100".center(get_width()) + "│\n│" +
                            f"You will need to watch a compulsory animation".center(get_width()) + "│\n│" +
                            f"".center(get_width()) + "│\n" + 
                            f"╰{"":─^{get_width()}}╯"
            )
        if screen == "guess":
            for i in range(gnum):
                g1 += render("r", 0)
                g2 += render("r", 1)
                g3 += render("r", 2)
                g4 += render("r", 3)
                g5 += render("r", 4)
                g6 += render("r", 5)

            output.text = ( f"╭{"":─^{get_width()}}╮" + "\n│" + 
                            f"".center(get_width()) + "│\n│" +
                            f"{g1}".center(get_width()) + "│\n│" +
                            f"{g2}".center(get_width()) + "│\n│" +
                            f"{g3}".center(get_width()) + "│\n│" +
                            f"{g4}".center(get_width()) + "│\n│" +
                            f"{g5}".center(get_width()) + "│\n│" +
                            f"{g6}".center(get_width()) + "│\n│" +
                            f"".center(get_width()) + "│\n" + 
                            f"╰{"":─^{get_width()}}╯"
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
    global votes, mode ,money ,screen ,mv_cost ,uv_cost ,v_u ,m_u , pv, rank,pn , pb, ranks, notif, gnum
    width = get_width()

    text = input_box.text.strip()
    cmds = ["x", "x"]
    cmds = text.lower().split()
    if screen == "guess":
        cmds = ["DONT DISTURB"]
    if not cmds:
        if screen == "start":
            screen = "main"
        if mode == "votes":
            votes += 1*v_u*pb
        else:
            money += 1*m_u*pb
        cmds.append("x")
    else:
        if screen == "start":
            screen = "main"
    # hi
    if len(cmds) == 1:
        if cmds[0] == "guess" or cmds[0] == "g":
            screen = "ginfo"
    if len(cmds) >= 2:
        if cmds[0] == "guess" or cmds[0] == "g":
            if is_int(cmds[1]):
                gnum = int(cmds[1])
                if money >= (10 ** gnum):
                    screen == "guess"
                else:
                    notif = f"{datetime.now().strftime("%H:%M:%S")} Too Poor to play Guess"


    if cmds[0] == "m" or cmds[0] == "mode":
        if mode == "votes":
            mode = "money"
        else:
            mode = "votes"
    if cmds[0] == "shop" or cmds[0] == "s":
        screen = "shop"

    if cmds[0] == "main" or cmds[0] == "ma":
        screen = "main"

    if cmds[0] == "uv1":
        if money >= uv_cost:
            money -= uv_cost
            v_u += 1
            notif = f"{datetime.now().strftime("%H:%M:%S")} Upgraded Votes"
    if cmds[0] == "mv1":
        if money >= mv_cost:
            money -= mv_cost
            m_u += 1
            notif = f"{datetime.now().strftime("%H:%M:%S")} Upgraded Money"
    if cmds[0] == "p" or cmds[0] == "prestige":
        if votes >= pv:
            votes = 0
            money = 0
            v_u = 1
            m_u = 1
            pn += 1
            pv *= 10
            notif = f"{datetime.now().strftime("%H:%M:%S")} Prestiged to {ranks[pn]}"


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
