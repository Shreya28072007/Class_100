class Atm :
    
    def __init__(self , cardNumber , pin) :
        self.cardNumber = cardNumber
        self.pin = pin

    def check_balance(self) :
        print("Your balance is ₹15000")

    def withdrawl(self, amount) :
        new_Amount = 15000 - amount
        print("You have withdrawed amount " + str(amount) + ". Your remaining balance is " + str(new_Amount))

def main() :
    card_number = input("Insert your cardnumber :- ")
    pinnumber = input("Enter you pin number :- ")
    new_User = Atm(card_number , pinnumber)
    print("Choose your activity ")
    print("1. Balance Enquiry 2. withdrawl")

    activity = int(input("Enter activity number :- "))

    if ( activity == 1) :

        new_User.check_balance()

    elif (activity ==  2) :

        amount = int(input("Enter the amount :- "))
        new_User.withdrawl(amount)

    else :

        print("Enter a valid number")

if __name__ == "__main__" :
    main()