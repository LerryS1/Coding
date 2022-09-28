import random
turns = ['rock', 'paper', 'scissors']
human_turns = []
computer_turns = []
computer_wins = 0
human_wins = 0


while(True):
    human_turn = input("Enter your turn, or type exit: ")
    computer_turn = random.choice(turns)

    human_turns.append(human_turn)
    computer_turns.append(computer_turn)

    if human_turn == 'exit':
        print('Thank you for playing! Bye bye')
        break

    print(f'Human:{human_turn} vs. Computer:{computer_turn}')
    if human_turn == computer_turn:
        print('Draw!')
    elif human_turn == 'rock' and computer_turn == 'scissors':
        print('Human wins!')
        human_wins=human_wins + 1
    elif human_turn == 'paper' and computer_turn == 'rock':
        print('Human wins!')
        human_wins=human_wins + 1
    elif human_turn == 'scissors' and computer_turn == 'paper':
        print('Human wins!')
        human_wins=human_wins + 1
    else:
        print('Computer wins!')
        computer_wins=computer_wins + 1



print(f'You have played {len(human_turns)} times')
print(human_turns)
print(computer_turns)
print(f'Human won {human_wins} times!')
print(f'Computer won {computer_wins} times!')
