import random
import string

def random_case(text):
    rand_case_text = ""

    for char in text:
        case = random.randint(0, 1)

        if case == 1:
            rand_case_text += char.upper()
    return rand_case_text

def generate_password():
    max_length = int(input("Max password length: "))
    contains_special = input("""Use special characters (e.g. !@#$%^&*)? (y/n): """).lower()

    letters = string.ascii_lowercase
    numbers = string.digits
    special_chars = "!@#$%^&*=+-_/"

    if contains_special == "y" or contains_special == "yes":
        all_chars = letters + numbers + special_chars
    else:
        all_chars = letters + numbers

    password = ""

    for i in range(max_length):
        password += random.choice(all_chars)

    return password

if __name__ == "__main__":
    password = generate_password()
    print(password)