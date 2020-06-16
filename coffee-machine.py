import sys

ITEMS = ["water", "milk", "coffee beans", "disposable cups", "money"]  # Used for output and looping logic (length)
STATE = [400, 540, 120, 9, 550]  # Stores the amount for each item

# List of ingredients needed for each coffee type.
INGREDIENTS = [
    [250, 0, 16, 1, -4],  # espresso
    [350, 75, 20, 1, -7],  # latte
    [200, 100, 12, 1, -6],  # cappuccino
]
MONEY = 4
flavor = 0


class ResourceError(Exception):
    pass


def menu():
    print()
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()

    if action == "buy":
        buy()
    elif action == "fill":
        execute_fill_action()
    elif action == "take":
        execute_take_action()
    elif action == "remaining":
        status()
    elif action == "exit":
        sys.exit()
    else:
        menu()
    print()


def status():
    print("The coffee machine has:")
    counter = 0
    while counter < len(ITEMS):
        print(str(STATE[counter]), "of", ITEMS[counter])
        counter += 1
    menu()


def select_flavor() -> int:
    print()
    response = input('What do you want to buy?'
                     ' 1 - espresso,'
                     ' 2 - latte,'
                     ' 3 - cappuccino,'
                     ' back - to main menu: ')
    if response == 'back':
        return 0
    return int(response)


def is_enough(need_water=0, need_milk=0, need_beans=0):
    if STATE[0] < need_water:
        print("Sorry, not enough water!\n")
        raise ResourceError
    if STATE[1] < need_milk:
        print("Sorry, not enough milk!\n")
        raise ResourceError
    if STATE[2] < need_beans:
        print("Sorry, not enough beans!\n")
        raise ResourceError
    if STATE[3] < 1:
        print("Sorry, not enough cups\n")
        raise ResourceError
    print("I have enough resources, making you a coffee!\n")


def buy():
    global flavor
    flavor = select_flavor()
    try:
        if flavor == 0:
            pass
        elif flavor == 1:  # espresso
            is_enough(need_water=250, need_beans=16)
            execute_buy_action()
        elif flavor == 2:  # latte
            is_enough(need_water=350, need_milk=75, need_beans=20)
            execute_buy_action()
        elif flavor == 3:  # cappuccino
            is_enough(need_water=200, need_milk=100, need_beans=12)
            execute_buy_action()
        else:
            raise ValueError(f'Unknown flavor {flavor}')
    except ResourceError:
        pass
    menu()


def execute_buy_action():
    counter = 0
    while counter < len(ITEMS):
        STATE[counter] -= INGREDIENTS[flavor - 1][counter]
        counter += 1


def execute_fill_action():
    message = [
        "Write how many ml of water do you want to add:",
        "Write how many ml of milk do you want to add:",
        "Write how many grams of coffee beans do you want to add:",
        "Write how many disposable cups of coffee do you want to add:"
    ]
    counter = 0
    while counter < len(message):
        print(message[counter])
        STATE[counter] += int(input())
        counter += 1
    menu()


def execute_take_action():
    money = STATE[MONEY]
    STATE[MONEY] = 0
    print("I give you $" + str(money))
    menu()


menu()
