import tkinter as tk
from capyle.guicomponents import _ConfigUIComponent
import numpy as np

class _WindWeightUI(tk.Frame, _ConfigUIComponent):

    def __init__(self, parent, ca_config):
        tk.Frame.__init__(self, parent)
        _ConfigUIComponent.__init__(self)
        # super().__init__(parent)

        self.ca_config = ca_config

        # upper frame to hold title and dropdown box
        labelframe = tk.Frame(self)
        gen_label = tk.Label(labelframe, text='Wind Weight:')
        gen_label.pack(side=tk.LEFT)
        
        self.wind_weight = tk.StringVar()

        self.options = '0.0', '0.5', '1.0', '1.5', '2.0', '2.5', '3.0'
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
        print(choice)
        return float(choice)

    def set(self, value):
        self.wind_weight.set(value)

    def set_default(self):
        self.wind_weight.set("1")