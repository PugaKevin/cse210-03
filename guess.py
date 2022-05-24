from random import random

class Guess:
    """control the word and letter the user is guessing  
    
    The responsibility of Guess is to compare the user's input with the right letter of the random word. 
    
    Attributes:
        _word_list (List[string]): The list of words the game has (option of words).
        _select_word (string): The word in the current game.
        _letter_user (string): The user's input.
        _letters_guessed(int): A counter to know what index of the word we'll compare
        _letter_game(string): The letter the user has to guess
    """

    def __init__(self):

        self._word_list = ["apple", "dream", "drama", "enemy", "blind"]
        self._select_word = ""
        self._letter_user = ""
        self._letters_gessed = 0
        self._letter_game = ""


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

        return self._select_word

    def get_word(self):
        """method returns the value when someclass needs it"""
        return self._select_word

    def get_letterToGuess(self):
        #A helper array to save the letters of the word guessing. 
        letter_game = []
        #The word we are guessing
        word = self.get_word()

        #Add the letters into the Array
        for letter in word:
            letter_game.append(letter)
        
        index = self._letters_gessed

        self._letter_game = letter_game[index]
         
        #clear all elements in the Array
        letter_game.clear()

        return self._letter_game

    def comparation(self):
        is_correct = False
        self._letter_game = self.get_letterToGuess()
        user_input = self.get_letter()



        """ comparate the user's input with
         the letters in the game"""

        return is_correct
    pass
