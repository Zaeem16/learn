from validator_collection import validators, errors

def main():
    print(email_validater(input("What's your Email Address? ")))

def email_validater(email):
    try:
        email_validation = validators.email(email)
    except (errors.EmptyValueError, errors.CannotCoerceError, errors.InvalidEmailError) :
        return "Invalid"
    else:
        return "Valid"



if __name__ == "__main__":
    main()

