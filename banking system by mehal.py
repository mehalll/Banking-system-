from termcolor import colored

print(colored('\t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t BANKING SYSTEM BY MEHAL', 'blue'))


print("\t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t   WELCOME TO THE STATE BANK OF PAKISTAN ","\n")


balance = 80
restart = ('Y')
tries = 3

while tries >= 0:
    user_input = int(input("Enter your key: "))
    if user_input == (1234):
        print("you have entered the correct key\n")

        while restart not in ('n','N','NO','no',"\n"):
            print("Press 1 for withdrawl\n")
            print("press 2 for balance enquiry\n")
            print("press 3 for to pay in\n")
            print("press 4 to take your card back\n")
            option = int(input("what would you like to choose: "))
            if option == 2:
                print("your balance is $",balance,"\n")

                restart = input("Would you like to go back ? ")
                if restart in ('n','N','NO','no',"\n"):
                    print("THANKYOU")
                    break
            elif option == 1:
                option2 = ('Y')
                withdrawl_money = float(input("how much money you want to withdraw? \n $10/$20/$40/$60/$80/$100 "))
                if withdrawl_money in [10, 20, 40, 60, 80, 100]:
                    balance = balance - withdrawl_money
                    print("\n Your balance is now $", balance)


                    restart = input("Would you like to go back ? ")
                    if restart in ('n','N','NO','no',"\n"):
                        print("THANKYOU")
                        break

                elif withdrawl_money != [10, 20, 40, 60, 80, 100]:
                    print(' INVALID AMOUNT, PLEASE RETRY \n')
                    restart = ('y')


            elif option == 3:
                pay_in = float(input("How much would you like to pay in?: "))
                balance = balance + pay_in
                print(" \n Your balaance is now :", balance)

                restart = input("Would you like to go back ? ")
                if restart in ('n','N','NO','no',"\n"):
                        print("THANKYOU")
                        break

            elif option == 4:
                print("PLEASE WAIT UNTIL YOU CARD IS RETURNED")
                print("THANKYOU FOR YOUR TIME")
                break

            else:
                print("ENTER THE CORRECT NUMBER, \n ")
                restart = ('y')

    elif user_input != (1234):
        print("INCORRECT PASSWORD")
        tries = tries - 1
        if tries == 0:
            print("\n NO MORE TRIES")
            break
