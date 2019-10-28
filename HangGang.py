#  This program has been written by Oliver Sprange on Oct. 13th 2019.

#  This program is based on the code found on https://www.geeksforgeeks.org/python-program-for-word-guessing-game/

#  The code has been modified by Oliver Sprange to suit the needs for our group project.

#  Modifications include a hint system, and minor changes to turns etc.


import random  # The random function will allow us to choose a random word from a list

#  Making multiple tuples, containing the words and hints
def HangManGame():
    words_hints = (('monty', 'Whose surname is Python?'),

                   ('subnet', 'A logical subdivision of an IP network'),

                   ('developer', 'What may you call the one who wrote this program?'),

                   ('debugging', 'Nasty bugs.'),

                   ('pseudocode',
                    'An informal high-level description of the operating principle for a computer program.'),

                   ('dictionary', 'A resource that lists the words of a language.'),

                   ('argument', 'A value we pass to a function or method when calling it.'),

                   ('generator', 'A function that "yields" values one by one.'),

                   ('function', 'A series of statements which returns some value to a caller.'),

                   ('immutable', 'An object with a fixed value.'),

                   ('metaclass', 'The class of a class.'),

                   ('namespace', 'The place where a variable is stored.'),

                   ('slice', 'An object usually containing a portion of a sequence.'),

                   ('computer', 'Is made up of two components: Hardware, and software.'),

                   ('binary', 'A language made up of ones and zeroes.'),

                   ('boolean', 'A value that is either true or false.'),

                   ('constructor', 'A method or function for creating an instance of the class to which it belongs.'),

                   ('github', 'A web-based hosting service where anyone can share programming code with anyone else.'),

                   ('increment', 'The process of increasing or decreasing a numeric value by another value.'),

                   ('inheritance',
                    'The ability of an object to take on one or more characteristics from other classes.'))

    word_tuple = random.choice(words_hints)  # Choosing a random tuple from the words_lists

    word = word_tuple[0]  # Var that picks the words from the beforementioned tuple

    hint = word_tuple[1]  # Var that picks the according hint to the word

    print('Guess the characters: ')

    guesses = ''  # Variable that contains the users guesses

    turns = 6  # Counter that counts down the users turns

    while turns > 0:

        failed = 0  # Amount of times the user has input a wrong character

        for char in word:

            if char in guesses:

                print(char)

            else:

                print('_')

                failed += 1  # For every failure, failed will increment by 1

        if failed == 0:
            print('You win!')

            print('This word is: ', word)

            break

        while True:
            try:
                guess = input('Guess a character: ').lower()  # Prompting user for input, and converting to lowercase
            except:
                continue

            if len(guess) > 1:  # Making sure, the user doesn't input multiple letters, thus being able to win in one move
                print("One character please.")
                continue
            else:
                break

        guesses += guess  # Assign guess to guesses var


        if guess.isalpha():  # Making sure the users input is a alphabetical character

            if guess not in word:

                turns -= 1

                print('Wrong')

                print('You have', + turns, 'more guesses')

                if turns <= 2 and turns != 0:  # Conditional statement, that prints [1] from the tuple, which is the hint var
                    print("Here is a hint: ", hint)

        else:  # Punishing the user for trying to input anything else that alphabetical characters

            if guess not in word:

                turns -= 1

                print('Invalid character - you lose a life, because you know which characters are used in a word.')

                print('You have', + turns, 'more guesses')

                if turns <= 2 and turns != 0:
                    print("Here is a hint: ", hint)

            if turns == 0:  # Prompting user that they have lost, once the turns var == 0
                print('You lost.')
