import pyautogui

class GraphicUserInterface:
    
    def __init__(self) -> None:
        self.__screen = pyautogui
    
    @property
    def screen(self):
        return self.__screen
    
