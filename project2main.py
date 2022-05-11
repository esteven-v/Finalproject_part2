from project2gui import *


def main():
    """
    - Window for a Dice roll
    - will also do math in it too.
    - window will not change size.
    """
    window = Tk()
    window.title('Final project Section 2')
    window.geometry('700x500')
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
