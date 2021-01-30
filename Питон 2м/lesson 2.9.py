class BankAccount:
    name = 'Aidar'        #public
    _passport = 'an203832' #potectod / public
    __balance = 0           #private

    def get_balance(self):
        return self.__balance

account = BankAccount()
account.name ='Azamat'
print(account.name, account._passport, account.get_balance())