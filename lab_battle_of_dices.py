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


player1_score = 0
player2_score = 0
round_number = 0
gameover = False

while not gameover:
    round_number += 1
    input("\nPress Enter to roll the dice...")

    
    player1_roll1 = roll_d6()
    player1_roll2 = roll_d8()
    player1_total = player1_roll1 + player1_roll2

    
    player2_roll1 = roll_d6()
    player2_roll2 = roll_d8()
    player2_total = player2_roll1 + player2_roll2

    print("Player 1 rolled:", player1_roll1, "+", player1_roll2, "=", player1_total)
    print("Player 2 rolled:", player2_roll1, "+", player2_roll2, "=", player2_total)

    
    if player1_total > player2_total:
        player1_score += 1
        winner = "Player 1"
    elif player2_total > player1_total:
        player2_score += 1
        winner = "Player 2"
    else:
        winner = "Tie"

    print("Winner of this round:", winner)
    print("Player 1 score:", player1_score)
    print("Player 2 score:", player2_score)

    
    if player1_score == 3:
        print("\n Player 1 is fighting for the win! It took", round_number, "rounds.")
        gameover = True
    elif player2_score == 3:
        print("\n Player 2 is crushing the field! It took", round_number, "rounds.")
        gameover = True
    else:
        print("\n The Battle of dices is at its peak!")
