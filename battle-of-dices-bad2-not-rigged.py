import random

# Scores
player1_score = 0
player2_score = 0

# Save the rolls
player1_rolls = []
player2_rolls = []

# Round 1
player1_roll1 = random.randint(1, 6)
player2_roll1 = random.randint(1, 6)
player1_rolls.append(player1_roll1)
player2_rolls.append(player2_roll1)
print("Player 1 rolled:", player1_roll1)
print("Player 2 rolled:", player2_roll1)

if player1_roll1 > player2_roll1:
    player1_score += 1
    winner = "Player 1"
elif player2_roll1 > player1_roll1:
    player2_score += 1
    winner = "Player 2"
else:
    winner = "Tie"

print("Winner of this round:", winner)
print("Player 1 score:", player1_score)
print("Player 2 score:", player2_score)
print()

# Round 2
player1_roll2 = random.randint(1, 6)
player2_roll2 = random.randint(1, 6)
player1_rolls.append(player1_roll2)
player2_rolls.append(player2_roll2)
print("Player 1 rolled:", player1_roll2)
print("Player 2 rolled:", player2_roll2)

if player1_roll2 > player2_roll2:
    player1_score += 1
    winner = "Player 1"
elif player2_roll2 > player1_roll2:
    player2_score += 1
    winner = "Player 2"
else:
    winner = "Tie"

print("Winner of this round:", winner)
print("Player 1 score:", player1_score)
print("Player 2 score:", player2_score)
print()

# Round 3
player1_roll3 = random.randint(1, 6)
player2_roll3 = random.randint(1, 6)
player1_rolls.append(player1_roll3)
player2_rolls.append(player2_roll3)
print("Player 1 rolled:", player1_roll3)
print("Player 2 rolled:", player2_roll3)

if player1_roll3 > player2_roll3:
    player1_score += 1
    winner = "Player 1"
elif player2_roll3 > player1_roll3:
    player2_score += 1
    winner = "Player 2"
else:
    winner = "Tie"

print("Winner of this round:", winner)
print("Player 1 score:", player1_score)
print("Player 2 score:", player2_score)
print()

# Game commentary 
if player1_score == 3:
    print("\n Player 1 is fighting for the win!")
elif player2_score == 3:
    print("\n Player 2 is crushing the field")
else:
    print("\n The Battle of dices is on it's peak!") 

# Round-by round table
print("\nRound-by-Round Summary:")
print("-------------------------")
print("Round    | 1 | 2 | 3 |")
print("Player 1 |", player1_rolls[0], "|", player1_rolls[1], "|", player1_rolls[2], "|")
print("Player 2 |", player2_rolls[0], "|", player2_rolls[1], "|", player2_rolls[2], "|")
