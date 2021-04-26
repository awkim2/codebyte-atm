class Bank:
    def __init__(self):
        self.bank_data = dict()
    def add_card(self, num, pin, account, balance):
        self.bank_data[num] = {"pin number": pin, "accounts": {account: balance}}
    def add_account(self, num, account, balance):
        self.bank_data[num]["accounts"][account] = balance
    def update_balance(self, num, account, balance):
        self.bank_data[num]["accounts"][account] = balance
    def get_account(self, num, pin):
        return self.bank_data[num]
    def show_accounts(self, num):
        return list(self.bank_data[num]["accounts"].keys())
class ATM:
    def __init__(self, bank, cash):
        self.Bank = bank
        self.cash_count = cash
        self.entry = None
        self.account = None
    def insert_card(self, num, pin):
        self.entry = self.Bank.get_account(num, pin)
        if self.entry == None:
            return "Invalid Card!"
        elif pin != self.entry["pin number"]:
            return "Invalid Pin!"
        else:
            return "Welcome!"
    def select_account(self, selection):
        if selection in self.entry["accounts"]:
            return True
        else:
            return False
    def run_action(self, num, acc, action, money=0):
        if action.lower() == "show balance":
            return self.entry["accounts"][acc]
        elif action.lower() == "make a deposit":
            new_balance = self.entry["account"][acc] + money
            self.Bank.update_balance(num, acc, new_balance)
            return "Money successfull deposited! Your new balance is " + str(self.entry["accounts"][acc])
        elif action.lower() == "withdraw money":
            if money > self.entry["account"][acc]:
                return "Not enough money in account!"
            elif money > self.cash_count:
                return "Not enough cash in ATM!"
            else:
                new_balance = self.entry["account"][acc] - money
                self.Bank.update_balance(num, acc, new_balance)
                return "Retrieve your cash below!"
        else:
            return "Invalid Action!"

if __name__ == "__main__":
    bankofAndrew = Bank()
    bankofAndrew.add_card(123456789, 1234, "checking", 100)
    bankofAndrew.add_account(123456789, "savings", 1000)
    myATM = ATM(bankofAndrew, 1000)

    # getting in
    card_number = int(input("Welcome to Bank of Andrew! Insert your card to begin: "))
    pin_number = int(input("Enter your pin: "))
    print(myATM.insert_card(card_number, pin_number))
    while myATM.insert_card(card_number, pin_number) != "Welcome!":
        card_number = int(input("Welcome to Bank of Andrew! Insert your card to begin: "))
        pin_number = int(input("Enter your pin: "))
        print(myATM.insert_card(card_number, pin_number))
        print("Please try again!")

    # select account
    print(bankofAndrew.show_accounts(card_number))
    account = str(input("Select an account: "))
    while not myATM.select_account(account):
        print(bankofAndrew.show_accounts(card_number))
        account = str(input("Select a valid account: "))

    actions = ["Show Balance", "Make a Deposit", "Withdraw Money"]
    print(actions)
    action = str(input("Select an action from above: "))
    amt = 0
    if action.lower() == "make a deposit":
        amt = int(input("How much would you like to deposit? "))
    if action.lower() == "withdraw money":
        amt = int(input("How much would you like to deposit? "))
    print(myATM.run_action(card_number, account, action, amt))
    while (myATM.run_action(card_number, account, action, amt) == "Invalid Action" or myATM.run_action(card_number, account, action, amt) == "Not enough money in account!" or myATM.run_action(card_number, account, action, amt) == "Not enough cash in ATM!"):
        print(actions)
        action = str(input("Select an action from above: "))
        if action.lower() == "make a deposit":
            amt = int(input("How much would you like to deposit? "))
        if action.lower() == "withdraw money":
            amt = int(input("How much would you like to deposit? "))