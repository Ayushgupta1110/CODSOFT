import random
computer_points = 0
user_points = 0
game_choice_list = ['stone','paper','scissor']
def stone_paper_scissor(user_game_choice):
    global computer_game_choice, user_points , computer_points
    computer_game_choice = random.choice(game_choice_list)
    if user_game_choice == 'stone':
        if computer_game_choice == 'stone':
            return "The match is drawn"
        
        elif computer_game_choice == 'paper':
            computer_points += 1
            return "Computer wins the match "
        else:
            user_points += 1
            return "User wins the match"
        
    elif user_game_choice == 'paper':
        if computer_game_choice == 'paper':
            return "The match is drawn"
        elif computer_game_choice == 'scissor':
            computer_points += 1
            return "Computer wins the match"
        else:
            user_points += 1
            return "User wins the match"
        
    else:
        if computer_game_choice == 'scissor':
            return "The match is drawn"
        elif computer_game_choice == 'stone':
            computer_points += 1
            return "Computer wins the match"
        else:
            user_points += 1
            return "User wins the match"

while True:
    user_game_choice = input("Enter the choice between('stone','paper','scissor'): ").lower()
    if user_game_choice not in game_choice_list:
        print("The entered choice is not a respected choice")
        break
    else:
        print(stone_paper_scissor(user_game_choice))
        print("user choice is : {}".format(user_game_choice))
        print("computer choice is : {}".format(computer_game_choice))


    print("computer score is : {} and the user score is : {}".format(computer_points,user_points))



    further_wish = input("Do you want to play more (type 'yes' or 'no'): ").lower()
    further_choice_list = ["yes","no"]
    if further_wish not in further_choice_list:
        print("the input is not correct")
        break
    elif further_wish == 'no':
        print("thank you for playing")
        if user_points > computer_points:
            print("User has won the game")
        elif user_points < computer_points:
            print("Computer has won the game")
        else :
            print("The game is drawn")
        break
    else :
        continue