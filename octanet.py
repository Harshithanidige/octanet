import time

print("please insert YOUR CARD")

time.sleep(5)

password = 1234

pin = int(input("enter your atm pin"))

balance = 5000

if pin == password:
    while True:

        print("""
            1 == balance
            2 == withdraw balance
            3 == deposite balance
            4 == exit
            """
            )

        try:
            option = int(input("please enter your choise "))
        except:
            print("please enter valid option")


        if option == 1:
            print(f"Yuor current balance is {balance}")

        if option == 2:

            withdraw_amount = int(input("please enter withdraw_amount "))

            balance = balance = withdraw_amount

            print(f"{withdraw_amount} is dedited from your account")

            print(f"your current balance is {balance}")

        if option==3:
        
            deposite_amount = int(input("please enter deposite_amount"))

            balance = balance = deposite_amount

            print(f"{deposite_amount} is credited to your account")

            print(f"your updated balance is {balance}")
        
        if option == 4:

            break


else:
    print("wrong pin please try again")
