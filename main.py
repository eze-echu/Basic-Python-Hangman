import random
import colorama

words = ["platypus", "kangaroo", "master"]


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


if __name__ == "__main__":
    word = random.choice(words)
    print(f"The word has {len(word)} letters.")
    solved = False
    failed = False
    guessed_letters = []
    display_word = ""
    for character in word:
        if character in guessed_letters:
            display_word += f" {character} "
        else:
            display_word += " _ "
    while not solved and not failed:
        print(display_word)
        print(f"Guessed letters: {guessed_letters}")
        letter = input("Enter a letter: ")
        if letter not in guessed_letters or len(letter) != 1:
            guessed_letters.append(letter)
            result = check_for_letter(word, letter)
            if result:
                display_word = ""
                for character in word:
                    if character in guessed_letters:
                        display_word += f" {character} "
                    else:
                        display_word += " _ "
                if "_" not in display_word:
                    solved = True
            else:
                print(colorama.Fore.YELLOW, f"letter {letter} not found in word.")
        elif letter in guessed_letters:
            print(colorama.Fore.RED, f"You have already guessed {letter}")
            print(colorama.Style.RESET_ALL)
        elif len(letter) != 1:
            print(colorama.Fore.RED, f"You must guess a single letter", colorama.Style.RESET_ALL)
            print(colorama.Style.RESET_ALL)

