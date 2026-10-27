# Designed with https://visualtkinter.com - paste this file into File > Import there to edit it visually
import tkinter as tk
from tkinter import ttk


class Application:
    def __init__(self, root):
        self.root = root
        root.title("Main")
        root.geometry("520x380")

        self.name_lbl = tk.Label(root, text="Name")
        self.name_lbl.place(x=90, y=90, width=90, height=26)

        self.course_lbl = tk.Label(root, text="Class")
        self.course_lbl.place(x=100, y=150, width=90, height=26)

        self.entry1 = tk.Entry(root)
        self.entry1.place(x=240, y=90, width=150, height=28)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
