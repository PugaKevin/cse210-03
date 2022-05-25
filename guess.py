from random import random
from typing import Counter
from Display import Display


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

        self._display = Display()

        self._letter_user = ""

        self._letters_guessed = 0
        self._tries = 0


    def set_tries(self, tries):

        self._tries = tries

    def get_tries(self):

        return self._tries
   

    def get_word_index(self, guess):
        """Creates indexes for letter in the secretword.
        """
        letter_indexes = []

        word = self._display.get_secret_word()

        for index, char in enumerate(list(word)):
            if char == guess:
                letter_indexes.append(index)

        return letter_indexes



    def check_guess(self, guess):
        """Checks to makes sure user guess matches letter.
        """
        secretWord = self._display.get_secret_word()
        
        if guess in secretWord:
            index = self.get_word_index(guess)
            self._display.update_word(index, guess)
            
        else:
            counter += 1
            self.set_tries(counter)
        

        


    def check_for_win(self):
        """Check to see if you guessed all the letters correctly.
        """
        display = ' '.join(self._display.get_displayWord())
        word = self._display.get_secret_word()
        if display == word:
            print('You Win!')
            return True
