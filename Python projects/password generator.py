import random
import string
import re

def main(lenght):
    characters = string.ascii_letters + string.digits + string.punctuation
    password=''.join(random.choice(characters) for _ in range(lenght))

    return password
def validate_password(password):
    if len(password)<12:
        return False
    if  not re.search("[A-Z]",password):
        return  False
    if not re.search('[0-9]',password):
        return False
    if not re.search("[!@#$%^&*()_+=-{};:'<>,./?]",password):
        return False
    return True
if __name__ == '__main__':
    print(main(1))
    print(main(23))
    if validate_password:
        print('Password is valid')
    else:
        print("Password is not valid")