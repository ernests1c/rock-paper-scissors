#
# ROCK, PAPER, SCISSORS - Iterācija 1
# 
# 1. Spēle prasa ievadīt ciparu no 1 līdz 3 (izmanto input, https://www.w3schools.com/python/python_user_input.asp)
# 2. Dators iedomājas ciparu no 1 līdz 3  (izmanto random, https://www.w3schools.com/python/ref_random_randint.asp)
# 3. Atkarībā no ievadītajiem cipariem un datora, izdrukā paziņojumu par zaudējumu, uzvaru, vai neizšķirtu (izmanto if, else https://www.w3schools.com/python/python_conditions.asp)
#


Rock = "1"
Scissors = "2"
Paper = "3"
print("Welcome to Rock, Paper, Scissors!")
import random
print("Choose a number from 1 to 3 ")
izveles = ["1", "2", "3"]
player_choice = input("Rock = 1, Scissors = 2, Paper = 3")
print("Your choice is " + player_choice)
player_choice = input
computer = random.choice(izveles)
if player_choice == "1" and computer == "1":
    print("Computer picked 1 - Rock, it's a draw!")
elif player_choice == "2" and computer == "2":
    print("Computer picked 2 - Scissors, it's a draw!")
elif player_choice == "3" and computer == "3":
    print("Computer picked 3 - Paper, it's a draw!")
elif player_choice == "1" and computer == "3":
    print("Computer picked 3 - Paper, it's a loss!")
elif player_choice == "3" and computer == "1":
    print("Computer picked 1 - Rock, it's a win!")
elif player_choice == "2" and computer == "1":
    print("Computer picked 1 - Rock, it's a loss!")
elif player_choice == "1" and computer == "2":
    print("Computer picked 2 - Scissors, it's a win!")
elif player_choice == "3" and computer == "2":
    print("Computer picked 2 - Scissors, it's a loss!")
elif player_choice == "2" and computer == "3":
    print("Computer picked 3 - Paper, it's a win!")
    

    

    

