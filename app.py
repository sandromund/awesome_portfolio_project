
import customtkinter as ct


class App(ct.CTk):

    def __init__(self):
        super().__init__()
        self.textbox = ct.CTkTextbox(master=self)
        self.label = ct.CTkLabel(self, text="X + Y = ? ")
        self.x = ct.CTkEntry(self, placeholder_text="Enter a number X")
        self.y = ct.CTkEntry(self, placeholder_text="Enter a number Y")
        self.button = ct.CTkButton(master=self, text="Addition", command=self.button_pressed)
        self.progressbar = ct.CTkProgressBar(master=self)
        # settings
        self.title("AI Inside")
        self.geometry("400x600")
        self.progressbar.set(0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        # placements
        args = {"padx": 10, "pady": 5, "sticky": "ew"}
        self.label.grid(row=0, **args)
        self.x.grid(row=1, columnspan=2, **args)
        self.y.grid(row=2, columnspan=2, **args)
        self.textbox.grid(row=3, columnspan=2, **args)
        self.progressbar.grid(row=4, columnspan=2, **args)
        self.button.grid(row=5, columnspan=2, **args)

    def button_pressed(self, value=0):
        if not (0 <= value <= 1):
            x = self.x.get()
            y = self.y.get()
            answer = f"X={x} + Y={y} = {x + y} \n"
            self.textbox.insert("0.0", answer)
            return
        self.progressbar.set(value)
        app.after(500, self.button_pressed, value + 0.2)


if __name__ == '__main__':
    ct.set_appearance_mode("Dark")
    ct.set_default_color_theme("green")

    app = App()
    app.mainloop()
