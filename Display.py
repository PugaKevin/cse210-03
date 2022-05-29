import random

class Display: 
    #Please create a variable that is public called "tries" and set it equal to 4

    def __init__(self):
        """control the word and letter the user is guessing  
    
    The responsibility of Guess is to compare the user's input with the right letter of the random word. 
    
    Attributes:
        _stages = Save the board for display
        _select_word (string): The word in the current game.
        """
        self._word_list = ["apple", "dream", "drama", "enemy", "blind"]
        self._select_word = random.choice(self._word_list)
        self._display_word = ['_' for i in range(len(self._select_word))]
        self._mns = ""
        self.stage = 0

    
    def get_displayWord(self):
        return ' '.join(self._display_word)


    def get_message(self, tries, is_guessed):
        mns = ""
        if is_guessed == False and (tries >= 1 and tries < 4):
            mns = "Keep trying you have " + str(4 - tries) + " tries left!"

        elif is_guessed:
            mns = "You guessed right!"
        elif tries == 4:
            mns = "Sorry, you lost all your tries"

        elif tries == 0:
            mns = "Welcome to Jumper! \n You have 4 tries, Good luck!"

        else:
            mns = "Sorry, please enter a letter."

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

        for index in indexes:
            self._display_word[index] = user_guess

        


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

