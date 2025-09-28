#mouse_events.py

import curses as c
def main(screen):
    c.curs_set(0) #hides the cursor
    c.mousemask(1)
    inp = screen.getch()
    if inp == c.KEY_MOUSE:
        screen.addstr(17,40, "Mouse is clicked")
        screen.refresh()
    screen.getch()

c.wrapper(main)

