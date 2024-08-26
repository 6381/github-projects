import random


def game():
  while True:
    user_input=input("Enter rock,paper or scissors:")
    while user_input not in ['rock','paper','scissors']:
     user_input=input("Invalid input. Please enter rock,paper,scissors")
    computer_choice=random.choice(['rock','paper','scissors'])
    print(f"you chose {user_input},computer chose {computer_choice}")
    if user_input==computer_choice:
        print("It's a tie")
    else:
        if user_input=='rock':
            if computer_choice=='paper' :
                print("computer WINS")
            else:
                print('user_input WINS')
        elif user_input=='paper':
            if computer_choice=='rock' :
                print('user WINS')
            else:
                print("computer WINS")
        elif user_input=='scissors':
            if computer_choice=='paper':
                print('user WINS')
            else:
                print(('computer WINS'))
        play_again=input("Play again? yes/no:").lower()
        while play_again not in ['yes','no']:
            play_again=input("Invalid input,please select yes or no")
        if play_again!='yes':
                break
game()