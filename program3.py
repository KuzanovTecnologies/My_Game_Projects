#program3.py
import curses as c

screen = c.initscr()
win = c.newwin(20, 60, 0, 0)

c.noecho()
c.cbreak()
screen.keypad(True)
while True:
    char = screen.getch() #takes input
    if char == ord('q'):
        win.addstr(5,10, "Hello World")
        win.refresh()
screen.endwin()
