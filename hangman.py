import random

print("H A N G M A N")
action = "play"
while not(action == "exit"):
    action = input('Type "play" to play the game, "exit" to quit: ')
    if action == "exit":
        break
    elif action == "play":
        pass
    else:
        continue

    word = random.choice(['python', 'java', 'kotlin', 'javascript'])
    guess = len(word) * "-"
    guess_cnt = 0
    word_index = 0
    letter = ""
    input_items = []

    while guess_cnt < 8 and guess != word:
        match = False
        already_matched = False
        print()
        print(guess)

        try:
            letter = input('Input a letter: ')
        except:
            print("EOFError: EOF when reading a line")
            break

        if not len(letter) == 1:
            print("You should print a single letter")
            continue
        elif letter in input_items:
            print("You already typed this letter")
            continue
        else:
            input_items.append(letter)

        if not letter.islower():
            print("It is not an ASCII lowercase letter")
        else:
            word_index = 0
            while word_index < len(word):
                if word[word_index] == letter:
                    guess = "{0}{1}{2}".format(guess[:word_index], letter, guess[word_index + 1:])
                    match = True

                word_index += 1

            if not match:
                guess_cnt += 1
                print("No such letter in the word")

    # print()

    if guess == word:
        print(guess)
        print("You guessed the word!" + guess + "\nYou survived!")
    else:
        print("You are hanged!")

