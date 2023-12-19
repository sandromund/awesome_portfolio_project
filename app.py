import time

import customtkinter as ct
import tkinter as t


class App(ct.CTk):

    def __init__(self):
        super().__init__()
        #self.textbox = ct.CTkTextbox(master=self)
        self.x_label = ct.CTkLabel(self, text="Input X")
        self.y_label = ct.CTkLabel(self, text="Input Y")
        self.x = ct.CTkEntry(self, placeholder_text="4")
        self.y = ct.CTkEntry(self, placeholder_text="20")
        self.button = ct.CTkButton(master=self, text="Complex Calculation", command=self.button_pressed)
        self.progressbar = ct.CTkProgressBar(master=self)
        # settings
        self.title("AI Inside")
        self.geometry("400x600")
        self.progressbar.set(0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        # placements
        args = {"padx": 20, "pady": 10, "sticky": "nsew"}
        # self.textbox.grid(**args)
        self.x_label.grid(row=0, column=0, **args)
        self.x.grid(row=0, column=1, **args)
        self.y_label.grid(row=1, column=0, **args)
        self.y.grid(row=1, column=1, **args)
        self.progressbar.grid(row=2, columnspan=2, **args)
        self.button.grid(row=3, columnspan=2, **args)

    def button_pressed(self, value=0):
        x = self.textbox.get(1.0, t.END)
        if not (0 <= value <= 1):
            self.textbox.insert("0.0", str(x) + "\n")
            return
        self.progressbar.set(value)
        app.after(1500, self.button_pressed, value + 0.2)


if __name__ == '__main__':
    ct.set_appearance_mode("Dark")
    ct.set_default_color_theme("green")

    app = App()
    app.mainloop()
