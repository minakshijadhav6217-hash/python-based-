import random
#assume store(books,food)
choices = ["rock","paper","scissors"]
print("@ ROCK PAPER SCISSORS")

user_score = 0
comp_score = 0


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
          user_score += 1
     else:
          print("YOU LOSE")
          comp_score += 1
     print(f"score-> you: {user_score}| Computer:{comp_score}")
    
    
     again = input("\nplay again? (yes/no): ").lower()
     
     if again != "yes":
          print("thanks")
          break
     