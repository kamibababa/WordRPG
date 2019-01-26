""" 'load_game' state """

from ..gui.screen import const, Screen
from .states import State



class Load_Game(State):
    def __init__(self):
        """ Initiailize class and super class """
        super(Load_Game, self).__init__()

        self.screen = self._init_screen()


    def _init_screen(self):
        screen = Screen()
        screen.load_screen('scroll', offset=('center',1), fgcolor='YELLOW')

        screen.add_string_to_screen('LOAD GAME', offset=('center', 2),
                    fgcolor='CYAN')

        return screen
        

    def update_screen(self):
        """ Draws the screen """
        self.screen.draw()


    def on_event(self, event, prev_state):
        """ Handles events that are delegated to this State. """
        self.update_screen()
        self.wait_for_keypress()     
        return 'game'   #prev_state
