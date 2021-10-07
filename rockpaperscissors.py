from random import choice

options = ['rock', 'paper', 'scissors']

answer = input("Please choose rock, paper or scissors: ")
opponent = choice(options)

if answer == 'rock' and opponent == 'rock':
    print("Tie! You both chose rock.")
elif answer == 'rock' and opponent == 'paper':
    print("You lose! Paper covers rock.")
elif answer == 'rock' and opponent == 'scissors':
    print("You win! Rock crushes scissors.")
elif answer == 'paper' and opponent == 'paper':
    print("Tie! You both chose paper.")
elif answer == 'paper' and opponent == 'rock':
    print("You win! Paper covers rock.")
elif answer == 'paper' and opponent == 'scissors':
    print("You lose! Scissors cut paper")
elif answer == 'scissors' and opponent == 'scissors':
    print("Tie! You both chose scissors.")
elif answer == 'scissors' and opponent == 'rock':
    print("You lose! Rock crushes scissors.")
elif answer == 'scissors' and opponent == 'paper':
    print("You win! Scissors cut paper.")
