import random
def getrandom():
    return random.randrange(1,101)
def random_guess(guess,number):
    if guess==number:
        return "your guess is right"
    elif abs(guess-number)<=10:
        return "you're near to guess"
    else:
        return "you're far to guess"
def run_guess():
    secretNumber=getrandom()
    print("enter the number between 1 and 101")
    while True:
        try:
          user_input=int(input("Enter the guess or type('quit' or 'exit' :"))
        except ValueError:
            print("Invalid input Please enter the number")
            continue
        if user_input<1 and user_input>100:
            print("Enter the number btwn 1 and 100")
            continue

        hint = random_guess(secretNumber, user_input)

        if hint=='Right':
            print("you guessed it right")
            break
        else:
            print(hint)
if __name__ == '__main__':
    run_guess()



