import random

print("Welcome to hangman")
print("-----------------------------------")

wordDict = ["gold","warrior","hi"]

##Choose random word
randomWord = random.choice(wordDict)

for i in randomWord:
    print("_", end=" ")

def print_hangman(wrong):
    if wrong == 0:
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif wrong == 1:
        print("\n+---+")
        print("O   |")
        print("    |")
        print("    |")
        print("   ===")
    elif wrong == 2:
        print("\n+---+")
        print("O   |")
        print("|   |")
        print("    |")
        print("   ===")
    elif wrong == 3:
        print("\n+---+")
        print(" O   |")
        print("/|   |")
        print("     |")
        print("    ===")
    elif wrong == 4:
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("     |")
        print("    ===")
    elif wrong == 5:
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("/    |")
        print("    ===")
    elif wrong == 6:
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("    ===")

def printWord(guessedLetters):
    counter = 0
    rightLetters = 0
    for char in randomWord:
        if char in guessedLetters:
            print(randomWord[counter], end=" ")
            rightLetters += 1
        else:
            print(" ",end=" ")
        counter += 1
    return rightLetters

def print_Lines():
    print("\r")
    for char in randomWord:
        print("\u203E", end=" ")

lenght_of_Word_to_guess = len(randomWord)
times_of_wrong = 0
current_guessed_index = 0
current_letters_guessed = []
current_letters_right = 0

while(times_of_wrong != 6 and current_letters_right != lenght_of_Word_to_guess):
    print("\nLeeters guessed so far: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")

    letterGuessed = input("\nGuess a letter: ")
    if(randomWord[current_guessed_index] == letterGuessed):
        print_hangman(times_of_wrong)
        current_guessed_index += 1
        current_letters_guessed.append(letterGuessed)
        current_letters_right = printWord(current_letters_guessed)
        print_Lines()
    
    else:
        times_of_wrong += 1
        current_letters_guessed.append(letterGuessed)
        print_hangman(times_of_wrong)
        current_letters_right = printWord(current_letters_guessed)
        print_Lines()


print("Game is over! Thank for playing ^_^")
