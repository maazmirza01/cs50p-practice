import re

email = input("Whats your Email? ").strip()

if re.search(r"^.*@.*\.edu$", email):
    print("Valid!")
else:
    print("Invalid!")

if re.search(r"^[a-zA-Z0-9_]+@\w+\.edu$", email, re.IGNORECASE):
    print("Valid!")
else:
    print("Invalid!")