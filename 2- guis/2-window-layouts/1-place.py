#gui.py 

from tkinter import *

class Gui(TK):

    def __init__(self):
        super().__init__()

    #set window properties 
    self.title("Newsletter")
    self.configuration(bg="#ccc", height=200, width=360)

    #add components
    self.__add_outer_frame()
    self.__add_heading_label()
    self.__add_instruction_label()
    self.__add_email_label()
    self.__add_email_entry()
    self.__add_subscribe_button()

