import curses


def main(stdscr: curses.window):
    resize_count = 0
    curses.curs_set(False)
    stdscr.timeout(5)
    stdscr.resize(100, 100)
    while(1):
        key = stdscr.getch()
        if key == curses.KEY_RESIZE:
            resize_count += 1
        if key == curses.KEY_UP:
            stdscr.scroll()

        stdscr.clear()
        for i in range(10):
            stdscr.addstr(i, 0, f'key{i}:')
        stdscr.refresh()


curses.wrapper(main)
