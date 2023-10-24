from __future__ import annotations
from typing import List

class Account:
    all_accounts:List[Account]=[]
    transactions:List[Transaction]=[]
    account_quantity = 0

    def __init__(self, owner:Owner, account_number=None):
        # puedo asignarle directamente el parámetro owner porque 
        # es de tipo Owner (y el atributo de instancia owner también!)
        self.owner:Owner = owner 
        self.account_number:int = Account.automatic_account_number(account_number)
        self.balance = 0.0
        Account.all_accounts.append(self)
        
    @staticmethod
    def automatic_account_number(account_number):
        if account_number is None: 
            Account.account_quantity+=1
            return Account.account_quantity
        else: 
            return account_number

	# def __repr__(self): #sirve para cualquier return de una instancia de la clase
    #   return f"{self.owner.id_number}-{self.owner.name}-{self.balance}"

    @staticmethod
    def get_account_by_number(account_number):
        # recorro la lista all_accounts, que la llamo con el prefijo de la clase Account porque es un atributo de clase
        for account in Account.all_accounts: 
            # variable account del for es un iterador, o sea, va saltando de elemento en elemento en la 
            # lista all_accounts. En cada iteración va a ser una instancia distinta de Account, porque 
            # los elementos de la lista all_accounts son de tipo Account
            if account.account_number == account_number: 
                return account
        raise ValueError(f"El número de cuenta {account_number} no tiene cuenta asociada") #si ya hizo return no lee esta linea

    # Otra posible solución sabiendo que el lugar que ocupa cada account en la lista coincide con account_number-1
    # def get_account_by_number(account_number):
	#   if all_accounts[account_number-1] is not None:
    #       return all_accounts[account_number-1]
    #   raise ValueError(f"El número de cuenta {account_number} no tiene cuenta asociada") #si ya hizo return no lee esta linea
    
    # "Getter" de atributo de clase all_accounts (podría ser privado)
    @staticmethod
    def get_accounts(): 
        return(Account.all_accounts)
    
    # "Getter" de atributo de clase transactions (podría ser privado)
    @staticmethod
    def get_transactions(): 
        return(Account.transactions)
    
    # "Getter" de atributo de instancia balance (podría ser privado)
    def get_balance(self):
        return(self.balance)
    
    def deposit(self, amount):
        self.balance += amount 
        Account.transactions.append(Transaction("Deposit", amount))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            Account.transactions.append(Transaction("Withdrawal", amount))
        else: 
            raise ValueError("Fondos insuficientes")

    def transfer(self, amount:float, destination_account:Account):
        if amount <= self.balance: 
            self.balance -= amount
            destination_account.balance += amount 
            Account.transactions.append(Transaction("Transfer", amount, destination_account))
        else:
            raise ValueError("Fondos insuficientes")


class Transaction: 
    def __init__(self, type:str, amount:float, destination_account:Account=None):
        self.type = type
        self.amount = amount
        if type == "Transfer": # si no es transfer no lo agrega el None porque no lo inicializo
            self.destination_account = destination_account
        

class Owner:
    def __init__(self, id_number:int, name:str): 
        self.id_number=id_number
        self.name=name


moe: Owner = Owner(1, "Moe") # => {id_number: 1, name: "Moe"}
larry: Owner = Owner(2, "Larry")
curly: Owner = Owner(10, "Curly")
Account(moe, 1) 
Account(larry, 2) 
Account(curly, 3) 
print(Account.get_account_by_number(3).owner.name)