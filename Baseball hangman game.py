import random

def choose_word():
    words = ["Judge", "Jeter", "Babe", "Mantle", "Yogi", "Elston", "Mo"]
    return random.choice (words)

def display_word(word, guessed_letters):
    display = "" 
    for letter in word:
        if letter in guessed_letters:

            display += "_"
            return display
        
def hangman():
    word = choose_word()

    guessed_letters = []
    attempts = 6

    print("Welcome to Baseball Hangman!")

    print(display_word(word, guessed_letters))

    while True: guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        
        print("Please enter a single letter.")   
    
        if guess in guessed_letters:
            
            print("That letter has already been guessed.")

        guessed_letters.append(guess)

        if guess not in word: attempts -= 1

        print("You have guessed wrong. You have {} attempts left.".formatattempts)

        if attempts == 0:

            print("You have no more attemps. The word was'{}'.".format(word))

        else:

            print("You are correct!")

            if all(letter in guessed_letters for letter in word):

                print("We have a winner! You have guessed the word'{}'!".format(word))

                print(display_word(word, guessed_letters))

                if __name__ == "__main__": hangman()