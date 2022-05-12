from tkinter import *
import csv


class GUI:
    def __init__(self, window):
        """
        This method initializes the graphical user interface.
        :param window: tkinter gui window from main.py
        """
        self.window = window

        # Name entry box
        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Student Name')
        self.entry_name = Entry(self.frame_name)
        self.label_name.pack(padx=5, side='left')
        self.entry_name.pack(padx=5, side='left')
        self.frame_name.pack(anchor='w', pady=10)   # anchor='w' helps to change the frame position from center to west.

        # Student ID entry box
        self.frame_id = Frame(self.window)
        self.label_id = Label(self.frame_id, text='Student ID')
        self.entry_id = Entry(self.frame_id)
        self.label_id.pack(padx=5, side='left')
        self.entry_id.pack(padx=26, side='left')
        self.frame_id.pack(anchor='w', pady=10)

        # Grade level radio buttons
        self.frame_status = Frame(self.window)
        self.radio_1 = StringVar()
        self.radio_1.set('NONE')
        self.label_status = Label(self.frame_status, text='Status')
        self.radio_fresh = Radiobutton(self.frame_status, text='Freshman', variable=self.radio_1, value='Freshman')
        self.radio_soph = Radiobutton(self.frame_status, text='Sophomore', variable=self.radio_1, value='Sophomore')
        self.radio_junior = Radiobutton(self.frame_status, text='Junior', variable=self.radio_1, value='Junior')
        self.radio_senior = Radiobutton(self.frame_status, text='Senior', variable=self.radio_1, value='Senior')
        self.label_status.pack(padx=5, side='left')
        self.radio_fresh.pack(side='left')
        self.radio_soph.pack(side='left')
        self.radio_junior.pack(side='left')
        self.radio_senior.pack(side='left')
        self.frame_status.pack(anchor='w', pady=10)

        # Save and remove buttons
        self.frame_buttons = Frame(self.window)
        self.button_save = Button(self.frame_buttons, text='    SAVE    ', command=self.save_clicked)
        self.button_remove = Button(self.frame_buttons, text='REMOVE', command=self.remove_clicked)
        self.button_save.pack(side='left', padx=10)
        self.button_remove.pack(side='left', padx=10)
        self.frame_buttons.pack(pady=10)

        # Message prompt
        self.frame_prompt = Frame(self.window)
        self.label_prompt = Label(self.frame_prompt, text='')
        self.label_prompt.pack(side='top')
        self.frame_prompt.pack(pady=10)

    def clear_window(self):
        """
        This method is called to reset the window to its default settings
        :return: None
        """
        try:
            self.entry_name.delete(0, END)
            self.entry_id.delete(0, END)
            self.radio_1.set("NONE")
        except Exception:
            print('error')

    def save_clicked(self):
        """
        This method is enacted when the save button is clicked.
        It saves the entered student into a csv file.
        :return: None
        """
        try:
            name = self.entry_name.get()
            student_id = self.entry_id.get()
            status = self.radio_1.get()
            duplicate = False

            if student_id.isdigit():
                int(student_id)

                with open('records.csv', 'r', newline='') as records:
                    content = csv.reader(records)
                    for row in content:
                        if int(row[1]) == int(student_id):
                            duplicate = True
                if duplicate:
                    prompt = f'Student {student_id} already exists!'
                else:
                    with open('records.csv', 'a', newline='') as records:
                        content = csv.writer(records)
                        content.writerow([name, student_id, status])
                        prompt = 'Student added.'
            else:
                prompt = 'Student ID must be an number!'

            self.label_prompt.config(text=f'{prompt}')
        except Exception:
            print('Error')

        self.clear_window()

    def remove_clicked(self):
        """
        This method searches records.csv for a student ID and removes its contents
        :return: None
        """
        try:
            student_id = int(self.entry_id.get())

            with open('records.csv', 'r', newline='') as read_file:
                lines = list()
                prompt = ''
                found = False
                content = csv.reader(read_file)

                for row in content:
                    if int(row[1]) != student_id:
                        lines.append(row)
                    else:
                        prompt = 'Student removed.'
                        found = True
                if found:
                    self.rewrite(lines)
                elif not found:
                    prompt = f'Student ID: {student_id} not found!'

                self.label_prompt.config(text=f'{prompt}')
        except Exception:
            print('Error')

        self.clear_window()

    def rewrite(self, lines):
        """
        This method overwrites the records.csv file with all the students
        except for the one removed in the remove.clicked() method.
        :param lines: list of records.csv contents without the student to be removed
        :return: none
        """
        try:
            with open('records.csv', 'w', newline='') as write_file:
                new_content = csv.writer(write_file)
                for line in lines:
                    new_content.writerow(line)
        except Exception:
            print('Error')
