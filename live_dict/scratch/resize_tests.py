import curses


def main(stdscr: curses.window):
    resize_count = 0
    curses.curs_set(False)
    stdscr.timeout(5)
    while(1):

        if stdscr.getch() == curses.KEY_RESIZE:
            resize_count += 1
        stdscr.clear()
        stdscr.addstr(0, 0, f"{resize_count}")
        stdscr.refresh()


curses.wrapper(main)
