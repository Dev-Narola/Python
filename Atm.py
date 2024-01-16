class Atm: 
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        print("""
                Hi How can i help you ?
                1. Press 1 to create pin
                2. press 2 to change pin
                3. press 3 to check balance
                4. press 4 to withdraw
                5. anything else to exit
                """)
        person_input = input("Enter the choice : ")

        if person_input == '1':
            #create pin
            self.createPin()
        elif person_input == '2':
            # change pin
            self.change_pin()
        elif person_input == '3':
            # check balance
            self.check_balance()
        elif person_input == '4':
            # withdrow
            self.withdraw_balance()
        else:
            exit()

    def createPin(self):
        user_pin = input('enter your pin : ')
        self.pin = user_pin
        user_balance = int(input("Enter your balance : "))
        self.balance = user_balance
        print('pin created successfuklly')
        self.menu()

    def change_pin(self):
        old_pin = input('enter old pin : ')
        if old_pin == self.pin:
            new_pin = input('enter new pin : ')
            self.pin = new_pin
            print('pin badlay gai chhe')
        else:
            print('nai karva dau ja')
        self.menu()

    def check_balance(self):
        user_pin = input('enter the pin : ')
        if user_pin == self.pin:
            print(f'your balance is {self.balance}')
        else:
            print('pin khotu chhe')
        self.menu()

    def withdraw_balance(self):
        if self.balance == 0:
            print("tamari pase paisa nathi")
            self.menu()
        w_money = int(input('tamare ketla paisa upadva chhe : '))
        user_pin = input('pin nakho : ')
        if user_pin == self.pin:
            if w_money <= self.balance:  # Use <= for comparison
                self.balance -= w_money
                print(f'tamara account mathi {w_money} paisa kapay gaya chhe.')
                print(f'have tamara account ma {self.balance} paisa chhe.')
            else:
                print(f'tamari pase {self.balance} paisa j chhe')
        else:
            print('tamek khoto pin nakhyo chhe')
        self.menu()



a = Atm()