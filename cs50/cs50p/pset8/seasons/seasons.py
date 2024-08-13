from datetime import datetime, date
import sys
import inflect

p = inflect.engine()

class Birthday:

    def __init__(self, input):
        self.input = input
        try:
            self.date_object = datetime.strptime(self.input, "%Y-%m-%d")
        except ValueError:
            sys.exit("Invalid Date")


    def get_current_date(self):
        return date.today()

    def calculate_difference(self):
        current_date = self.get_current_date()
        birth_date = self.date_object.date()
        if current_date < birth_date:
            sys.exit("Invalid date")
        difference = current_date - birth_date
        minutes = round(difference.days * 1440)
        return f"{p.number_to_words(minutes, andword='').capitalize()} minutes"



def main():
    date = input("Date of birth: ")
    birthday = Birthday(date)
    print(birthday.calculate_difference())






if __name__ == "__main__":
    main()
