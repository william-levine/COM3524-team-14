import tkinter as tk
from capyle.guicomponents import _ConfigUIComponent

class _FireToggleUI(tk.Frame, _ConfigUIComponent):

    def __init__(self, parent, ca_config):
        tk.Frame.__init__(self, parent)
        _ConfigUIComponent.__init__(self)
        # super().__init__(parent)

        self.ca_config = ca_config

        # upper frame to hold title and dropdown box
        labelframe = tk.Frame(self)
        gen_label = tk.Label(labelframe, text='Fire Start:')
        gen_label.pack(side=tk.LEFT)
        
        self.start_fire = tk.StringVar()

        self.options = 'LEFT', 'RIGHT'
        self.optvar = tk.StringVar(self)
        self.optvar.set(self.options[0])
        self.optbox = tk.OptionMenu(labelframe, self.optvar, *self.options)
        self.optbox.config(width=9)
        self.optbox.pack(side=tk.LEFT)
        labelframe.pack()

    def get_value(self):
        return self.optvar.get()

    def set(self, value):
        self.start_fire.set(value)

    def set_default(self):
        self.start_fire.set("LEFT")