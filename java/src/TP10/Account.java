package TP10;

import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;

public class Account {
    private Integer accountNumber = null;
    //Integer como tipo objeto (wrapper). Como es objeto puede ser puntero
    private Owner owner;
    private static List<Account> allAccounts = new ArrayList<>();
    private static List<Transaction> transactions = new ArrayList<>();
    //definir con la clase padre el tipado (tiene más métodos)
    //no inicializo en contrustor porque lo borraría cada vez que lo llamo
    //cada elemenot de la lista tiene instancia de transaction --> operador diamante
    private static int accountQuantity = 0;
    private float balance = 0.0F;
// definirlas afuera para que sean de la clase

    public Account(int account_number, Owner owner) {
        this.owner = owner;
        this.accountNumber = automaticAccountNumber(account_number);
        this.balance = balance;
        Account.allAccounts.add(this);
    }
    public Account(Owner owner) {
        this.owner = owner;
        this.accountNumber = automaticAccountNumber();
        this.balance = balance;
        Account.allAccounts.add(this);
    }
    public static int automaticAccountNumber(int accountNumber){
        return accountNumber;
    }
    public static int automaticAccountNumber(){
        return accountQuantity +=1;
    }
    //como indicar en la linea que sigue que es de tipo account?
    public static Account getAccount(Integer account_number) {
        //for each método de las colecciones
        //for más largo para guardar el índice
        for (Account a : allAccounts) {
            //TP10.Account.all_accounts=all_accounts
            //para ver si dos objetos son iguales, equals() para comparar instancias de clase
            if (a.accountNumber.equals(account_number)) {
                return a;
            }
        }
        // si llego acá es porque nunca entró al if, no hizo return porque no encontró el valor buscado
        throw new NoSuchElementException(String.format("El número de cuenta %d no tiene cuenta asociada.", account_number));
    }

    public static List<Account> getAccounts() {
        return allAccounts;
    }

    public static List<Transaction> getTransactions() {
        return transactions;
    }

    public float get_balance() {
        return this.balance;
    }

    public void deposit(float amount) {
        this.balance += amount;
        //no hace falta TP10.Account.transactions...
        transactions.add(new Transaction("Deposit", amount));
        //necesito new para crear nueva instancia. Con new llama constructor
        //recorre un constructor o el otro según la cantidad de parámetros y el tipo de los parámetros
    }

    public void withdraw(float amount) {
        if (amount <= this.balance) {
            this.balance -= amount;
            transactions.add(new Transaction("Withdrawl", amount));
        } else {
            throw new IllegalArgumentException("Fondos insuficientes");
            //porque el parámetro que paso es "ilegal"
        }
    }

    public void transfer(float amount, Account destination_account) {
        if (amount <= this.balance) {
            this.balance -= amount;
            destination_account.balance += amount;
            //le sumo al atributo, no a al objeto de la clase!
            Account.transactions.add(new Transaction("Transfer", amount));
        } else {
            throw new IllegalArgumentException("Fondos insuficientes");
        }
    }

    public Integer getAccountNumber() {
        return accountNumber;
    }

    public Owner getOwner() {
        return owner;
    }

    public float getBalance() {
        return balance;
    }
}
// para llamar a atributo o método de clase necesito nombre de clase. en python, en java no!

