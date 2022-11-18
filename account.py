class Account:

    def __init__(self, name) -> None:
        """
        Method to initialize the values.
        :param name: The name of the account.
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount) -> bool:
        """
        A method that deposits the amount into account as long as the amount is greater than 0.
        :param amount: The amount of money to be deposited to the account.
        :return: Returns a Boolean, False if depositing a negative amount, and returns True if greater than 0.
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount) -> bool:
        """
        A method that withdraws the amount from the account as long as the amount is greater than 0 but not more
        than the amount that is already in the account.
        :param amount: The amount of money to be withdrawn from the account.
        :return: Returns a Boolean, False if withdrawing a negative amount or an amount greater than what's in the
        account, and returns True if greater than 0 and less than the amount in the account.
        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Method to get account balance.
        :return: Returns the account balance.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method to get account name.
        :return: Returns the account balance.
        """
        return self.__account_name
