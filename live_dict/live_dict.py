import curses
import curses.textpad

from typing import Dict, Optional

import time


class Screen:
    def __init__(self, data: Dict) -> None:
        self.window_y, self.window_x = 0, 0

        self.scroll_top = 0

        self.data = data
        self.num_elements = self.read_dict()

        self.pad_dict: Optional[curses.window] = None

    def init_curses(self):
        self.wwindow = curses.initscr()
        self.wwindow.keypad(True)

        self.window_y, self.window_x = self.wwindow.getmaxyx()

        self.pad_dict = curses.newpad(self.num_elements, self.window_x)

        curses.curs_set(False)

        curses.noecho()
        curses.cbreak()

        # Masks the mouse inputs, turns scrolling into key up and downs.
        curses.mousemask(0)

        self.wwindow.timeout(0)

        self.height, self.width = self.wwindow.getmaxyx()

    def read_dict(self):
        return self.read_dict_inner(self.data)

    def read_dict_inner(self, curr_dict: Dict) -> int:
        num_elements = 0
        for value in curr_dict.values():
            num_elements += 1
            if isinstance(value, dict):
                num_elements += self.read_dict_inner(value)
        return num_elements

    def display_dict(self, data: dict, idx: int = 0, nest: int = 0) -> int:
        tabs: str = "  "*nest
        for key, val in data.items():
            if isinstance(val, dict):
                disp: str = f'{tabs}{key}'
                if len(disp) >= self.window_x:
                    self.too_smol()
                self.pad_dict.addstr(idx, 0, disp)
                idx += 1
                idx = self.display_dict(val, idx, nest+1)
            else:
                disp: str = f'{tabs}{key} = {val}'
                if len(disp) >= self.window_x:
                    self.too_smol()
                self.pad_dict.addstr(idx, 0, disp)
                # self.pad_dict.addstr(idx, self.window_x -
                #                      len(str(val)) - 1, f'{val}')
                idx += 1

        return idx

    def run(self):

        try:
            self.init_curses()
            self.display_dict(self.data)
            self.input_stream()
        except KeyboardInterrupt:
            pass
        finally:
            curses.endwin()

    def input_stream(self):
        while(1):

            key_ch = self.get_one_key()

            if key_ch == curses.KEY_RESIZE:
                self.window_y, self.window_x = self.wwindow.getmaxyx()
                self.pad_dict.resize(self.num_elements, self.window_x)

                self.pad_dict.clear()
                self.display_dict(self.data)
            elif key_ch == curses.KEY_MOUSE:
                self.oprint("mouse")
            elif key_ch == curses.KEY_UP:
                self.oprint("keyup")
                self.scroll_top = max(0, self.scroll_top-1)
            elif key_ch == curses.KEY_DOWN:
                self.scroll_top = min(
                    self.num_elements-self.window_y, self.scroll_top+1)
                self.oprint("keydown")

            elif key_ch == curses.KEY_PPAGE:
                self.scroll_top = max(0, self.scroll_top-1)
            elif key_ch == curses.KEY_NPAGE:
                self.scroll_top = min(
                    self.num_elements-self.window_y, self.scroll_top+1)

            self.pad_dict.refresh(self.scroll_top, 0, 0, 0,
                                  self.window_y-1, self.window_x-1)

            time.sleep(0.05)

    def get_one_key(self) -> int:
        prev_ch = curses.ERR

        while 1:
            key_ch = self.wwindow.getch()
            if key_ch == curses.ERR:
                break
            prev_ch = key_ch

        return prev_ch

    def too_smol(self):
        self.pad_dict.clear()
        self.wwindow.clear()
        # From my experimentation, this barely fits in the smallest possible terminal.
        self.wwindow.addstr(0, 0, "ERR 2 SMOL")
        self.wwindow.refresh()

        while 1:
            ch = self.wwindow.getch()
            if ch == curses.ascii.ESC:
                curses.endwin()
                exit(0)

    def oprint(self, s: str) -> None:
        # TODO: update with logging
        pass
