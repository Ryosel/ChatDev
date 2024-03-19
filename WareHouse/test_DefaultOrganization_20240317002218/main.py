'''
This is the main file of the software. It contains the entry point of the program and handles the GUI initialization.
'''
import tkinter as tk
class Application(tk.Tk):
    def __init__(self):
        super().__init__()  # Add this line to properly initialize the class
        self.title("SW Software")
        self.geometry("800x600")
        # Create and configure GUI elements here
        self.mainloop()
if __name__ == "__main__":
    app = Application()