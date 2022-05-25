import random

class Display: 
    #Please create a variable that is public called "tries" and set it equal to 4

    def __init__(self):
        """control the word and letter the user is guessing  
    
    The responsibility of Guess is to compare the user's input with the right letter of the random word. 
    
    Attributes:
        _stages = Save the board for display

        
        """
        self._word_list = ["apple", "dream", "drama", "enemy", "blind"]
        self._select_word = random.choice(self._word_list)
        self._display_word = '_' * len(self._select_word)
        
       

    def set_word(self):
        """get the a random word from the word_list"""
        index = random.randint(0,4)
        self._select_word = self._word_list[index]

    def get_secret_word(self):
        """Returns secret word to a reusable method.
        """
        return self._select_word


    def get_displayWord(self):
        return self._display_word

    def update_word(self, index, letter):
        for number in index:
            self._display_word[number] = letter

    def display_para(tries): 
        stages = [
            """
             ___
            /___\
            \   /
             \ /
              O
             /|\
             / \   

            """,
            """
             
            /___\
            \   /
             \ /
              O
             /|\
             / \   

            """,
            """
             
            
            \   /
             \ /
              O
             /|\
             / \   

            """,
            """
             
        
            
             \ /
              O
             /|\
             / \   

            """,
            """
             
              x
             /|\
             / \   

            """,
        ]
        return stages[tries]

