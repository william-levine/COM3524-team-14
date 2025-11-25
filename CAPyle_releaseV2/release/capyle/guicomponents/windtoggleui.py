import tkinter as tk
from capyle.guicomponents import _ConfigUIComponent

class _WindToggleUI(tk.Frame, _ConfigUIComponent):

    def __init__(self, parent, ca_config):
        tk.Frame.__init__(self, parent)
        _ConfigUIComponent.__init__(self)
        # super().__init__(parent)

        self.ca_config = ca_config

        # upper frame to hold title and dropdown box
        labelframe = tk.Frame(self)
        gen_label = tk.Label(labelframe, text='Wind Direction:')
        gen_label.pack(side=tk.LEFT)
        
        self.wind_direction = tk.StringVar()

        self.options = 'North-West', 'North', 'North-East', 'West', 'East', 'South-West', 'South', 'South-East'
        self.optvar = tk.StringVar(self)
        self.option = self.options[0]
        self.optvar.set(self.options[0])
        self.optbox = tk.OptionMenu(labelframe, self.optvar, *self.options)
        self.optbox.config(width=9)
        self.optbox.pack(side=tk.LEFT)
        labelframe.pack()

    def get_value(self):
        # return self.options_map[self.optvar.get()]
        choice = self.optvar.get()
        return self.options.index(choice)

    def set(self, value):
        self.wind_direction.set(value)

    def set_default(self):
        self.wind_direction.set("North-West")