from random import random
import random

class Guess:
    """control the word and letter the user is guessing  
    
    The responsibility of Guess is to compare the user's input with the right letter of the random word. 
    
    Attributes:
        _word_list (List[string]): The list of words the game has (option of words).
        _select_word (string): The word in the current game.
        _letter_user (string): The user's input.
        _letters_guessed(int): A counter to know what index of the word we'll compare

    """

    def __init__(self):

        self._word_list = ["apple", "dream", "drama", "enemy", "blind"]
        self._select_word = random.choice(self._word_list)
        self._display = ' ' * len(self._select_word)

        self._letter_user = ""

        self._letters_guessed = 0
        self.tries = 4


    def set_letter(self, letter):
        """ method sets the user's input value into self._letter_user attribute"""
        letter = input("Guess a letter (a-z): ")
        self._letter_user = letter


    def get_letter(self):
        """method returns the value when someclass needs it"""
        
    pass

    def set_word(self):
        """get the a random word from the word_list"""
        index = random.randint(0,4)
        self._select_word = self._word_list[index]

    def secret_word(self):
        """Returns secret word to a reusable method.
        """
        return self._select_word
   

    def get_word_index(self, guess):
        """Creates indexes for letter in the secretword.
        """
        letter_indexes = []

        word = self.secret_word()

        for index, char in enumerate(list(word)):
            if char == guess:
                letter_indexes.append(index)

        return letter_indexes
                

    def comparison(self, index, letter):
        """Compares and updates the index to the letter.
        """
        for number in index:
            self._display[number] = letter


    def check_guess(self, guess):
        """Checks to makes sure user guess matches letter.
        """
        if guess in self.secret_word:
            index = self.get_word_index(guess)
            self.comparison(index, guess)



    def check_for_win(self):
        """Check to see if you guessed all the letters correctly.
        """
        display = ' '.join(self._display)
        word = self._select_word
        if display == word:
            print('You Win!')
            return True
