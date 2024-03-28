water = 400
milk = 540
coffee_bean = 120
cups = 9
money = 550


def display_material():
    print("The coffee machine has:")
    print("{water} ml of water".format(water=water))
    print("{milk} ml of milk".format(milk=milk))
    print("{coffee_bean} g of coffee beans".format(coffee_bean=coffee_bean))
    print("{count} disposable cups".format(count=cups))
    print("${amount} of money".format(amount=money))


def is_has_enough_material(waters, milks, coffee_beans, cups):
    if water * cups < waters:
        return False

    if milk * cups < milks:
        return False

    if coffee_bean * cups < coffee_beans:
        return False

    return True


products = {
    "1": {
        "name": "espresso",
        "water": 250,
        "coffee_bean": 16,
        "milk": 0,
        "price_dollar": 4
    },
    "2": {
        "name": "latte",
        "water": 350,
        "coffee_bean": 20,
        "milk": 75,
        "price_dollar": 7
    },
    "3": {
        "name": "cappuccino",
        "water": 200,
        "coffee_bean": 12,
        "milk": 100,
        "price_dollar": 6
    }
}


def check_material(coffee):
    require_material = []

    if water < coffee['water']:
        require_material.append("water")

    if milk < coffee['milk']:
        require_material.append("milk")

    if coffee_bean < coffee['coffee_bean']:
        require_material.append("coffee bean")

    if cups < 1:
        require_material.append("cups")

    return require_material


while True:

    action = input("Write action (buy, fill, take, remaining, exit): ")

    if action == 'exit':
        break

    if action == 'remaining':
        display_material()

    if action == 'buy':
        coffee_id = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")

        if coffee_id == 'back':
            continue

        coffee = products[coffee_id]

        missing_material = check_material(coffee)

        if len(missing_material) > 0:
            items = ", ".join(missing_material)
            print("Sorry, not enough {items}!".format(items=items))
            continue
        else:
            print("I have enough resources, making you a coffee!")

        cups = cups - 1
        water = water - coffee['water']
        milk = milk - coffee['milk']
        coffee_bean = coffee_bean - coffee['coffee_bean']
        money = money + coffee['price_dollar']

    if action == 'fill':
        water = water + int(input("Write how many ml of water you want to add:"))
        milk = milk + int(input("Write how many ml of milk you want to add:"))
        coffee_bean = coffee_bean + int(input("Write how many grams of coffee beans you want to add:"))
        cups = cups + int(input("Write how many disposable cups you want to add:"))

    if action == 'take':
        print("I gave you ${amount}".format(amount=money))
        money = 0
