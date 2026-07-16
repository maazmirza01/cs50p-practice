import validator_collection

def main():
    print(email_validator(input("What's your email? ")))

def email_validator(email):
    if result := validator_collection.is_email(email):
        return "Valid!"
    else:
        return "Invalid!"
    


if __name__ == "__main__":
    main()