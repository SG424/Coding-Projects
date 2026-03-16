import random

x = input("Welcome to Mascarpone, your name? ")

tables = ("Table 1", "Table 2", "Table 3", "Table 4", "Table 5")
y = random.choice(list(tables))


menu = {
    "Smoked beef Carbonara": 785,
    "Pasta di Gaber": 950,
    "Lasagna": 850,
    "Untitled": 400,
    "Caprese Salad": 500,
}

Beverages = {
    "Water": 100,
    "Juice": 100,
    "Four loko": 350,
    "Presidente": 400,
    "Chivas 18": 800,
}

Deserts = {
    "untitled1": 400,
    "untitled2": 400,
    "untitled3": 400,
    "Tiramisu": 400,
    "untitled4": 400,
}



total = 0


if y==tables[1] or y == tables[4] or y == tables[3]:
    print("Your table is", y)
    print("Our Menu:")
    for item, price in menu.items():
            print(f"{item}: ${price:.2f}")
 

    while True:
        try:
            order = int(input("Enter the number of your order (0 to finish): "))
            match order:
                case 1: total = total + 785
                case 2:total = total + 950
                case 3:total = total + 850
                case 4:total = total + 400
                case 5:total = total + 500
                case 0:break
                case _:
                    print("We dont have that")
                    continue 
        except ValueError:
            print("Please enter a number.") 
    
    for item,price in Beverages.items():
        print(f"{item}: ${price:.2f}")
    while True:
        order = int(input("Enter the number of your Beverage (0 to finish): "))
        try:
            match order: 
                    case 1: total = total + 100
                    case 2:total = total + 100
                    case 3:total = total + 350
                    case 4:total = total + 400
                    case 5:total = total + 800
                    case 0:break
                    case _:
                        print("We dont have that")
                        continue  
        except ValueError:
            print("Please enter a number.") 
    for item,price in Deserts.items():
        print(f"{item}: ${price:.2f}")
    while True:
        order = int(input("Enter the number of your desert (0 to finish): "))
        try:
            match order: 
                    case 1: total = total + 400
                    case 2:total = total + 400
                    case 3:total = total + 400
                    case 4:total = total + 400
                    case 5:total = total + 400
                    case 0:break
                    case _:
                        print("We dont have that")
                        continue  

        except ValueError:
            print("Please enter a number.")
    itbis=(total*0.18)
    itbis_total= itbis+total
    print("Total:", total)

    print(f"Thank you,, {x}")
    print(f"Total:{total}")
    print(f"ITBIS:{itbis}")
    print(f"Final Total:{itbis_total}")
    
    bill=int(input("Card(1) or Cash(2)?:  "))
   
    money=[2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
    balance=random.randint(1, 100000)


    if bill==2:
        given=float(input("How much cash?: ")) 
        if given<itbis_total:
            print("Not enough money")
        else:
         change=given-itbis_total
         print(change)
         for billete in money:
             if change//billete:
                print(f"{change//billete}*{billete}")
                change=change%billete
             



    elif bill==1:
        if balance<itbis_total:
            print("Sorry not enough money", x)
        else:
            result=balance-itbis_total
            print("Thanks for coming", result)#Revisar
    
    asktip=input("Want to add a tip?:  ")

    if asktip== "yes":
        tip=input("How much?: ") 
        print("Thanks,", x)
    else:
         print("Thanks,", x)



       
        


         

else:
    print("There are no tables,", x)


