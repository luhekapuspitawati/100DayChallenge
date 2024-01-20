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

game = [rock, paper, scissors]

human = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor."))
print(human)
print(game[human])

print("computer choose: ")
computer = random.randint(0,2)
print(computer)
print(game[computer])

if human == 0 and computer == 1 :
    print("You Lose")
elif human == 0 and computer == 2 :
    print("You Win")
elif human == 1 and computer == 0 :
    print("You Win")
elif human == 1 and computer == 2 :
    print("You Lose")
elif human == 2 and computer == 1 :
    print("You Win")
elif human == 2 and computer == 0 :
    print("You Lose")
elif human == computer :
    print("You Draw")