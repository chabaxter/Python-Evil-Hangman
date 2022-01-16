import random

def main():
    print("Welcome to (Evil) Hangman!\n")
    play_again = True
    while play_again:
        length = int(input("How long would you like the word to be?: "))
        num_guesses = int(input("How many guesses would you like to use?: "))
        Evil_hangman(num_guesses, length)
        while True:
            try:
                usr_input = str(input("Do you wish to play again? (yes or no): "))
            except ValueError:
                print("You must enter a string!")
                continue
            else:
                if usr_input.lower() == "yes":
                    break
                elif usr_input.lower() == "no":
                    play_again = False
                    break
                else:
                    print("You must either enter (yes) or (no)!")
        print()

    print("Goodbye!")


def Evil_hangman(guesses_remaining, word_length):
    print("\n\n~~~Evil Hangman~~~")
    print(f"Word Length: {word_length}\nNumber of Guesses {guesses_remaining}")

    permutations_dict = dict()
    words_dict = dict()
    guessed_letters = list()
    key = progress = word_length*'-'

    dictionary = open('dictionary.txt', 'r')
    for word in dictionary:
        word = word.strip()
        if len(word) in words_dict.keys():
            words_dict[len(word)].append(word)
        else:
            words_dict[len(word)] = [word]
    dictionary.close()

    words = words_dict[word_length]

    win = False
    while not win and guesses_remaining:
        permutations_dict = dict()
        print(f"Guesses Remaining: {guesses_remaining}")
        print(f"Your progress is: {key}")
        print(f"Previous guesses: {guessed_letters}")
        while True:
            try:
                guess = str(input("Make your guess: "))
            except ValueError:
                print("You must enter a character!")
                continue
            else:
                guess = guess.lower()
                if len(guess) == 1 and guess[0].isalpha() and guess[0] not in guessed_letters:
                    guessed_letters.append(guess)
                    break
                else:
                    print("You must enter a single letter which has not already been guessed!")

        for i in range(len(words)):
            key_str = ''
            for j in range(word_length):
                if key[j] != '-':
                    key_str += key[j]
                elif words[i][j] == guess:
                    key_str += guess
                else:
                    key_str += '-'

            if key_str not in permutations_dict.keys():
                permutations_dict[key_str] = [i]
            else:
                permutations_dict[key_str].append(i)

        previous = key
        key = max(permutations_dict, key=lambda x: len(permutations_dict[x]))
        words = [ words[k] for k in permutations_dict[key] ]

        if previous != key:
            print(f"\n{guess} was correct!")
        else:
            print(f"\n{guess} was incorrect")

        win = '-' not in key

        guesses_remaining -= 1

    if win:
        print(f"You win! The word was {key}")
    else:
        print(f"You lose! The word was {random.choice(words)}")


if __name__ == '__main__':
    main()
