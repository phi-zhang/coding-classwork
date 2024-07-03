# This program allows the user to play New York Times' game Wordle. The
# objective is to guess a the 5-letter word, chosen from a provided text
# file, within 6 guesses.
# Written for COMPSCI 101.

def main():
    filename = input("Enter the name of the word file: ")
    play_game(filename)

def play_game(filename):
    words_list = get_words(filename)
    print_welcome()
    print_rules()
    round_number, correct_count, continue_round = 0, 0, 'Y'
    data_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    while continue_round != 'N':
        puzzle_word = get_random_word(words_list)
        round_number += 1
        print()
        print("Round:", round_number)
        print()
        guess_count, correctness = play_round(puzzle_word)
        print_success_message(correctness, puzzle_word)
        continue_round = get_confirmation()
        if correctness == True:
            correct_count += 1
            data_dict[guess_count] += 1
    print_summary(correct_count, round_number, data_dict)

def get_words(filename):
    input_file = open(filename, 'r')
    words_list = input_file.read().split()
    input_file.close()
    return words_list

def print_welcome():
    name = input("Please enter your name: ")
    print()
    print("Welcome to Wordle 101", name)
    print()

def print_rules():
    print("========================================================================")
    print("                                 Rules")
    print("You have 6 guesses to figure out the solution.")
    print("All solutions are words that are 5 letters long.")
    print("Words may include repeated letters.")
    print("Letters that have been guessed correctly are displayed in uppercase.")
    print("Letters that are in the word but have been guessed in the wrong location")
    print("are displayed in lowercase.")
    print("========================================================================")
    print()

def play_round(puzzle_word):
    game_state = "_ _ _ _ _"
    guess_count = 1
    print(f"Guess {guess_count}:")
    print()
    guess = get_player_guess()
    while puzzle_word != guess and guess_count < 6:
        game_state = update_game_state(puzzle_word, guess)
        guess_count += 1
        print(game_state)
        print()
        print(f"Guess {guess_count}:")
        print()
        guess = get_player_guess()
    print(update_game_state(puzzle_word, guess))
    print()
    return guess_count, puzzle_word == guess

def get_player_guess():
    guess = input("Please enter your guess: ")
    while len(guess) != 5 or guess.isalpha() == False:
        guess = input("Your guess must have 5 letters: ")
    return guess.lower()

def update_game_state(puzzle_word, guess):
    new_game_state = ['_', '_', '_', '_', '_']
    remaining_letters_dict = {}
    remaining_indices = [0, 1, 2, 3, 4]
    for letter in guess:
        remaining_letters_dict[letter] = puzzle_word.count(letter)
    for index in range(5):
        if guess[index] == puzzle_word[index]:
            new_game_state[index] = guess[index].upper()
            remaining_indices.pop(remaining_indices.index(index))
            remaining_letters_dict[guess[index]] -= 1
    for index in remaining_indices:
        if (guess[index] in puzzle_word and
            remaining_letters_dict[guess[index]] > 0):
            new_game_state[index] = guess[index].lower()
            remaining_letters_dict[guess[index]] -= 1
    return " ".join(new_game_state)

def print_success_message(correctness, puzzle_word):
    if correctness == True:
        print(f"Success! The word is {puzzle_word}!")
        print()
    else:
        print(f"Better luck next time! The word is {puzzle_word}!")
        print()

def get_confirmation():
    prompt = "Please enter 'Y' to continue or 'N' to stop playing: "
    answer = input(prompt)
    while answer not in ['Y', 'N']:
        print("Only enter 'Y' or 'N'!")
        answer = input(prompt)
    return answer

def print_summary(correct_count, round_number, data_dict):
    from math import ceil
    win_percentage = ceil(correct_count / round_number * 100)
    print()
    print("========================================================================")
    print("                                Summary")
    print(f"Win percentage: {win_percentage}%")
    print("Win Distribution:")
    print_bar_chart(data_dict)
    print("========================================================================")

def print_bar_chart(data_dict):
    for key, value in sorted(data_dict.items()):
        print(str(key) + '|' + '#' * value + str(value))

import random

def get_random_word(words):
    random_index = random.randrange(len(words))
    return words[random_index]
