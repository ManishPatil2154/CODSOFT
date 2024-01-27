import random

options = ["rock", "scissor", "paper"]

while True:
    computer_count = 0
    user_count = 0
    
    user_input = input('''
Game Start....
1. Yes
2. No | Exit   
''')
    
    if user_input == '1':
        for _ in range(5):
            u_choice = int(input('''
1. Rock            
2. Scissor            
3. Paper            
'''))
            
            if u_choice == 1:
                u_choice = "rock"
            elif u_choice == 2:
                u_choice = "scissor"
            elif u_choice == 3:
                u_choice = "paper"
            else:
                print("Invalid choice. Try again.")
                continue

            C_choice = random.choice(options)

            print("User's Choice:", u_choice)
            print("Computer's Choice:", C_choice)

            if C_choice == u_choice:
                print("Game Draw")
            elif (u_choice == "rock" and C_choice == "scissor") or (
                u_choice == "paper" and C_choice == "rock") or (
                u_choice == "scissor" and C_choice == "paper"):
                print("You Win")
                user_count += 1
            else:
                print("Computer Wins")
                computer_count += 1

        print("Final Game Results:")
        print("User Score:", user_count)
        print("Computer Score:", computer_count)

        if user_count > computer_count:
            print("Congratulations! You WIN the Game!")
        elif user_count < computer_count:
            print("Sorry, Computer WINS the Game!")
        else:
            print("The Game is a DRAW!")

    elif user_input == '2':
        break

    else:
        print("Invalid choice. Please enter 1 or 2.")
