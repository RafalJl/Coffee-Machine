class CM:
    def __init__(self, water, milk, beans, cup, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cup = cup
        self.money = money

    def current_state(self):
        print('''The coffee machine has:
{} of water
{} of milk
{} of coffee beans
{} of disposable cups
{} of money'''.format(self.water, self.milk, self.beans, self.cup, self.money))

    def fill(self):
        print("Write how many ml of water do you want to add:")
        current.water += int(input())
        print("Write how many ml of milk do you want to add:")
        current.milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        current.beans += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        current.cup += int(input())
        print()

    def take(self):
        print("I gave you $" + str(current.money))
        current.money = 0
        print()

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu")
        user_selection = input()

        if user_selection == "back":
            pass
        else:
            if int(user_selection) == 1 and (current.water < espresso.water \
                                             or current.beans < espresso.beans or current.cup < 1):
                if current.water < espresso.water:
                    print("Sorry I don't have enough water")
                if current.beans < espresso.beans:
                    print("Sorry I don't have enough beans")
                if current.cup < 1:
                    print("Sorry I don't have enough cups")
            elif int(user_selection) == 1 and current.water >= espresso.water \
                    and current.beans >= espresso.beans and current.cup >= 1:
                current.water -= espresso.water
                current.beans -= espresso.beans
                current.cup -= 1
                current.money += espresso.money
                print("I have enough resources, making you a coffee!")
            elif int(user_selection) == 2 and (current.water < latte.water \
                                               or current.milk < latte.milk or current.beans < latte.beans \
                                               or current.cup < 1):
                if current.water < latte.water:
                    print("Sorry I don't have enough water")
                if current.milk < latte.milk:
                    print("sorry I don't have enough milk")
                if current.beans < latte.beans:
                    print("Sorry I don't have enough beans")
                if current.cup < 1:
                    print("Sorry I don't have enough cups")
            elif int(user_selection) == 2 and current.water >= latte.water \
                    and current.milk >= latte.milk and current.beans >= latte.beans \
                    and current.cup >= 1:
                current.water -= latte.water
                current.milk -= latte.milk
                current.beans -= latte.beans
                current.cup -= 1
                current.money += latte.money
                print("I have enough resources, making you a coffee!")
            elif int(user_selection) == 3 and (current.water < cappuccino.water \
                                               or current.milk < cappuccino.milk or current.beans < cappuccino.beans \
                                               or current.cup < 1):
                if current.water < cappuccino.water:
                    print("Sorry I don't have enough water")
                if current.milk < cappuccino.milk:
                    print("sorry I don't have enough milk")
                if current.beans < cappuccino.beans:
                    print("Sorry I don't have enough beans")
                if current.cup < 1:
                    print("Sorry I don't have enough cups")
            elif int(user_selection) == 3 and current.water >= cappuccino.water \
                    and current.milk >= cappuccino.milk and current.beans >= cappuccino.beans \
                    and current.cup >= 1:
                current.water -= cappuccino.water
                current.milk -= cappuccino.milk
                current.beans -= cappuccino.beans
                current.cup -= 1
                current.money += cappuccino.money
                print("I have enough resources, making you a coffee!")

        print()

current = CM(400, 540, 120, 9, 550)
espresso = CM(250, 0, 16, 1, 4)
latte = CM(350, 75, 20, 1, 7)
cappuccino = CM(200, 100, 12, 1, 6)

while True:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    print()

    if action == "buy":
        current.buy()
    elif action == "fill":
        current.fill()
    elif action == "take":
        current.take()
    elif action == "remaining":
        current.current_state()
    elif action == "exit":
        break