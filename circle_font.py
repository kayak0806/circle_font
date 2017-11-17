#!/usr/bin/env python

import Tkinter as tk
import string
import build_arcs as barc
from letters import Letters
from build_arcs import Dimentions

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def values(self):
        return [self.x, self.y, point.x, point.y]

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

class App(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, None)
        self.grid()
        self._letters = Letters(80)
        self.createWidget()

    def createWidget(self):
        self.master.title("Lines")
        self.pack(fill=tk.BOTH, expand=1)

        # word = "The secret is not to dream, The secret is to wake up. Waking up is harder. I have woken up and I am real. I know where I come from and I know where I'm going. You cannot fool me any more. Or touch me. Or anything that is mine."
        # word = "It doesn't stop being magic just because you know how it works"
        word = "helloworld"
        text, width, height = self._letters.build_text(word, 5)

        canvas = tk.Canvas(self, width=width, height=height)

        for letter in text:
            for arc in letter:
                canvas.create_line(*arc, fill="grey", width=2)

        
        canvas.pack(fill=tk.BOTH, expand=1)
        





app = App()
app.master.title('circle font')
app.mainloop()
