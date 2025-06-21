import random

input_map = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors',
    'l': 'lizard',
    'v': 'spock'
}

rules = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['spock', 'paper'],
    'spock': ['scissors', 'rock']
}

fun_facts = {
    'rock': "🪨  Rock crushes scissors and crushes lizard!",
    'paper': "📄 Paper covers rock and disproves Spock!",
    'scissors': "✂️  Scissors cuts paper and decapitates lizard!",
    'lizard': "🦎 Lizard eats paper and poisons Spock!",
    'spock': "🖖 Spock smashes scissors and vaporizes rock!"
}

player_win_messages = [
    "You're on fire! 🔥",
    "Unstoppable! 💪",
    "Nice moves, champ! 🏅"
]

computer_win_messages = [
    "Try harder! 😏",
    "The machine is learning... 🤖",
    "Oops, gotcha again! 😬"
]

def determine_winner(player, computer):
    if player == computer:
        return "Ugh it's a tie 🪢", 0, 0
    elif computer in rules[player]:
        return "You win 🏆", 1, 0
    else:
        return "You lose 👎", 0, 1

player_score = 0
computer_score = 0
win_streak = 0
last_result = None

while True:
    player_input = input("Choose: (r)ock, (p)aper, (s)cissors, (l)izard, (v)spock or 'q' to quit: ").lower()

    if player_input == 'q':
        print("Thanks for playing!")
        break

    if player_input not in input_map:
        print("Invalid input. Try again.")
        continue

    player_choice = input_map[player_input]
    computer_choice = random.choice(list(input_map.values()))

    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    print(fun_facts[player_choice])
    print(fun_facts[computer_choice])

    result, p_win, c_win = determine_winner(player_choice, computer_choice)
    player_score += p_win
    computer_score += c_win

    if p_win:
        if last_result == 'player':
            win_streak += 1
        else:
            win_streak = 1
        last_result = 'player'
    elif c_win:
        if last_result == 'computer':
            win_streak += 1
        else:
            win_streak = 1
        last_result = 'computer'
    else:
        win_streak = 0
        last_result = None

    print(result)

    if win_streak >= 2:
        if last_result == 'player':
            print(random.choice(player_win_messages))
        elif last_result == 'computer':
            print(random.choice(computer_win_messages))

    print(f"Score — You: {player_score} | Computer: {computer_score}")
    print("-" * 40)
