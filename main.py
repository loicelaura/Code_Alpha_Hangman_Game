import random

# List of words for Hangman Game
words_list = [
    "killer", "assassin", "executor", "headsman", "butcher", "slayer"
]


class Hangman:

    def __init__(self, words_list, max_incorrect_guesses=6):
        self.words_list = words_list
        self.max_incorrect_guesses = max_incorrect_guesses
        self.word = random.choice(self.words_list)
        self.correct_guesses = set()
        self.incorrect_guesses = set()
        self.hints_used = 0


#Function to select a random word from the List
def get_random_word():
    return random.choice(words_list)


# Function to display the current state of the word
def display_word_state(self):
    display = ""
    for letter in self.word:
        if letter in self.correct_guesses:
            display += letter
        else:
            display += "_"
    return display


def is_word_guessed(self):
    return all(letter in self.correct_guesses for letter in self.word)


def get_hint(self):
    unused_letters = [
        letter for letter in self.word if letter not in self.correct_guesses
    ]
    if unused_letters:
        hint = random.choice(unused_letters)
        self.hints_used += 1
        return hint
    return None


def display_hangman(self):
    stages = [
        """
               -----
               |   |
               O   |
              /|\\  |
              / \\  |
                   |
            --------
            """, """
               -----
               |   |
               O   |
              /|\\  |
              /    |
                   |
            --------
            """, """
               -----
               |   |
               O   |
              /|\\  |
                   |
                   |
            --------
            """, """
               -----
               |   |
               O   |
              /|   |
                   |
                   |
            --------
            """, """
               -----
               |   |
               O   |
               |   |
                   |
                   |
            --------
            """, """
               -----
               |   |
               O   |
                   |
                   |
                   |
            --------
            """, """
               -----
               |   |
                   |
                   |
                   |
                   |
            --------
            """
    ]

    return stages[self.max_incorrect_guesses - len(self.incorrect_guesses)]


# Function to play the game
def play(self):
    print("Welcome to Hangman!")
    print(f"The word has {len(self.word)} letters.")

    while len(self.incorrect_guesses) < self.max_incorrect_guesses:
        print(f"\nCurrent word: {self.display_word_state()}")
        print(self.display_hangman())
        print(f"Incorrect guesses: {', '.join(self.incorrect_guesses)}")
        print(
            f"Guesses left: {self.max_incorrect_guesses - len(self.incorrect_guesses)}"
        )
        print(f"Hints used: {self.hints_used}")

        guess = input("Guess a letter (or type 'hint' for a hint): ").lower()

        if guess == 'hint':
            hint = self.get_hint()
            if hint:
                print(f"Hint: Try the letter '{hint}'")
            else:
                print("No more hints available.")
            continue

        if guess in self.correct_guesses or guess in self.incorrect_guesses:
            print("You already guessed that letter. Try again.")
            continue

        if guess in self.word:
            self.correct_guesses.add(guess)
            if self.is_word_guessed():
                print(f"Congratulations! You've guessed the word: {self.word}")
                break
        else:
            self.incorrect_guesses.add(guess)
            print(f"Wrong guess! '{guess}' is not in the word.")

        if len(self.incorrect_guesses) == self.max_incorrect_guesses:
            print(self.display_hangman())
            print(
                f"Game over! You've used all your guesses. The word was: {self.word}"
            )


# List of words for the Hangman game
words_list = [
    "killer", "assassin", "executor", "headsman", "butcher", "slayer"
]
