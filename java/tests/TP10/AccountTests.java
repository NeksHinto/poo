package TP10;

import TP10.Account;
import TP10.Owner;
import TP10.Transaction;
import org.junit.Test;

import java.util.List;
import java.util.stream.Collectors;

import static junit.framework.TestCase.assertEquals;

public class AccountTests {

    Owner moe = new Owner(1, "Moe");
    Owner larry = new Owner(2, "Larry");
    Owner curly = new Owner(10, "Curly");

    @Test
    public void testCreationAccount() {
        Account moeAccount = new Account(1, moe);
        // assertEquals(1, moeAccount.getAccountNumber());
        assertEquals(1, moeAccount.getOwner().getIdNumber());
        assertEquals("Moe", moeAccount.getOwner().getName());
        assertEquals(0.0, moeAccount.getBalance());
    }

    @Test
    public void testDeposit() {
        Account moeAccount = new Account(1, moe);
        moeAccount.deposit(100);
        assertEquals(100.0, moeAccount.getBalance());
    }

    @Test
    public void testWithdraw() {
        Account moeAccount = new Account(1, moe);
        moeAccount.deposit(100);
        moeAccount.withdraw(50);
        assertEquals(50, moeAccount.getBalance());
    }

    @Test
    public void testTransfer() {
        Account moeAccount = new Account(1, moe);
        Account larryAccount = new Account(2, larry);
        moeAccount.deposit(100);
        moeAccount.transfer(30, larryAccount);
        assertEquals(70.0, moeAccount.getBalance());
        assertEquals(30.0, larryAccount.getBalance());
    }

    @Test
    public void testListAccounts() {
        Account moeAccount = new Account(1, moe);
        Account larryAccount = new Account(2, larry);
        Account curlyAccount = new Account(3, curly);
        assertEquals(List.of(moeAccount, larryAccount, curlyAccount), Account.getAccounts());
    }

    @Test
    public void testAccessAccount() {
        Account accountMoe = new Account(1, moe);
        Account accountLarry = new Account(2, larry);
        Account accountCurly = new Account(3, curly);
        assertEquals("Curly", Account.getAccountByNumber(3).getOwner().getName());
    }

    @Test
    public void testTransactions() {
        Account moeAccount = new Account(1, moe);
        Account larryAccount = new Account(2, larry);
        moeAccount.deposit(100);
        moeAccount.transfer(30, larryAccount);
        moeAccount.withdraw(40);
        assertEquals(30.0, moeAccount.getBalance());
        List<Transaction> transactions = moeAccount.getTransactions();
        assertEquals(3, transactions.size());
        List<Float> amounts = transactions.stream().map(Transaction::getAmount).collect(Collectors.toList());
        assertEquals(List.of(100, 30, 40), amounts);
    }
}