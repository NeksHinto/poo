import unittest
from typing import List

from tp6 import (Account, Owner, Transaction)

moe: Owner = Owner(1, "Moe") # => {id_number: 1, name: "Moe"}
larry: Owner = Owner(2, "Larry")
curly: Owner = Owner(10, "Curly")

class AccountTest(unittest.TestCase):

    def test_creation_owner(self):
        self.assertEqual("Moe", moe.name)

    def test_creation_account(self):
        moe_account = Account(1, moe) # => moe = {id_number: 1, name: "Moe"}
        self.assertEqual(1, moe_account.account_number)
        self.assertEqual(1, moe_account.owner.id_number)
        self.assertEqual("Moe", moe_account.owner.name)
        self.assertEqual(0.0, moe_account.balance)
        # no es moe_account.balance, pero como no aclara, puede no ser privado

    def test_deposit(self):
        moe_account = Account(1, moe)
        moe_account.deposit(100)
        self.assertEqual(100, moe_account.get_balance())

    def test_withdraw(self):
        moe_account = Account(1, moe)
        moe_account.deposit(100)
        moe_account.withdraw(50)
        self.assertEqual(50, moe_account.get_balance())

    def test_transfer(self):
        moe_account = Account(1, moe)
        larry_account = Account(2, larry)
        moe_account.deposit(100)
        moe_account.transfer(30, larry_account)
        self.assertEqual(70, moe_account.get_balance())
        self.assertEqual(30, larry_account.get_balance())

    def test_list_accounts(self):
        moe_account = Account(1, moe)
        larry_account = Account(2, larry)
        curly_account = Account(3, curly)
        # En este test nos pide  que get_accounts() imprima una lista con 
        # las referencias (SIN REPRESENTACIÓN EN STRING) de las instancias de Account que están guardadas hasta el momento
        # Es decir, si corremos print(Account.get_accounts()), nos tendría que imprimir para cada instancia el valor que ocupa en memoria:
        # [<__main__.Account object at 0x7f09085df700>, <__main__.Account object at 0x7f09085df6a0>, <__main__.Account object at 0x7f09085df640>]
        self.assertEqual([moe_account, larry_account, curly_account], Account.get_accounts()) #estático porque llama a la clase (método de clase)
#no pone el espacio en memoria sino nombre porque no se sabe donde almacena        
# self.assertEqual(["1-Moe-0.0", "2-Larry-0.0", "10-Curly-0.0"], Account.get_accounts())

    def test_access_account(self):
        Account(1, moe) # => lo guarda en all_accounts[0]
        Account(2, larry) # => lo guarda en all_accounts[1]
        Account(3, curly) # => lo guarda en all_accounts[2]
        # Este test me dice que Account.get_account_by_number(3).name tiene que ser igual a "Curly"
        # => tendría que devolver la instancia de Owner del Account con id 3
        # self.assertEqual("Curly", Account.get_account_by_number(3).name)

        # Este test me dice que Account.get_account_by_number(3).OWNER.name tiene que ser igual a "Curly"
        self.assertEqual("Curly", Account.get_account_by_number(3).owner.name)

        self.assertEqual("Curly", Account.get_account_by_number(3).owner.name)

    def test_access_account_with_automatic_account_number(self):
        Account(moe) 
        Account(larry) 
        Account(curly) 
        self.assertEqual("Curly", Account.get_account_by_number(3).owner.name)

    def test_transactions(self):
        moe_account = Account(1, moe)
        larry_account = Account(2, larry)
        moe_account.deposit(100)
        moe_account.transfer(30, larry_account)
        moe_account.withdraw(40)
        self.assertEqual(30, moe_account.get_balance())
        transactions:List[Transaction] = moe_account.get_transactions()
        self.assertEquals(3, len(transactions))
        amounts = [t.amount for t in transactions]
        self.assertEquals([100, 30, 40], amounts)
        transferred_accounts = [t.destination_acccount for t in transactions]
        self.assertEquals([larry_account], transferred_accounts)
