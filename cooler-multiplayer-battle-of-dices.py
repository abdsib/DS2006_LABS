import random

# Dice functions
def roll_d6():
    return random.randint(1, 6)

def roll_d8():
    return random.randint(1, 8)

# Setup
winning_score = 3
number_of_players = int(input("How many players? "))

# Saving player scores and roll history
player_wins = [0] * number_of_players
player_rolls_history = [[] for _ in range(number_of_players)]

round_number = 0
gameover = False

# Game loop
while not gameover:
    round_number += 1
    print(f"\nRound {round_number}:")
    input("Press ENTER to roll the dice...")

    current_totals = []

    # Roll dice for each player
    for i in range(number_of_players):
        roll1 = roll_d6()
        roll2 = roll_d8()
        total = roll1 + roll2
        current_totals.append(total)
        player_rolls_history[i].append((roll1, roll2))
        print(f"Player {i+1} rolled: {roll1} + {roll2} = {total}")

    # Determine winners
    max_total = max(current_totals)
    winners = []
    for i in range(number_of_players):
        if current_totals[i] == max_total:
            winners.append(f"Player {i+1}")
            player_wins[i] += 1

    print(f"Winners of this round: {', '.join(winners)}")

    # Show scores
    for i in range(number_of_players):
        print(f"Player {i+1} score: {player_wins[i]}")

    # Check if someone won
    for i in range(number_of_players):
        if player_wins[i] == winning_score:
            print(f"\nPlayer {i+1} wins the game! It took {round_number} rounds.")
            gameover = True
            break

    if not gameover:
        print("\nThe Battle of dices is at its peak!")

# Game summary
print("\nGame Summary Table:")
print("-----------------------------")
print("Round    |", end=" ")
for i in range(round_number):
    print(i + 1, end=" | ")
print()

for i in range(number_of_players):
    print(f"Player {i+1} |", end=" ")
    for rolls in player_rolls_history[i]:
        print(f"{rolls[0]}+{rolls[1]}", end=" | ")
    print()

print("\nDice types rolled: d6 + d8 for all players in this game")

# Save results
filename = input("\nEnter the name of the file to save the game summary (should end with .txt): ")

with open(filename, "w") as file:
    file.write("Game Summary Table:\n")
    file.write("-----------------------------\n")
    file.write("Round    |")
    for i in range(round_number):
        file.write(f" {i + 1} |")
    file.write("\n")

    for i in range(number_of_players):
        file.write(f"Player {i+1} |")
        for rolls in player_rolls_history[i]:
            file.write(f" {rolls[0]}+{rolls[1]} |")
        file.write(f" Wins: {player_wins[i]}\n")

    file.write("\nDice types rolled: d6 + d8 for all players in this game\n")

print(f"\nGame summary successfully saved to {filename}")