import random

comp_wins = 0
player_wins = 0

def Choose_Option():
    user_choice = input("Choose Rock, Paper or Scissors: ")
    if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "r"
        print("You Chose Rock!")
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
    elif user_choice in ["Paper", "paper", "p", "P"]:
        user_choice = "p"
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
    elif user_choice in ["Scissors", "scissors", "s", "S"]:
        user_choice = "s"
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)
    else:
        print("I Do not understand. Please enter a vaild input.")
        Choose_Option()
    return user_choice

def Computer_Option():
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice


while True:
    print("")

    user_choice = Choose_Option()
    comp_choice = Computer_Option()

    print("")

    if user_choice == "r":
        if comp_choice == "r":
            print("You chose rock. The computer also chose rock. You tied.")
            print("""
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            """)
        elif comp_choice == "p":
            print("You chose rock. The computer chose paper. You lose.")
            comp_wins += 1
            
            print("""
                 _______
            ---'    ____)____
                       ______)
                      _______)
                     _______)
            ---.__________)
            """)

        elif comp_choice == "s":
            print("You chose rock. The computer chose scissors. You win.")
            player_wins += 1
            
            print("""
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            """)

    elif user_choice == "p":
        if comp_choice == "r":
            print("You chose paper. The computer chose rock. You win.")
            player_wins += 1

            print("""
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            """)

        elif comp_choice == "p":
            print("You chose paper. The computer chose paper. You tied.")

            print("""
                 _______
            ---'    ____)____
                       ______)
                      _______)
                     _______)
            ---.__________)
            """)

        elif comp_choice == "s":
            print("You chose paper. The computer chose scissors. You lose.")
            comp_wins += 1
            print("""
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            """)

    elif user_choice == "s":
        if comp_choice == "r":
            print("You chose scissors. The computer chose rock. You lose.")
            comp_wins += 1
            print("""
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            """)

        elif comp_choice == "p":
            print("You chose scissors. The computer chose paper. You win.")
            player_wins += 1
            
            print("""
                 _______
            ---'    ____)____
                       ______)
                      _______)
                     _______)
            ---.__________)
            """)


        elif comp_choice == "s":
            print("You chose scissors. The computer chose scissors. You tied.")
            
            print("""
                _______
            ---'   ____)____
                      ______)
                   __________)w
                  (____)
            ---.__(___)
            """)

    print("")
    print("Player wins: " + str(player_wins))
    print("Computer wins: " + str(comp_wins))
    print("")

    user_choice = input("Do you want to play again? (y/n)")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "no", "No"]:
        break
