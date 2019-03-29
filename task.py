import csv
import datetime
import os


from tools import Clean


class Task:

    def __init__(self):
        # Verify correct date input
        while True:
            task_date = input("Date of task. \nPlease use DD/MM/YYYY format: ")
            try:
                task_date = datetime.datetime.strptime(task_date, "%d/%m/%Y")
                if task_date > datetime.datetime.now():
                    print("That date hasn't happen yet. Please try again")
                    continue
                else:
                    break
            except ValueError:
                print("That's not a valid format. Please try again")
        self.task_date = task_date
        # clear screen and check that a string title is added
        Clean()
        while True:
            title = input("Title of task: ")
            if not title.strip():
                print("Empty String! Please write task's title")
            else:
                break
        self.title = title
        # Task time check as integer
        Clean()
        while True:
            time_minutes = input("Time spent (rounded minutes): ")
            try:
                time_minutes = int(time_minutes)
                break
            except ValueError:
                print("Please enter a valid number")
        self.time_minutes = time_minutes
        # input notes  freestyle
        Clean()
        notes = input("Notes (optional): ")
        self.notes = notes
        Clean()
        leave = input("The entry was added. Press anything to continue\n")
        Clean()


    def show_task(self):
        for key, value in self.__dict__.items():
            print(key,":",value)

    def in_out_task(self):
        # detects previous log_file.csv file in directory
        presence_file = os.path.isfile("log_file.csv")
        # if present read file to a dict
        if presence_file == True:
            print("Read CSV")
        # if not present create the csv file
        else:
            print("Write CSV")
            with open('log_file.csv', 'w') as out:
                w = csv.DictWriter(out, delimiter="\t", fieldnames = self.__dict__.keys())
                w.writeheader()
                w.writerow(self.__dict__)
