
import tkinter as tk

import glueckskeks as gl

class my_gui():
    def __init__(self):
        # window setup
        self.main_window = tk.Tk()
        self.main_window.geometry("1000x100")
        # label
        self.main_text_label = tk.Label()
        self.main_text_label.pack()
        # button
        self.main_button = tk.Button(text="fetch quote", command=self.button_function)
        self.main_button.pack()
        # start
        self.start()

    def update_label(self, new_text):
        self.main_text_label.config(text=new_text)

    def button_function(self):
        # fetch quote
        new_quote = gl.get_quote()
        quote_text = new_quote[0]["q"] + "\n - by " + new_quote[0]["a"]
        # update label
        self.update_label(quote_text)

    def start(self):
        self.main_window.mainloop()

if __name__ == "__main__":
    my_gui = my_gui()

