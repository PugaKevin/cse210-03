from terminal_service import TerminalService
from guess import Guess
from Display import Display


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        
        is_playing (boolean): Whether or not to keep playing.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
      
        self._guess = Guess()
        self._is_playing = True
        self._display = Display()
        self._terminal_service = TerminalService()
        

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()


    def _get_inputs(self):
        """Takes user letter guesses.

        Args:
            self (Director): An instance of Director.
        """
        guess = self._terminal_service.read_text('\nEnter in a letter: ')
        self._guess.check_guess(guess)
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """

        #win
        display = self._terminal_service.write_text(self._display.get_displayWord())
        
        
        
        
        
    def _do_outputs(self):      
        """Updates display of jumper and word.

        Args:
            self (Director): An instance of Director.
        """
        display = self._guess.show_word()
        self._terminal_service.write_text(display)
        if self._guess.check_for_win():
            self._is_playing = False
