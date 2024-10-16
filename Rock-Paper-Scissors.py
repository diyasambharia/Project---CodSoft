import random

print('Rules for ROCK PAPER SCISSORS:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")


while True:
    print("\nChoose your option: \n 1 - Rock \n 2 - Paper \n 3 - Scissors")

    
    choice = int(input("Enter your choice (1/2/3): "))
    while choice not in [1, 2, 3]:
        choice = int(input('Please enter a valid choice (1/2/3): '))

    
    choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
    user_choice_name = choices[choice]
    print(f'Your choice: {user_choice_name}')

    
    comp_choice = random.randint(1, 3)
    comp_choice_name = choices[comp_choice]
    print(f"Computer's choice: {comp_choice_name}")

    
    print(f'{user_choice_name} vs {comp_choice_name}')

   
    if choice == comp_choice:
        result = "DRAW"
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        result = comp_choice_name
    else:
        result = user_choice_name

    
    if result == "DRAW":
        print("<== It's a tie! ==>")
    elif result == user_choice_name:
        print("<== You win! ==>")
    else:
        print("<== Computer wins! ==>")

    
    replay = input("Play again? (Y/N): ").lower()
    if replay == 'n':
        break

print("Thanks for playing!")
