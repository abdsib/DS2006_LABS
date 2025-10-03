import random

# Dice function
def roll_d6():
    return random.randint(1, 6)

# Setup
winning_score = 3
number_of_players = int(input("How many players? "))

# Saving player scores and roll history
player_wins = [0] * number_of_players
player_rolls_history = [[] for _ in range(number_of_players)]

round_number = 0
gameover = False

# Game lopp
while not gameover:
    round_number += 1
    print(f"\nRound {round_number}:")
    input("Press ENTER to roll the dice...")

    current_rolls = []

    # Roll dice for each player
    for i in range(number_of_players):
        roll = roll_d6()
        current_rolls.append(roll)
        player_rolls_history[i].append(roll)
        print(f"Player {i+1} rolled: {roll}")

    # Determine winners
    max_roll = max(current_rolls)
    winners = []
    for i in range(number_of_players):
        if current_rolls[i] == max_roll:
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
    for roll in player_rolls_history[i]:
        print(roll, end=" | ")
    print()

print("\nDice type rolled: d6 for all players in this game")

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
        for roll in player_rolls_history[i]:
            file.write(f" {roll} |")
        file.write("\n")
    file.write("\nDice type rolled: d6 for all players in this game\n")

print(f"\nGame summary successfully saved to {filename}")
