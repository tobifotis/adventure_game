print("**********************************")
print("* CHOOSE YOUR OWN ADVENTURE GAME *")
print("**********************************\n")
name = input("Enter your name: ")
print(f"Hello {name}, welcome to the beautiful game!\n")

should_we_play = input("Do you want to play? ").lower()

if should_we_play == "yes" or should_we_play == "y":
    print("lets gooooo!\n")

    direction = ""
    while direction != "right" and direction != "left":  # Keep looping until the user enters "left" or "right"
        # Ask the user for input
        direction = input("Do you want to go left or right? ('left'/'right') ").lower()

        if direction == "left":
            print("You went left and fell off a cliff, game over!")
        elif direction == "right":

            choice = ""
            while choice != "swim" and choice != "cross":  # Keep looping until the user enters "swim" or "cross"
                choice = input(
                    "\nOkay, you now see a bridge, do you want to swim under it or cross it? ('swim'/'cross') ").lower()

                if choice == "swim":
                    print("You got eaten by an alligator, game over!")
                elif choice == "cross":
                    print("You found the gold and won!")
                else:
                    print("\nInvalid choice. Please choose 'swim' or 'cross'\n")

        else:
            print("Invalid input. Please choose 'left' or 'right'\n")

else:
    print("Maybe next time! Game over.")
