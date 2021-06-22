from art import *  # My local file art.py
import time

# Drinks Menu
MENU = [
    {
        'type': 'Espresso',
        'water': 50,
        'coffee_bean': 18,
        'milk': 0,
        'price': 1.50,
    },
    {
        'type': 'Latte',
        'water': 200,
        'coffee_bean': 24,
        'milk': 150,
        'price': 2.50,
    },
    {
        'type': 'Cappuccino',
        'water': 250,
        'coffee_bean': 24,
        'milk': 100,
        'price': 3.50,
    },
]

# Machine conditions
MACHINE_REPORT = {
    'water': 500,
    'coffee_bean': 150,
    'milk': 500,
}

"""All Functions for the main program"""


# Clear the screen
def clear_screen():
    return print('\n' * 30)


# Main menu
def main_menu():
    keep_looping = True

    while keep_looping:
        print(LOGO)
        print("\nWhat would you like to drink today ?")
        print("1 - Espresso")
        print("2 - Latte")
        print("3 - Cappuccino")
        print("4 - Machine Reports")
        print("5 - Turn off")
        user_input = int(input("Type a number above: "))

        if user_input < 1 or user_input > 5:
            print("\nSomething went wrong, please try again")
            time.sleep(2)
            clear_screen()
        else:
            return user_input


# Making Espresso
def espresso_maker():
    clear_screen()
    print(f"{MENU[0]['type']} is ${MENU[0]['price']}, please touch your card on the screen")
    print(CARD_PAYMENT)
    time.sleep(4)
    clear_screen()
    print(CUP_COFFEE)
    print("Making your Espresso")
    print("Please, don't forget to place your cup on the holder")

    if MACHINE_REPORT['water'] >= MENU[0]['water']:
        MACHINE_REPORT['water'] -= MENU[0]['water']
        if MACHINE_REPORT['coffee_bean'] >= MENU[0]['coffee_bean']:
            MACHINE_REPORT['coffee_bean'] -= MENU[0]['coffee_bean']
            for number in range(1, 16):
                if number == 15:
                    time.sleep(1)
                    print("#", sep=' ', end=' ]', flush=True)
                elif number == 1:
                    time.sleep(1)
                    print("[#", sep=' ', end=' ', flush=True)
                else:
                    time.sleep(1)
                    print("#", sep=' ', end=' ', flush=True)
        else:
            print('\nNot enough coffee beans. Please, turn off the machine, fill more coffee beans in the recipient '
                  'and try again.\n')
    else:
        print('\nNot enough water. Please, turn off the machine, fill more water in the recipient and try again.\n')

    print("\nYour coffee is ready ! Enjoy =) ")
    time.sleep(2)


# Making Latte
def latte_maker():
    clear_screen()
    print(f"{MENU[1]['type']} is ${MENU[1]['price']}, please touch your card on the screen")
    print(CARD_PAYMENT)
    time.sleep(4)
    clear_screen()
    print(CUP_COFFEE)
    print(f"Making your {MENU[1]['type']}")
    print("Please, don't forget to place your cup on the holder")

    if MACHINE_REPORT['water'] >= MENU[1]['water']:
        MACHINE_REPORT['water'] -= MENU[1]['water']
        if MACHINE_REPORT['coffee_bean'] >= MENU[1]['coffee_bean']:
            MACHINE_REPORT['coffee_bean'] -= MENU[1]['coffee_bean']
            if MACHINE_REPORT['milk'] >= MENU[1]['milk']:
                MACHINE_REPORT['milk'] -= MENU[1]['milk']
                for number in range(1, 16):
                    if number == 15:
                        time.sleep(1)
                        print("#", sep=' ', end=' ]', flush=True)
                    elif number == 1:
                        time.sleep(1)
                        print("[#", sep=' ', end=' ', flush=True)
                    else:
                        time.sleep(1)
                        print("#", sep=' ', end=' ', flush=True)
            else:
                print('\nNot enough milk. Please, turn off the machine, fill with more milk in the recipient '
                      'and try again.\n')
        else:
            print('\nNot enough coffee beans. Please, turn off the machine, fill more coffee beans in the recipient '
                  'and try again.\n')
    else:
        print('\nNot enough water. Please, turn off the machine, fill more water in the recipient and try again.\n')

    print("\nYour coffee is ready ! Enjoy =) ")
    time.sleep(2)


# Making Cappuccino
def cappuccino_maker():
    clear_screen()
    print(f"{MENU[2]['type']} is ${MENU[2]['price']}, please touch your card on the screen")
    print(CARD_PAYMENT)
    time.sleep(4)
    clear_screen()
    print(CUP_COFFEE)
    print(f"Making your {MENU[2]['type']}")
    print("Please, don't forget to place your cup on the holder")

    if MACHINE_REPORT['water'] >= MENU[2]['water']:
        MACHINE_REPORT['water'] -= MENU[2]['water']
        if MACHINE_REPORT['coffee_bean'] >= MENU[2]['coffee_bean']:
            MACHINE_REPORT['coffee_bean'] -= MENU[2]['coffee_bean']
            if MACHINE_REPORT['milk'] >= MENU[2]['milk']:
                MACHINE_REPORT['milk'] -= MENU[2]['milk']
                for number in range(1, 16):
                    if number == 15:
                        time.sleep(1)
                        print("#", sep=' ', end=' ]', flush=True)
                    elif number == 1:
                        time.sleep(1)
                        print("[#", sep=' ', end=' ', flush=True)
                    else:
                        time.sleep(1)
                        print("#", sep=' ', end=' ', flush=True)
            else:
                print('\nNot enough milk. Please, turn off the machine, fill with more milk in the recipient '
                      'and try again.\n')
        else:
            print('\nNot enough coffee beans. Please, turn off the machine, fill with more coffee beans in the '
                  'recipient and try again.\n')
    else:
        print('\nNot enough water. Please, turn off the machine, fill more water in the recipient and try again.\n')

    print("\nYour coffee is ready ! Enjoy =) ")
    time.sleep(2)


# Report
def machine_report():
    clear_screen()
    print(MACHINE_REPORT_ART + '\n')
    print(f"Water: {MACHINE_REPORT['water']}ml")
    print(f"Coffee Beans: {MACHINE_REPORT['coffee_bean']}g")
    print(f"Milk: {MACHINE_REPORT['milk']}ml")
    user_input = int(input("Press '1' to refill the ingredients or '0' to go to main menu: "))
    if user_input == 1:
        machine_refill()
        time.sleep(2)
        print(f"\nWater: {MACHINE_REPORT['water']}ml")
        print(f"Coffee Beans: {MACHINE_REPORT['coffee_bean']}g")
        print(f"Milk: {MACHINE_REPORT['milk']}ml")
        time.sleep(2)
    else:
        return


#refill machine
def machine_refill():
    MACHINE_REPORT['water'] = 500
    MACHINE_REPORT['coffee_bean'] = 150
    MACHINE_REPORT['milk'] = 500
