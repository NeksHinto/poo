package TP10;

public class Transaction{
    private String type;
    private float amount;
    private Account destination_account;
    //null no es valor de default porque tengo doble constructor

    public Transaction(String type, float amount, Account destination_account) {
        this.type = type;
        this.amount = amount;
        if (type == "Transfer")
            this.destination_account = destination_account;
    }
    //múltiples constructores. En el caso de que instancien con Y sin destination account
    public Transaction(String type, float amount) {
        this.type = type;
        this.amount = amount;
    }

    public float getAmount() {
        return amount;
    }
}