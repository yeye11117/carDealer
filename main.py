
car = ["Toyota", "Tesla", "BMW"]
price = ["1000", "2000", "3000"]

def menu():
    print("Hello, welcome to Yael's car dealer. \n 1) View Car List \n 2) View Car Prices \n 3) Add Car to Inventory \n 4) Exit Program")
    print("-----------------------------------------------")

def error():
    print("\n------------------------------------------------ \nPlease make another choice.\n")

error()
menu()

choice = int(input("Please make a choice: "))

while choice != 4:

    if choice == 1:
        print(car)
        x = int(input("Please press 1 to return to menu: "))

        if x != 1:
            error()
            continue

    if choice == 2:
        print(price)
        x = int(input("Please press 1 to return to menu: "))

        if x != 1:
            error()
            continue

    if choice == 3:
        print(f"\nCurrent car in list: {car}")
        car_add = input("Please write the name of the car: ")
        car_price = input("Please name the price: ")
        car.insert(0,car_add)
        price.insert(0,car_price)
        print(f"\nupdated list:\n{car}\n{price}")

    else:
        print("Not a valid selection. Please try again.")

    print("-----------------------------------------------")
    menu()
    choice = int(input("Please make a choice: "))

print("\nThank you for being our user. Have a nice day! :D")