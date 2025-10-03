import random
import copy

# Dice function
def roll_d6():
    return random.randint(1, 6)

def roll_d8():
    return random.randint(1, 8)

# Dictionary  for storing player information
player_template = {
    "name": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": []
}

# Setup
winning_score = 3
number_of_players = int(input("How many players? "))

# Create players list
players = []
for i in range(number_of_players):
    player = copy.deepcopy(player_template)
    player["name"] = input(f"What is the name of Player {i+1}? ")
    player["email"] = input(f"What is the email of Player {i+1}? ")
    player["country"] = input(f"What is the country of Player {i+1}? ")
    players.append(player)

round_number = 0
gameover = False

# Game loop
while not gameover:
    round_number += 1
    print(f"\nRound {round_number}:")
    input("Press ENTER to roll the dice...")

    current_totals = []

    # Roll two dice for each player
    for player in players:
        roll1 = roll_d6()
        roll2 = roll_d8()
        total = roll1 + roll2
        player["rolls"].append((roll1, roll2))
        current_totals.append(total)
        print(f"{player['name']} rolled: {roll1} + {roll2} = {total}")

    # Determine winners
    max_total = max(current_totals)
    winners = []
    for idx, player in enumerate(players):
        if current_totals[idx] == max_total:
            winners.append(player["name"])
            player["wins"] += 1

    print(f"Winners of this round: {', '.join(winners)}")

    # Show scores
    for player in players:
        print(f"{player['name']} score: {player['wins']}")

    # Check if someone won
    for player in players:
        if player["wins"] == winning_score:
            print(f"\n{player['name']} wins the game! It took {round_number} rounds.")
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

for player in players:
    print(f"{player['name']} |", end=" ")
    for rolls in player["rolls"]:
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

    for player in players:
        file.write(f"{player['name']} |")
        for rolls in player["rolls"]:
            file.write(f" {rolls[0]}+{rolls[1]} |")
        file.write(f" Wins: {player['wins']}\n")

    file.write("\nDice types rolled: d6 + d8 for all players in this game\n")

print(f"\nGame summary successfully saved to {filename}")
