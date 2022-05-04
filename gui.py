from tkinter import *
import csv


class GUI:
    def __init__(self, window):
        """
        :param window:
        """
        self.window = window

        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Name')
        self.entry_name = Entry(self.frame_name)
        self.label_name.pack(padx=5, side='left')
        self.entry_name.pack(padx=5, side='left')
        self.frame_name.pack(anchor='w', pady=10)   # anchor='w' helps to change the frame position from center to west.

        self.frame_age = Frame(self.window)
        self.label_age = Label(self.frame_age, text='Age')
        self.entry_age = Entry(self.frame_age)
        self.label_age.pack(padx=5, side='left')
        self.entry_age.pack(padx=16, side='left')
        self.frame_age.pack(anchor='w', pady=10)

        self.frame_status = Frame(self.window)
        self.radio_1 = StringVar()
        self.radio_1.set('NONE')
        self.label_status = Label(self.frame_status, text='Status')
        self.radio_student = Radiobutton(self.frame_status, text='Student', variable=self.radio_1, value='Student')
        self.radio_staff = Radiobutton(self.frame_status, text='Staff', variable=self.radio_1, value='Staff')
        self.radio_both = Radiobutton(self.frame_status, text='Both', variable=self.radio_1, value='Both')
        self.label_status.pack(padx=5, side='left')
        self.radio_student.pack(side='left')
        self.radio_staff.pack(side='left')
        self.radio_both.pack(side='left')
        self.frame_status.pack(anchor='w', pady=10)

        self.frame_save = Frame(self.window)
        self.button_save = Button(self.frame_save, text='SAVE', command=self.save_clicked)
        self.button_save.pack()
        self.frame_save.pack(pady=10)



    def save_clicked(self):
        name = self.entry_name.get()
        age = int(self.entry_age.get()) * 2
        status = self.radio_1.get()

        with open('records.csv', 'a', newline='') as records:
            content = csv.writer(records)
            content.writerow([name, age, status])

        self.entry_name.delete(0,END)
        self.entry_age.delete(0, END)
        self.radio_1.set("NONE")
