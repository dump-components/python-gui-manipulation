import pyautogui

class GraphicUserInterface:
    
    def __init__(self) -> None:
        self._screen= pyautogui
    
    @property
    def screen(self):
        return self._screen
    
