import random

# Scores
player1_score = 0
player2_score = 0

# Round 1
player1_round1_roll = random.randint(1, 6)
player2_round1_roll = random.randint(1, 6)
print("Round 1:")
print("Player 1 rolled:", player1_round1_roll)
print("Player 2 rolled:", player2_round1_roll)

if player1_round1_roll > player2_round1_roll:
    player1_score += 1
    winner = "Player 1"
elif player2_round1_roll > player1_round1_roll:
    player2_score += 1
    winner = "Player 2"
else:
    winner = "Tie"
print("Winner of Round 1:", winner)
print("Player 1 score:", player1_score, "Player 2 score:", player2_score)
print()

# Round 2
player1_round2_roll = random.randint(1, 6)
player2_round2_roll = random.randint(1, 6)
print("Round 2:")
print("Player 1 rolled:", player1_round2_roll)
print("Player 2 rolled:", player2_round2_roll)

if player1_round2_roll > player2_round2_roll:
    player1_score += 1
    winner = "Player 1"
elif player2_round2_roll > player1_round2_roll:
    player2_score += 1
    winner = "Player 2"
else:
    winner = "Tie"
print("Winner of Round 2:", winner)
print("Player 1 score:", player1_score, "Player 2 score:", player2_score)
print()

# Round 3
player1_round3_roll = random.randint(1, 6)
player2_round3_roll = random.randint(1, 6)
print("Round 3:")
print("Player 1 rolled:", player1_round3_roll)
print("Player 2 rolled:", player2_round3_roll)

if player1_round3_roll > player2_round3_roll:
    player1_score += 1
    winner = "Player 1"
elif player2_round3_roll > player1_round3_roll:
    player2_score += 1
    winner = "Player 2"
else:
    winner = "Tie"
print("Winner of Round 3:", winner)
print("Player 1 score:", player1_score, "Player 2 score:", player2_score)
print()

# Game commentary
if player1_score == 3:
    print("Player 1 is fighting for the win!")
elif player2_score == 3:
    print("Player 2 is crushing the field!")
else:
    print("The battle of dices is at its peak!")
