class Coffee:
    old_water = 400
    old_milk = 540
    old_bean = 120
    old_cup = 9
    old_money = 550
    
    
    
    
    def __init__ (self, water, milk, bean, cup, cost):
      self.water = water
      self.milk = milk
      self.bean = bean
      self.cup = cup
      self.cost = cost
    def all(self):
        Coffee.old_water -= self.water
        
    

        Coffee.old_milk -= self.milk
    
        Coffee.old_bean -= self.bean
    
        Coffee.old_cup -= self.cup

    
        Coffee.old_money += self.cost
      
  

espresso = Coffee(250, 0, 16, 1, 4)
latte = Coffee(350, 75, 20, 1, 7)
cappuccino = Coffee(200, 100, 12, 1, 6)






def next(water, milk, bean, cups, cost):
    water = Coffee.old_water 
    milk = Coffee.old_milk 
    bean = Coffee.old_bean 
    cups = Coffee.old_cup 
    cost = Coffee.old_money
    while True:
        print("Write action (buy, fill, take, remaining, exit):")
        answer = input()
        if answer == "remaining":
            print(f"""The coffee machine has:
{Coffee.old_water} ml of water
{Coffee.old_milk} ml of milk
{Coffee.old_bean} g of coffee beans
{Coffee.old_cup} disposable cups
${Coffee.old_money} of money""")
      
        elif answer == "buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
            answer = input()
            if answer == "1" and Coffee.old_water > 250:
                espresso.all()
                print("I have enough resources, making you a coffee!")
            elif answer == "2" and Coffee.old_water > 350:
                latte.all()
                print("I have enough resources, making you a coffee!")
            elif answer == "3" and Coffee.old_water > 200:
                cappuccino.all()
                print("I have enough resources, making you a coffee!")
            elif answer == "back":
                return next(water, milk, bean, cups, cost) 
            else:
              print("Sorry, not enough water!")
        elif answer == "fill":
            print("Write how many ml of water you want to add:") 
            water_add = int(input())
            Coffee.old_water += water_add
            print("Write how many ml of milk you want to add:")
            milk_add = int(input())
            Coffee.old_milk += milk_add
            print("Write how many grams of coffee beans you want to add:") 
            beans_add = int(input())
            Coffee.old_bean += beans_add
            print("Write how many disposable cups you want to add:")
            cups_add = int(input())
            Coffee.old_cup += cups_add

        elif answer == "take":
            print(f"I give you ${Coffee.old_money}")
            Coffee.old_money -= Coffee.old_money
        elif answer == "exit":
            break;
next(Coffee.old_water, Coffee.old_milk, Coffee.old_bean, Coffee.old_cup, Coffee.old_money)
