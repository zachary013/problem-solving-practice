import java.util.Scanner;

// Base BankAccount class
class BankAccount {
    private String accountNumber;
    private String accountHolderName;
    protected double balance;

    public BankAccount(String accountNumber, String accountHolderName, double balance) {
        this.accountNumber = accountNumber;
        this.accountHolderName = accountHolderName;
        this.balance = balance;
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("Deposit successful. New balance: $" + balance);
        } else {
            System.out.println("Deposit amount must be positive.");
        }
    }

    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            System.out.println("Withdrawal successful. New balance: $" + balance);
        } else {
            System.out.println("Insufficient balance or invalid amount.");
        }
    }

    public void checkBalance() {
        System.out.println("Account balance: $" + balance);
    }

    public String getAccountHolderName() {
        return accountHolderName;
    }

    public String getAccountNumber() {
        return accountNumber;
    }
}

// Derived class for SavingsAccount with interest calculation
class SavingsAccount extends BankAccount {
    private double interestRate;

    public SavingsAccount(String accountNumber, String accountHolderName, double balance, double interestRate) {
        super(accountNumber, accountHolderName, balance);
        this.interestRate = interestRate;
    }

    public void addInterest() {
        double interest = balance * interestRate / 100;
        balance += interest;
        System.out.println("Interest added. New balance: $" + balance);
    }
}

// Derived class for CheckingAccount with overdraft limit
class CheckingAccount extends BankAccount {
    private double overdraftLimit;

    public CheckingAccount(String accountNumber, String accountHolderName, double balance, double overdraftLimit) {
        super(accountNumber, accountHolderName, balance);
        this.overdraftLimit = overdraftLimit;
    }

    @Override
    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance + overdraftLimit) {
            balance -= amount;
            System.out.println("Withdrawal successful. New balance: $" + balance);
        } else {
            System.out.println("Exceeds overdraft limit or invalid amount.");
        }
    }
}

// Main application to interact with the user
public class BankSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        BankAccount account;

        System.out.println("Welcome to the Bank Account Management System");

        // Sample data for the account creation
        System.out.print("Enter account type (savings/checking): ");
        String accountType = scanner.nextLine().toLowerCase();

        System.out.print("Enter account number: ");
        String accountNumber = scanner.nextLine();

        System.out.print("Enter account holder's name: ");
        String accountHolderName = scanner.nextLine();

        System.out.print("Enter initial balance: ");
        double balance = scanner.nextDouble();

        if (accountType.equals("savings")) {
            System.out.print("Enter interest rate (%): ");
            double interestRate = scanner.nextDouble();
            account = new SavingsAccount(accountNumber, accountHolderName, balance, interestRate);
        } else if (accountType.equals("checking")) {
            System.out.print("Enter overdraft limit: ");
            double overdraftLimit = scanner.nextDouble();
            account = new CheckingAccount(accountNumber, accountHolderName, balance, overdraftLimit);
        } else {
            System.out.println("Invalid account type.");
            return;
        }

        // Menu to interact with the account
        int choice;
        do {
            System.out.println("\n1. Deposit");
            System.out.println("\n2. Withdraw");
            System.out.println("\n3. Check Balance");
            if (account instanceof SavingsAccount) {
                System.out.println("\n4. Add Interest");
            }
            System.out.println("\n5. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter deposit amount: ");
                    double depositAmount = scanner.nextDouble();
                    account.deposit(depositAmount);
                    break;
                case 2:
                    System.out.print("Enter withdrawal amount: ");
                    double withdrawAmount = scanner.nextDouble();
                    account.withdraw(withdrawAmount);
                    break;
                case 3:
                    account.checkBalance();
                    break;
                case 4:
                    if (account instanceof SavingsAccount) {
                        ((SavingsAccount) account).addInterest();
                    } else {
                        System.out.println("Invalid option for this account type.");
                    }
                    break;
                case 5:
                    System.out.println("Thank you for using the Bank System.");
                    break;
                default:
                    System.out.println("Invalid choice.");
            }
        } while (choice != 5);

        scanner.close();
    }
}
