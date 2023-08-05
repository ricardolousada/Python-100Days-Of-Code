# create by Ricardo Lousada
# Coffee machine project

from data import MENU, resources

# make the current resources the same that the machine starts with
current_resources = resources
# add money key to the current resources
current_resources["money"] = 0

# variable to keep track of the machine status (on/off)
machine_off = False

# make a list of command accepted by the user
commands = ["espresso", "latte", "cappuccino", "off", "report"]


def machine_report(status: dict):
    """ takes a dictionary with the resources and print then to the console
    :type status: dictionary
    """
    water = status["water"]
    milk = status["milk"]
    coffee = status["coffee"]
    money = status["money"]
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: {money}€")


def make_drink(drink: str):
    """Tests if there are enough resources to make the cappuccino, if yes calls the payment function-pay()"""
    for key, value in MENU[drink]["ingredients"].items():
        if current_resources[key] < value:
            print(f"Sorry there is not enough {key}.")
            return
    pay(drink)


def pay(drink):
    """Handles the payment for the drink. If successful deduct ingredients and increase money"""
    drink_prince = MENU[drink]["cost"]
    print(f"Please insert coins. ({drink_prince}€)")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total_payed = round((quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01), 2)
    if total_payed < drink_prince:
        print(f"Sorry that's not enough money. Money refunded")
    else:
        change = round((total_payed - drink_prince), 2)
        if change != 0:
            print(f"Here is €{change} in change.")
        print(f"Here is your {drink} ☕. Enjoy!")
        # add money to the machine
        current_resources["money"] = current_resources["money"] + drink_prince
        update_machine_resources(drink)


def update_machine_resources(drink: str):
    """Takes a string that uis the drink and updates the machine resources"""
    for key, value in MENU[drink]["ingredients"].items():
        current_resources[key] = current_resources[key] - value


while not machine_off:
    user_input = input("What you like? (espresso/latte/cappuccino): ").lower()
    if user_input not in commands:
        print("I'm sorry, i don't recognize that command.")
        machine_off = True
    elif user_input == "off":
        print("Turning off for maintenance.")
        machine_off = True
    elif user_input == "report":
        machine_report(current_resources)
    else:
        make_drink(user_input)

# Change the call to make drinks only to one function
