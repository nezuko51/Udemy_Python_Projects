# TODO Setup: import packages and starting global variables. Continuously add along the way.
# TODO 1: Prompt user for coffee choice ✅
# TODO 2: Turn off coffee machine by entering "off" prompt ✅
# TODO 3: Print report to display current resources ✅
# TODO 3.1: Create function that prints report ✅
# TODO 4: Check if resources are sufficient ✅
# TODO 5: Process coins; only takes US coins such as penny, nickel, dime, and quarter ✅
# TODO 6: Check if transaction is successful. Insufficient funds prompt message & refund ✅
# TODO 7: Make coffee chosen by user IF there are enough resources & IF sufficient funds are processed ✅
# TODO 8: Improve interface and functionality of code. e.g: create a menu to choose from including an "off" to turn off coffee machine


# Coffee machine starting resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Constant variables for calculating transactions
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

QUARTER = 0.25
DIME = 0.10
NICKLE = 0.05
PENNY = 0.01


def print_report(resources_dict, money):
    """Prints report of current resources available"""
    total_money = money
    print("\n-----------------\nCurrent resources\n-----------------")
    return f"Water: {resources['water']}mL\nMilk: {resources['milk']}mL\nCoffee: {resources['coffee']}g\nMoney: ${total_money}"


def print_menu():
    """Prints the menu items of the coffee machine"""
    print("\nHello! Below is a selection of coffee we have to offer you. ☕\nTo check current resources available (waster, milk, coffee, current money in the machine), type 'report'.\nTo turn off the machine, type 'off'.")
    print("Please note that this machine ONLY takes coins as currency.\nFeel free to insert as many coins as you'd like if you're unsure.")
    print("\n--------------------\nCoffee Machine Menu\n--------------------")
    for item in MENU:
        print(f"{item}: ${MENU[item]['cost']}")
    print("--------------------")


def check_resources(curr_resources, menu_item):
    """ This function checks the current resources against the necessary resources from the list MENU to see if the
     coffee item chosen by the user can be processed.  "menu_item" variable contains the specific dictionary key from MENU which is based on
     user_choice in the running program"""
    is_available = False
    no_resource = None
    menu_item_resources = menu_item["ingredients"]
    # print(resources)
    # print(MENU[item]['ingredients'])

    for item, resource_value in curr_resources.items():
        # print(item)
        for i, menu_val in menu_item_resources.items():
            if item == i:
                if menu_val <= resource_value:
                    # print(f"{item}: {resource_value} == {i}: {menu_val}") # check if resources are matched
                    is_available = True
                else:
                    is_available = False
                    no_resource = item
                    return is_available, no_resource
            else:
                continue

    return is_available, no_resource


def transaction(menu_item_price):
    """ This function processes the transactions based on the availability of resources.
    If there are enough resources, then coffee machine proceeds with the transaction.
    However, if the user does not insert enough money, the money is 'refunded'. """

    print("\nPlease insert coins.")
    num_quarters = int(input("How many quarters?: "))
    num_dimes = int(input("How many dimes?: "))
    num_nickles = int(input("How many nickles?: "))
    num_pennies = int(input("How many pennies?: "))

    total = (num_quarters * QUARTER) + (num_dimes * DIME) + (num_nickles * NICKLE) + (num_pennies * PENNY)
    if total > menu_item_price:
        final_change = total - menu_item_price
        f"\nHere is ${round(final_change, 2)} in change."
    else:
        final_change = menu_item_price - total
        f"\nHere is ${round(final_change, 2)} in change."

    return total


def check_funds(total_transaction, menu_cost):
    """ This function checks the total transaction given by user against the
    actual cost of the coffee item. If the total amount given is less than
    the actual cost of the item, the function returns False to let user know
    it was not enough money."""

    if total_transaction < menu_cost:
        return False
    else:
        return True


def update_resources(curr_resources, menu_resources):
    """ Updates current resources based on incoming requests from the user.
    Each request should reduce the available resources as any normal coffee
    machine would."""

    menu_item_resources = menu_resources["ingredients"]
    for item in curr_resources:
        for i in menu_item_resources:
            if item == i:
                curr_resources[item] -= menu_item_resources[i]
            else:
                curr_resources[item] -= 0

    return


def get_coffee(choice, coffee_resources, coffee_money):
    """ This is the main function that processes the user's choice of coffee,
    calls other functions to check if there are enough resources, enough money
    inserted, and updates resources accordingly. If resources are low, function
    immediately returns the user's money (aka no money was processed so machine
    transaction balance remains the same)."""
    available, low_resource = check_resources(coffee_resources, MENU[choice])

    if available is False:
        print(f"Sorry, there is not enough {low_resource}")
        return coffee_money

    else:
        process_money = (transaction(MENU[choice]["cost"]))
        funds = check_funds(process_money, MENU[choice]["cost"])
        if funds is False:
            coffee_money += 0
            print("Sorry, that's not enough money. Money refunded.")
            return coffee_money

        else:
            coffee_money += MENU[choice]["cost"]
            update_resources(coffee_resources, MENU[choice])
            print(f"Here is your {choice} ☕ Enjoy!")
            return coffee_money


run_machine = True
machine_money = 0  # counter to keep track of all the money in the coffee machine when a request is processed
print(""" 
    ╔═╗┌─┐┌─┐┌─┐┌─┐┌─┐  ╔╦╗┌─┐┌─┐┬ ┬┬┌┐┌┌─┐
    ║  │ │├┤ ├┤ ├┤ ├┤   ║║║├─┤│  ├─┤││││├┤ 
    ╚═╝└─┘└  └  └─┘└─┘  ╩ ╩┴ ┴└─┘┴ ┴┴┘└┘└─┘""")

print_menu()
while run_machine:

    user_choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        print("\nThank you for your support! We hope you come back soon!")
        run_machine = False
    elif user_choice == "report":
        print(print_report(resources, machine_money))
    elif user_choice == "espresso" or "latte" or "cappuccino":
        machine_money = get_coffee(user_choice, resources, machine_money)

    else:
        run_machine = False
