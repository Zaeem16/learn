from datetime import datetime
months = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" :8,
    "September" :9,
    "October" : 10,
    "November" :11,
    "December" : 12
}

while True:
    try:
        date = input("Date: ")
        date_object = datetime.strptime(date, "%B %d, %Y")
        formatted_date = date_object.strftime("%Y-%m-%d")
        print(formatted_date)
        break
    except ValueError:
        try:
            date_object = datetime.strptime(date, "%m/%d/%Y")
            formatted_date = date_object.strftime("%Y-%m-%d")
            print(formatted_date)
            break

        except ValueError:
            pass
    except EOFError:
        print()
        break
