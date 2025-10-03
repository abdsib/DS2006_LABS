import random

def roll_d4():
    return random.randint(1, 4)

def roll_d6():
    return random.randint(1, 6)

def roll_d8():
    return random.randint(1, 8)

def roll_d12():
    return random.randint(1, 12)

def roll_d20():
    return random.randint(1, 20)

def roll_d100():
    return random.randint(1, 100)

# Scores
player1_score = 0
player2_score = 0
round_number = 0
gameover = False

# Store all rolls
player1_rolls = []
player2_rolls = []

while gameover is False:
    round_number += 1  
    input("\nPress Enter to roll the dice...")

    player1_roll = roll_d6()
    player2_roll = roll_d6()

    # Save the rolls 
    player1_rolls.append(player1_roll)
    player2_rolls.append(player2_roll)

    print("Player 1 rolled:", player1_roll)
    print("Player 2 rolled:", player2_roll)

    if player1_roll > player2_roll:
        player1_score += 1
        winner = "Player 1"
    elif player2_roll > player1_roll:
        player2_score += 1
        winner = "Player 2"
    else:
        winner = "Tie"

    print("Winner of this round:", winner)
    print("Player 1 score:", player1_score)
    print("Player 2 score:", player2_score)

    if player1_score == 3:
        print("\n Player 1 is fighting for the win It took", round_number, "rounds.")
        gameover = True
    elif player2_score == 3:
        print("\n Player 2 is crushing the field It took", round_number, "rounds.")
        gameover = True
    else:
        print("\n The Battle of dices is at its peak!")

# Game commentary 
if player1_score == 3:
    print("\n Player 1 is fighting for the win!")
elif player2_score == 3:
    print("\n Player 2 is crushing the field")
else:
    print("\n The Battle of dices is on it's peak!") 

# Game summary 
print("\nGame Summary Table:")
print("-----------------------------")
print("Round    |", end=" ")
for i in range(len(player1_rolls)):
    print(i + 1, end=" | ")
print()

print("Player 1 |", end=" ")
for roll in player1_rolls:
    print(roll, end=" | ")
print()

print("Player 2 |", end=" ")
for roll in player2_rolls:
    print(roll, end=" | ")
print()

print("\nDice type rolled: d6 for both players in this game")

# Save to a file
filename = input("\nEnter the name of the file to save the game summary (should end with .txt): ")

with open(filename, "w") as file:
    file.write("Game Summary Table:\n")
    file.write("-----------------------------\n")
    
    # Round numbers
    file.write("Round    |")
    for i in range(len(player1_rolls)):
        file.write(f" {i + 1} |")
    file.write("\n")
    
    # Player 1 rolls
    file.write("Player 1 |")
    for roll in player1_rolls:
        file.write(f" {roll} |")
    file.write("\n")
    
    # Player 2 rolls
    file.write("Player 2 |")
    for roll in player2_rolls:
        file.write(f" {roll} |")
    file.write("\n")
    
    # Dice type info
    file.write("\nDice type rolled: d6 for both players in this game\n")

print(f"\nGame summary successfully saved to {filename}")
