class Guess:
    """control the word and letter the user is guessing  
    
    The responsibility of Guess is to compare the user's input with the right letter of the random word. 
    
    Attributes:
        _word_list (List[string]): The list of words the game has (option of words).
        _select_word (string): The word in the current game.
        _letter (string): The user's input.
    """

    def __init__(self):

        self._word_list = []
        self._select_word = ""
        self._letter = ""

    def set_letter(self, letter):
        """ method sets the user's input value into self._letter attribute"""
    pass

    def set_word(self):
        """get the word from the word_list"""
    pass 

    def get_word(self):
        """method returns the value when someclass needs it"""
        #return word
    pass



    def comparation(self):
        """ comparate the user's input with
         the random letter"""
    pass
