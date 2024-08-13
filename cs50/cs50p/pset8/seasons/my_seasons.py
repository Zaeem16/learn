

from datetime import datetime, date
import sys
import inflect

def main():
    date = input("Date of birth: ")
    print(validate_date(date))



def validate_date(date):
    date_format = datetime.strptime(date, "%Y-%m-%d")
    return date_format
