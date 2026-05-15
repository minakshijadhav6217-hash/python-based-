import random
#assume store(books,food)
choices = ["rock","paper","scissors"]
print("@ ROCK PAPER SCISSORS")

while True:
     user = input("\nENTER rock,paper or scissors").lower()
     if user not in choices:
          print("invalied choice")
          continue
     
     computer = random.choice(choices)
     print(f"\nYOU CHOSE: {user}")
     print(f"computer CHOSE:{computer}")
     
     if user == computer:
          print("IT IS A TIE")
     elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
       
       ):
          print("YOU WIN")
     else:
          print("YOU LOSE")
     again = input("\nplay again? (yes/no): ").lower()
     
     if again != "yes":
          print("thanks")
          break
     