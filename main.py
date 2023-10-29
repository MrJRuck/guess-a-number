import random
random_int = random.randint(1, 100)
print("Welcome to the Number Guessing Game!", "I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
def get_guesses():
  guesses = 0
  if difficulty == "easy":
    return guesses + 10
  else:
    return guesses + 5

def guess_num(game_difficulty):
  game_over = False
  guesses_remaining = get_guesses()
  while not game_over:
    guess = int(input("Make a guess:" ))
    if guess == random_int:
      print(f"You got it! The answer was {guess}.")
      game_over = True
      print("Game over")
    elif guess > random_int:
      print("Too high.")
    else:
      print("Too low.")
    guesses_remaining -= 1
    print(f"You have {guesses_remaining} guesses remaining")
    if guesses_remaining == 0:
      game_over = True
      print("Game over")
guess_num(difficulty)