from gui import *

def main():
    """
    ~~Main function~~
    This program will modify the student records in the records.csv
    file included in the GitHub repository CamdenMurphy/Student_Database.
    The records.csv file must be in the same folder/directory as main.py
    and gui.py to successfully append the records.
    :return: None
    """
    window = Tk()
    window.title('Student Database')
    window.geometry('345x250')
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
