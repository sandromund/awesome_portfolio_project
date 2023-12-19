import customtkinter as ct
from tkinter import BooleanVar


class App(ct.CTk):

    def __init__(self):
        super().__init__()
        # vars
        self.fun = BooleanVar(master=self, value=True)
        # objects
        self.textbox = ct.CTkTextbox(master=self)
        self.label = ct.CTkLabel(self, text="My Awsome Calculator ")
        self.x = ct.CTkEntry(self, placeholder_text="Enter a number X")
        self.y = ct.CTkEntry(self, placeholder_text="Enter a number Y")
        self.button = ct.CTkButton(master=self, text="Addition", command=self.button_pressed)
        self.progressbar = ct.CTkProgressBar(master=self)
        self.checkbox = ct.CTkCheckBox(master=self, text="Fun", variable=self.fun, onvalue=True, offvalue=False)
        # settings
        self.title("AI Inside")
        self.geometry("300x500")
        self.progressbar.set(0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        # placements
        args = {"padx": 10, "pady": 10, "sticky": "ew"}
        self.label.grid(**args)
        self.checkbox.grid(**args)
        self.x.grid(columnspan=2, **args)
        self.y.grid(columnspan=2, **args)
        self.textbox.grid(columnspan=2, **args)
        self.progressbar.grid(columnspan=2, **args)
        self.button.grid(columnspan=2, **args)

    def button_pressed(self, value=0):
        if len(self.x.get()) == 0 or len(self.y.get()) == 0:
            self.textbox.insert("0.0", "Please set values for X and Y. \n")
            return
        if not (0 <= value <= 1):
            x = self.x.get()
            y = self.y.get()
            if self.fun.get():
                result = x + y
            else:
                result = float(x) + float(y)
            answer = f"X={x} + Y={y} = {result} \n"
            self.textbox.insert("0.0", answer)
            return
        self.progressbar.set(value)
        app.after(500, self.button_pressed, value + 0.2)


if __name__ == '__main__':
    ct.set_appearance_mode("Dark")
    ct.set_default_color_theme("green")

    app = App()
    app.mainloop()
