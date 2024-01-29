import tkinter as tk
import sys

class Terminal(tk.Text):
    def __init__(self, root, bg="White", fg="black", **kwargs):
        super().__init__(root, bg = bg, fg=fg, **kwargs)
        with open('.buf', 'w') as f:
            f.write("")
            pass
        sys.stdout = open(".buf", 'a')
        self.read_std_out()
    def read_std_out(self):
        sys.stdout.flush()  # Force write
        with open('.buf', 'r') as buf:
            read = buf.read()
            if read:  # Do not write if empty
                self.insert("end", read)
        with open('.buf', 'w'):
            pass  # Clear file

        sys.stdout = open(".buf", 'a')
        self.after(200, self.read_std_out)