from gui import *
import csv

'''
~~~~ functions.py is no longer used, methods now located at bottom of gui.py ~~~~
'''

'''
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
'''
