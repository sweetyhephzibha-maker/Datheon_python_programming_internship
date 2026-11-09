
import random


# English word list
words = [
    "PYTHON",
    "COMPUTER",
    "PROGRAM",
    "SCIENCE",
    "DATABASE",
    "KEYBOARD",
    "FUNCTION",
    "VARIABLE",
    "ALGORITHM",
    "SOFTWARE",
    "HARDWARE",
    "INTERNET",
    "DEVELOPER",
    "LANGUAGE",
    "EDUCATION"
]


# ASCII Hangman stages
def display_hangman(wrong_guesses):

    stages = [
        """
         +---+
         |   |
             |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
         |   |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|   |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
        /    |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
        / \\  |
        =========
        """
    ]

    print(stages[wrong_guesses])


# Display correctly guessed letters
def display_word(secret_word, guessed_letters):

    display = ""

    for letter in secret_word:

        if letter in guessed_letters:
            display = display + letter + " "
        else:
            display = display + "_ "

    return display


# Main Hangman game
def play_hangman():

    # Select a random secret word
    secret_word = random.choice(words)

    # Store previously guessed letters
    guessed_letters = set()

    # Maximum incorrect attempts
    max_attempts = 6

    # Initial incorrect guesses
    wrong_guesses = 0

    print("\n===================================")
    print("       HANGMAN WORD GAME")
    print("===================================")

    print("\nGuess the hidden English word!")
    print("You have 6 incorrect attempts.")

    # Game loop
    while wrong_guesses < max_attempts:

        # Display current Hangman stage
        display_hangman(wrong_guesses)

        # Display masked word
        print("Hidden Word:", display_word(
            secret_word, guessed_letters))

        # Display guessed letters
        print("Guessed Letters:", sorted(guessed_letters))

        # Display remaining attempts
        print("Remaining Attempts:",
              max_attempts - wrong_guesses)

        # Get user input
        guess = input("\nEnter one letter: ").strip().upper()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():

            print("Invalid input! Enter only one alphabet letter.")
            continue

        # Check duplicate guesses
        if guess in guessed_letters:

            print("You already guessed this letter!")
            print("No penalty deducted.")
            continue

        # Store guessed letter
        guessed_letters.add(guess)

        # Check whether the letter is in the secret word
        if guess in secret_word:

            print("Correct guess!")

        else:

            print("Incorrect guess!")
            wrong_guesses += 1

        # Check winning condition
        if all(letter in guessed_letters
               for letter in secret_word):

            print("\n===================================")
            print("       CONGRATULATIONS!")
            print("          YOU WON!")
            print("===================================")

            print("Correct Word:", secret_word)
            print("Wrong Attempts:", wrong_guesses)

            return

    # Display final Hangman drawing
    display_hangman(wrong_guesses)

    # Losing condition
    print("\n===================================")
    print("             GAME OVER")
    print("===================================")

    print("You have used all 6 incorrect attempts.")
    print("The correct word was:", secret_word)

output
================================
      HANGMAN WORD GAME
================================

Guess the hidden word!
You have 6 incorrect attempts.
Enter one letter at a time.


         +---+
         |   |
             |
             |
             |
        =========
        
Word: _ _ _ _ _ _ _ 
Guessed letters: []
Remaining attempts: 6

Enter a letter: s
Wrong guess!

         +---+
         |   |
         O   |
             |
             |
        =========
        
Word: _ _ _ _ _ _ _ 
Guessed letters: ['S']
Remaining attempts: 5


# Program execution
if __name__ == "__main__":

    play_hangman()
