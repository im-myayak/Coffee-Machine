import myfunctions as f

info_list = f.collect_the_information('resources')
current_water = info_list[0]
current_milk = info_list[1]
current_coffee = info_list[2]
current_money = 0
game = True

while game:
    user_word = input("What would you like ?(espresso/latte/cappuccino/) ").lower()
    if user_word == 'off':
        game = False
    elif user_word == 'report':
        print(f"Water : {current_water}")
        print(f"Milk : {current_milk}")
        print(f"Coffee : {current_coffee}")
        print(f"Money : ${current_money}")
    else:
        info_list = f.collect_the_information(user_word)
        water_coffee_type = info_list[0]
        milk_coffee_type = info_list[1]
        coffee_coffee_type = info_list[2]
        cost_of_coffee_type = info_list[3]
        flag_of_sufficiency = f.check_coffee_sufficient(user_word, [current_water, current_milk, current_coffee])
        if flag_of_sufficiency:
            print("Insert the coins ")
            quarter = int(input("How many Quarter? "))
            dine = int(input("How many Dine? "))
            nickel = int(input("How many Nickel? "))
            penny = int(input("How many Penny? "))
            flag_of_money = f.check_money(penny, nickel, dine, quarter, cost_of_coffee_type)
            if flag_of_money:
                print(f"{flag_of_money}")
                current_money += cost_of_coffee_type
                current_milk -= milk_coffee_type
                current_water -= water_coffee_type
                current_coffee -= coffee_coffee_type
                print(f"Here is your {user_word} ☕, enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
