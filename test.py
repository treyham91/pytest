


class Bank:

    def __init__(self, name, id):
        """

        :param name: The name of the bank to be created
        :param id: A unique ID of integer type to identify
        the Bank
        """
        self.name = name
        self.id = id
        self.__init__(CheckingAccount)



class CheckingAccount:

    def __init__(self, name_on_account, amount, account_types=['Regular', 'Opportunity', 'Children']):
        """

        :param name_on_account: Name of the account holder
        :param amount: the amount in US dollars currently in the account
        :param account_types: 3 different categories of Checking Accounts:
                                - Regular
                                - Opporunity (which comes with higher fees)
                                - Children Checking (for kids under the age of 13)
        """
        self.amount = amount
        self.name_on_account = name_on_account
        self.account_types = account_types

    def deposit(self, amount):
        """

        :param amount: amount to be deposited, in US dollars
        :return: New account balance
        """
        if amount <= 0:
            print("You must deposit an amount more than zero.")
        else:
            self.amount += amount
            print("Thank you for the deposit of {}. Your new account\n"
                  "balance is ${}".format(amount, self.amount))
            return self.amount

    def withdrawal(self, amount, account_type):
        """

        :param amount: amount to be withdran, in US dollars
        :param account_type: the type of Checking account being withdrawn from
        :return: New account balance
        """
        if amount <= 0:
            print("You must deposit an amount more than zero.")
        elif amount > self.amount:
            CheckingAccount.overdraft_charge(account_type)
        else:
            self.amount -= amount
            print("Thank you for the deposit of {}. Your new account\n"
                  "balance is ${}".format(amount, self.amount))
            return self.amount

    def overdraft_charge(self, account_type):
        """

        :param account_type:
        :return: New account balance after an overdraft fee was placed on the account
        Each account type will have a different fee for overdrafts
        """
        # The overdraft charge amount with vary based on type of checking account
        # Regular Checking Account:
        if account_type == self.account_types[0]:
            self.amount = self.amount - 30
        # Opportunity Checking Account:
        elif account_type == self.account_types[1]:
            self.amount = self.amount - 40
        # Child Checking Account:
        elif account_type == self.account_types[2]:
            self.amount = self.amount - 5
        else:
            self.amount = self.amount



