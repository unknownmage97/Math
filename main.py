from tkinter import *
from gui import *


def main():
    window = Tk()
    window.title("Kind of Calculator")
    window.geometry('500x220')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()


if __name__ == "__main__":
    main()