class ATM :
    def __init__(self,cardnumber,pin) :
         self.cardnumber = cardnumber
         self.pin = pin
    def CashWithdrawl(self) :
         print("you can withdraw your cash hear")

    def BalanceEnquiry(self) :
         print("you can enquire here")
    def main():
      cardnumber1 = input("insert your card number:- ")
      pin1  = input("enter your pin number:- ")

      new_user =  ATM(cardnumber1 ,pin1)

      print("Choose your activity ")
      print("1.Balance Enquriy   2.withdrawl")
      activity = int(input("enter activity number :- "))

      if (activity == 1):
        new_user.BalanceEnquiry()
      elif (activity == 2):
        amount = int(input("enter the amount:- "))
        new_user.CashWithdrawl(amount)
      else:
        print("enter a valid number")


   # if _name_ == "_main_":
    main()
