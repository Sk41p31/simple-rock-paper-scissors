import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

possible_choices = [rock, paper, scissors]
#Write your code below this line 👇

print("Hello there, adventurer! Mind playin' some rock-paper-scissors with againt my top-notch AI?\nNo? Yes? Excellent! We will play anyway lol.")

choice = input("Write your choice! It's either 'rock', 'paper' or 'scissors'!\n")
ai_choice = random.randint(0,2)
player_choice = 0

if choice == 'rock':
  player_choice = 0
elif choice == 'paper':
  player_choice = 1
elif choice == 'scissors':
  player_choice = 2
else:
  print("Damn, you chose something weird, let me do this for you:\n")



print(f"AI choice:\n{possible_choices[ai_choice]}\n")
print(f"Your choice:\n{possible_choices[player_choice]}\n")


# Since the decissions are described by numbers 0, 1, 2,
# we can determine who won by substracting choice numbers
# possible  choices are [rock, paper, scissors]
# and it corresponds to [ 0  ,   1  ,    2    ]

# if the difference is 1 or -2, then we won
if player_choice - ai_choice == 1 or player_choice - ai_choice == -2 :
  print("Congrats! You won!\n")

# if the difference is opposite sign, then we lost
elif player_choice - ai_choice == -1 or player_choice - ai_choice == 2 :
  print("Damn it! You lost!\n")

# otherwise it is a draw
else:
  print("Oh boy! It's a draw!\n")



