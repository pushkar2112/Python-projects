import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')


print('Welcome to the Guessing Game!!')
print('Do you want to guess or let the computer guess??  (M/C)')

while True:
    ch = input().lower()
    if ch in ['m', 'c']:
        if ch == 'm':
            lim = int(input('Enter a limit: '))
            guess(lim)
            break
        elif ch == 'c':
            lim = int(input('Enter a limit: '))
            print('P.S.: Try to be honest!!')
            computer_guess(lim)
            break

    else:
        print('That is not a valid input. Try again...')
        continue
