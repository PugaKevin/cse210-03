from operator import index
from random import random
from typing import Counter


class Guess:
    """control the word and letter the user is guessing  
    
    The responsibility of Guess is to compare the user's input with the right letter of the random word. 
    
    Attributes:
        _word_list (List[string]): The list of words the game has (option of words).
        
        _letter_user (string): The user's input.
        _is_guessed(int): Whether or not the user has guessed.

    """

    def __init__(self):
        self._letter_user = ""
        self._tries = 0
        self._is_guessed = False


    def get_tries(self):
        return self._tries


    def set_userGuess(self, guess):
        self._letter_user = guess


    def get_userGuess(self):
        return self._letter_user


    def check_guess(self, secretWord):
        """Checks to make sure user's guess matches letter.
        """
        if self._letter_user in secretWord:
            self._indx = secretWord.index(self._letter_user)
            return True
        else:
            self._tries += 1
            return False  


    def check_for_win(self):
        """Check to see if you guessed all the letters correctly.
        """
        if self.get_tries() > 5:
            return True
        else:
            return False

