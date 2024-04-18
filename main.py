import random
import colorama
import re
from english_words import get_english_words_set


words = get_english_words_set(["web2"], lower=True)


def check_for_letter(word: str, letter: str) -> list | None:
    # This function detects if a letter is present in a word and returns an array of len(occurrences) = len(word)
    # That is conformed of boolean statements, True if letter present in position, false if not
    is_present = False
    occurrences = []
    for character in word:
        if character == letter:
            occurrences.append(True)
            is_present = True
        else:
            occurrences.append(False)
    return occurrences if is_present else None


def update_display_word(word: str, guessed_letters: list) -> str | None:
    display_word = ""
    for character in word:
        if character in guessed_letters:
            display_word += f" {character} "
        else:
            display_word += " _ "
    return display_word


if __name__ == "__main__":
    difficulty = 0
    while difficulty not in ["1", "2", "3", "4"]:
        difficulty = input("What difficulty would you like to play? \n"
                               "[1] Easy (3-6 letters) [2] Medium (7-9 letters) "
                               "[3] Hard (10-14 letters) [4] Extreme (>15)\n")
        print(colorama.ansi.clear_screen())
    difficulty = int(difficulty)
    word = random.choice(list(words))
    match difficulty:
        case 1:
            while len(word) > 6:
                word = random.choice(list(words))
        case 2:
            while len(word) < 7 or len(word) > 9:
                word = random.choice(list(words))
        case 3:
            while len(word) < 10 or len(word) > 14:
                word = random.choice(list(words))
        case 4:
            while len(word) < 15:
                word = random.choice(list(words))
    print(f"The word has {len(word)} letters.")
    solved = False
    failed = False
    lives = 5
    guessed_letters = []
    display_word = update_display_word(word, guessed_letters)
    while not solved and not failed:
        print(colorama.ansi.clear_screen(),end="")
        print(colorama.Style.RESET_ALL, display_word)
        print(f"You have {lives} guesses left.")
        print(f"Guessed letters: {guessed_letters}")
        letter = input("Enter a letter: ")
        if letter not in guessed_letters and re.match("^[a-zA-Z]$", letter):
            guessed_letters.append(letter)
            result = check_for_letter(word, letter)
            if result:
                display_word = update_display_word(word, guessed_letters)
                if "_" not in display_word:
                    solved = True
            else:
                print(colorama.Fore.YELLOW, f"letter {letter} not found in word.")
                lives -= 1
                if lives == 0:
                    failed = True
        elif letter in guessed_letters:
            print(colorama.Fore.RED, f"You have already guessed {letter}")
        elif not re.match("^[a-zA-Z]$", letter):
            print(colorama.Fore.RED, f"Input must me only a single alphabetical value")
    if not failed:
        print(colorama.Fore.GREEN, f"The word was {word}!")
        print(colorama.Fore.GREEN, f"Word Guessed in {len(guessed_letters)} attempts.")
    else:
        print(colorama.Fore.RED, f"The word was {word}!")
        print(colorama.Fore.RED, "Game Over!")
