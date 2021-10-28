import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print('Computer chose: ', computer)
        return 'It\'s a tie'

    # r > s, s > p, p > r
    if is_win(user, computer):
        print('Computer chose: ', computer)
        return 'You won!'
        
    print('Computer chose: ', computer)
    return 'You lost!'

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print('Welcome... Let\'s play...')
print(play())