#program is written as Scripts
# curser_starter.py

import curses
import time
window_screen = curses.initscr()
window_screen.clear()

time.sleep(10)

height = 20
width = 60
y = 0
x = 0

screen = curses.newwin(height, width, y, x)

# text_app.py
import curses
import time

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
screen.addstr(0,0, "Hello")
screen.refresh()
time.sleep(10)
curses.endwin()

