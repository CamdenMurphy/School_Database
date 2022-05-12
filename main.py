from gui import *


def main():
    window = Tk()
    window.title('Student Database')
    window.geometry('345x280')
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
