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
        self._display_word = ['_' for i in range(len(self._select_word))]
        self._mns = "(-.-) Nap time."
        self.stage = 0
    
    def get_displayWord(self):
        return self._display_word

    def get_message(self, tries, is_guessed):


        if tries == 0:
            mns = "Welcome to Jumper Game you have " + str(tries + 4) + " tries"
        elif is_guessed == False and (tries >= 1 and tries <= 4):
            mns = "Keep trying you have " + str(4 - tries) + " tries"

        elif is_guessed:
            mns = "you guessed"

        else:
            mns = "Sorry , You missed tries"

        
        self._mns = mns

        return self._mns


    def get_secret_word(self):
        """Returns secret word to a reusable method.
        """
        return self._select_word
    
    def selector_board(self, is_guessed, user_guess):
        if is_guessed:
            self.update_boardDisplay(user_guess)
            
        else:
            self.stage += 1

        return self.stage



    def update_boardDisplay(self, user_guess):

        secretWord = self.get_secret_word()
        indexes = []
        counter = 0
        for letter in secretWord:
            if letter == user_guess.lower():
                indexes.append(counter)
            counter += 1

        for index in range(len(indexes)):
            self._display_word.insert(indexes[index], user_guess)

        
        #for number in index:
           # self._display_word[number] = letter

    def display_para(self, tracker): 
        stages = ["""
             ___
            /___\\
            \   /
             \ /
              O
             /|\\
             / \\
            """,
            """
             
            /___\\
            \   /
             \ /
              O
             /|\\
             / \   

            """,
            """
             
            
            \   /
             \ /
              O
             /|\\
             / \   

            """,
            """
             
        
            
             \ /
              O
             /|\\
             / \   

            """,
            """
             
              x
             /|\\
             / \   

            """,
        ]
        return stages[tracker]

