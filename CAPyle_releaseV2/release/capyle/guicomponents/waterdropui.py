import tkinter as tk
from capyle.guicomponents import _ConfigUIComponent
from capyle.utils import is_valid_integer


class _WaterDropUI(tk.Frame, _ConfigUIComponent):
    DEFAULT = 3

    def __init__(self, parent,ca_config):
        """Starts the water drop stratergy after a number of hours/ iteration"""
        tk.Frame.__init__(self, parent)
        _ConfigUIComponent.__init__(self)
        water_label = tk.Label(self, text="Start water drop after:")
        hours_label = tk.Label(self, text="hour(s)")
        water_label.pack(side=tk.LEFT)
        hours_label.pack(side=tk.RIGHT)
        is_valid_int = (self.register(is_valid_integer), '%P')
        self.gen_entry = tk.Entry(self, validate='key',
                                  validatecommand=is_valid_int, width=4)
        self.set_default()
        self.gen_entry.pack(side=tk.LEFT)

    def get_value(self):
        x = self.gen_entry.get()
        if x == '':
            x = 0
        return int(x)

    def set_default(self):
        self.set(self.DEFAULT)

    def set(self, value):
        super(_WaterDropUI, self).set(entry=self.gen_entry, value=value)