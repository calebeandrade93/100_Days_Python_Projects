from art import *  # My local file art.py
from data import *  # My local file data.py
import time

machine_on = True

while machine_on:
    user_input = main_menu()
    if user_input == 1:
        espresso_maker()
        clear_screen()
    elif user_input == 2:
        latte_maker()
        clear_screen()
    elif user_input == 3:
        cappuccino_maker()
        clear_screen()
    elif user_input == 4:
        machine_report()
        clear_screen()
    else:
        machine_on = False

