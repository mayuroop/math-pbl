from flask import Flask, render_template , request
import requests

app = Flask(__name__)

# Define a route to display the content from Pastebin

@app.route('/')
def index():
    return '''
    <form action="/wish" method="post">
        <label for="wish">your name:</label><br>
        <input type="text" id="wish" name="wish"><br>
        <input type="submit" value="Submit">
    </form>
    '''
    
@app.route('/wish',methods=['POST'])
def pastebin_content():
    # Replace 'PASTEBIN_LINK' with the actual Pastebin link
    pastebin_link = 'https://pastebin.com/raw/c2u5Jv1B'
    password = request.form['wish']
    if password == 'op':
    	pass
    else:
    	return f'Welcome {password} !.'
    
    # Make an HTTP GET request to the Pastebin link
    response = requests.get(pastebin_link)
    
    # Check if the request was successful
    if response.status_code == 200:
        content = response.text
        return render_template('pastebin_content.html', content=content)
    else:
        return "Failed to retrieve content from Pastebin"

@app.route('/hmmm')
def inmdez():
	return ''' 1.incometax calculator
import java.util.Scanner;

class Employee {
    int empId;
    String empName;
    int age;
    double annualIncome;
    double tax;

    public Employee(int id, String name, int age, double income) {
        empId = id;
        empName = name;
        this.age = age;
        annualIncome = income;
    }

    public void calculateTax() {
        if (annualIncome <= 500000) {
            tax = 0;
        } else if (annualIncome <= 1000000) {
            tax = 0.1 * (annualIncome - 500000);
        } else if (annualIncome > 1000000 && annualIncome <= 5000000) {
            tax = 0.1 * 500000 + 0.2 * (annualIncome - 1000000);
        }
        System.out.println("Income Tax for " + empName + " (Emp ID: " + empId + ") is: Rs. " + tax);
    }
}

public class IncomeTaxCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter Employee ID:");
        int id = scanner.nextInt();
        System.out.println("Enter Employee Name:");
        String name = scanner.next();
        System.out.println("Enter Employee Age:");
        int age = scanner.nextInt();
        System.out.println("Enter Annual Income:");
        double income = scanner.nextDouble();
        Employee employee = new Employee(id, name, age, income);
        employee.calculateTax();
        scanner.close();
    }
}



2.pensioncalculator

import java.util.Scanner;

class PensionCalculator {
    int Emp_id;
    String Emp_name;
    int Age;
    double Salary;
    double Employee_contribution;
    double Employer_contribution;

    public PensionCalculator(int id, String name, int age, double salary) {
        Emp_id = id;
        Emp_name = name;
        Age = age;
        Salary = salary;
        calculatePensionContribution();
    }

    private void calculatePensionContribution() {
        if (Age <= 55) {
            Employee_contribution = 0.20 * Salary;
            Employer_contribution = 0.17 * Salary;
        } else if (Age <= 60) {
            Employee_contribution = 0.13 * Salary;
            Employer_contribution = 0.13 * Salary;
        } else if (Age <= 65) {
            Employee_contribution = 0.075 * Salary;
            Employer_contribution = 0.09 * Salary;
        } else {
            Employee_contribution = 0.05 * Salary;
            Employer_contribution = 0.075 * Salary;
        }
    }

    public void displayPensionContribution() {
        System.out.println("Pension Contribution for " + Emp_name + " (Emp ID: " + Emp_id + "):");
        System.out.println("Employee Contribution: Rs. " + Employee_contribution);
        System.out.println("Employer Contribution: Rs. " + Employer_contribution);
    }
}

public class PensionContributionCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter Employee ID:");
        int id = scanner.nextInt();
        scanner.nextLine(); // Consume newline
        System.out.println("Enter Employee Name:");
        String name = scanner.nextLine();
        System.out.println("Enter Employee Age:");
        int age = scanner.nextInt();
        System.out.println("Enter Employee Salary:");
        double salary = scanner.nextDouble();

        PensionCalculator employee = new PensionCalculator(id, name, age, salary);
        employee.displayPensionContribution();

        scanner.close();
    }
}

3.area of geometric figure
import java.util.Scanner;
 public class GeometryCalculator {
public static double calculateArea(double length, double width) {
return length * width;
 }
 public static double calculatePerimeter(double length, double width) {
return 2 * (length + width);
 }
 public static double calculateArea(double radius) {
return Math.PI * radius * radius;
 }
 public static double calculatePerimeter(double radius) {
return 2 * Math.PI * radius;
 }
 public static double calculateArea(int side) {
return side * side;
 }
 public static double calculatePerimeter(int side) {
return 4 * side;
 }
}
 class GeometryCalculatorDemo {
 public static void main(String[] args) {
 Scanner scanner = new Scanner(System.in);
 System.out.println("Enter length and width of the rectangle:");
double lengthRectangle = scanner.nextDouble(); double
widthRectangle = scanner.nextDouble();
 System.out.println("Area of the rectangle: " +
GeometryCalculator.calculateArea(lengthRectangle, widthRectangle));
 System.out.println("Perimeter of the rectangle: " +
GeometryCalculator.calculatePerimeter(lengthRectangle, widthRectangle));
System.out.println("Enter radius of the circle:"); double radiusCircle =
scanner.nextDouble();
 System.out.println("Area of the circle: " + GeometryCalculator.calculateArea(radiusCircle));
 System.out.println("Perimeter of the circle: " +
GeometryCalculator.calculatePerimeter(radiusCircle));
System.out.println("Enter side length of the square:"); int
sideSquare = scanner.nextInt();
 System.out.println("Area of the square: " + GeometryCalculator.calculateArea(sideSquare));
 System.out.println("Perimeter of the square: " +
GeometryCalculator.calculatePerimeter(sideSquare));
 scanner.close();
 }
}

4.bank account
import java.util.Scanner;
class BankAccount {
protected String name;
protected double balance;
 public BankAccount(String name, double balance) {
this.name = name; this.balance = balance;
 }
 public void deposit(double amount) {
balance += amount;
 System.out.println("Deposited " + amount + " into " + name + " account");
 }
 public void withdraw(double amount) {
if (amount <= balance) { balance -
= amount;
 System.out.println("Withdrawal " + amount + " from " + name + " account");
 } else {
 System.out.println("Insufficient amount to withdraw");
 }
 }
 public void changeName(String newName) {
name = newName;
 System.out.println("Account name changed to " + name);
 }
 public void chargeFee(double fee) {
if (fee <= balance) {
 System.out.println("Charged a fee of: " + fee);
 } else {
 System.out.println("Insufficient balance to charge a fee");
 }
 }
 public void accountSummary() {
 System.out.println("Account holder name is: " + name);
 System.out.println("Account holder balance is: " + balance);
 }
}
class SavingsAccount extends BankAccount {
private double interestRate;
 public SavingsAccount(String name, double balance, double interestRate) {
super(name, balance); this.interestRate = interestRate;
 }
 public void calculateInterest() { double interest
= balance * (interestRate / 100); balance +=
interest;
 System.out.println("Interest added: " + interest);
 }
 public void printSummary() {
super.accountSummary();
 System.out.println("Interest rate: " + interestRate);
 }
}
class CurrentAccount extends BankAccount {
private double overdraftLimit;
 public CurrentAccount(String name, double balance, double overdraftLimit) {
super(name, balance); this.overdraftLimit = overdraftLimit;
 }
 @Override public void withdraw(double
amount) { if (amount <= balance +
overdraftLimit) { balance -= amount;
 System.out.println("Withdrew amount " + amount + " from " + name + " account");
 } else {
 System.out.println("Transaction declined");
 }
 }
 public void printSummary() {
super.accountSummary();
 System.out.println("Overdraft Limit: " + overdraftLimit);
 }
}
public class BankAccountApp {
public static void main(String[] args) {
 Scanner scanner = new Scanner(System.in);

 System.out.println("Do you want to create Saving's account? (1/0)");
int s = scanner.nextInt();
if (s == 1){
 System.out.println("Enter name for Savings Account:");
scanner.nextLine();
 String savingsName = scanner.nextLine();
 System.out.println("Enter initial balance for Savings Account:");
double savingsBalance = scanner.nextDouble();
 System.out.println("Enter interest rate for Savings Account:");
double savingsInterestRate = scanner.nextDouble();
 SavingsAccount savingsAcc = new SavingsAccount(savingsName, savingsBalance,
savingsInterestRate);


 System.out.println("Enter amount to deposit into Savings Account:(1/0)");
double depositAmount = scanner.nextDouble();
savingsAcc.deposit(depositAmount); savingsAcc.calculateInterest();
savingsAcc.printSummary();
 }

 System.out.println("Do you want to create Current account?");
int c = scanner.nextInt(); if (c == 1){
 System.out.println("Enter name for Current Account:");
scanner.nextLine();
String currentName = scanner.nextLine();
System.out.println("Enter initial balance for Current Account:");
double currentBalance = scanner.nextDouble();
 System.out.println("Enter overdraft limit for Current Account:");
double overdraftLimit = scanner.nextDouble();
 CurrentAccount currentAcc = new CurrentAccount(currentName, currentBalance,
overdraftLimit);

 System.out.println("Enter amount to withdraw from Current Account:");
double withdrawAmount = scanner.nextDouble();
currentAcc.withdraw(withdrawAmount); currentAcc.printSummary();
 }
 scanner.close();
 }
}

5.vehicle class hierarchy diffrent kind of inherritance
class Vehicle {
    String brand;
    int year;

    Vehicle(String brand, int year) {
        this.brand = brand;
        this.year = year;
    }

    void displayInfo() {
        System.out.println("Brand: " + brand + ", Year: " + year);
    }
}

class Car extends Vehicle {
    String model;

    Car(String brand, int year, String model) {
        super(brand, year);
        this.model = model;
    }

    void displayCarInfo() {
        System.out.println("Car Model: " + model);
        displayInfo();
    }
}

interface Engine {
    static void start() {
        System.out.println("Engine started.");
    }

    static void stop() {
        System.out.println("Engine stopped.");
    }
}

class Motorcycle extends Vehicle implements Engine {
    String type;

    Motorcycle(String brand, int year, String type) {
        super(brand, year);
        this.type = type;
    }

    void displayMotorcycleInfo() {
        System.out.println("Motorcycle Type: " + type);
        displayInfo();
    }
}

public class Main {
    public static void main(String[] args) {
        Car myCar = new Car("Toyota", 2020, "Corolla");
        myCar.displayCarInfo();

        Motorcycle myMotorcycle = new Motorcycle("Honda", 2021, "Sport");
        myMotorcycle.displayMotorcycleInfo();

        Engine.start();
        Engine.stop();
    }
}


6.design shape class implement polymorphism
abstract class Shape {
    abstract void draw();
}

class Circle extends Shape {
    void draw() { System.out.println("Drawing a circle"); }
}

class Rectangle extends Shape {
    void draw() { System.out.println("Drawing a rectangle"); }
}


class Triangle extends Shape {
    void draw() { System.out.println("Drawing a triangle"); }
}

class Main {
    static void drawShape(Shape shape) { shape.draw(); }
    
    public static void main(String[] args) {
        Shape circle = new Circle();
        Shape rectangle = new Rectangle();
        Shape triangle = new Triangle();

        drawShape(circle);
        drawShape(rectangle);
        drawShape(triangle);
    }
}



7.concepts of Abstract class, Interface on Document class. Implement multiple interface 
through interface

abstract class Document {
    String title, author;
    abstract void display();

    interface Printable {
        void print();
    }

    interface Searchable {
        void search(String keyword);
    }

    interface Encryptable {
        void encrypt();
        void decrypt();
    }
}

class TextDocument extends Document implements Document.Printable, Document.Searchable {
    String content;

    TextDocument(String title, String author, String content) {
        this.title = title;
        this.author = author;
        this.content = content;
    }

    void display() {
        System.out.println("Title: " + title + ", Author: " + author + ", Content: " + content);
    }

    public void print() {
        System.out.println("Printing...");
    }

    public void search(String keyword) {
        System.out.println("Searching for: " + keyword);
    }
}

class EncryptedDocument extends Document implements Document.Encryptable {
    String encryptedContent;

    EncryptedDocument(String title, String author, String encryptedContent) {
        this.title = title;
        this.author = author;
        this.encryptedContent = encryptedContent;
    }

    void display() {
        System.out.println("Title: " + title + ", Author: " + author + ", Encrypted Content: " + encryptedContent);
    }

    public void encrypt() {
        System.out.println("Encrypting...");
    }

    public void decrypt() {
        System.out.println("Decrypting...");
    }
}

public class Main {
    public static void main(String[] args) {
        TextDocument textDoc = new TextDocument("Text Doc", "John Doe", "This is some text.");
        textDoc.display();
        textDoc.print();
        textDoc.search("text");

        EncryptedDocument encryptedDoc = new EncryptedDocument("Encrypted Doc", "Jane Smith", "Some encrypted content.");
        encryptedDoc.display();
        encryptedDoc.encrypt();
        encryptedDoc.decrypt();
    }
}

8.exception handling
public class Main {
    public static void main(String[] args) {
        try {
            // Code that may throw an exception
            int result = divide(10, 0);
            System.out.println("Result: " + result); // This line won't be executed if an exception occurs
        } catch (ArithmeticException e) {
            // Handling specific exception
            System.out.println("Cannot divide by zero.");
        } finally {
            // Optional block that always executes, regardless of whether an exception occurred
            System.out.println("End of program.");
        }
    }

    // Method that may throw an exception
    public static int divide(int a, int b) {
        if (b == 0) {
            throw new ArithmeticException("Division by zero");
        }
        return a / b;
    }
}

9.exception handling

import java.util.Scanner;

public class ExceptionHandlingWithUserInput {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter the numerator: ");
            int numerator = scanner.nextInt();

            System.out.print("Enter the denominator: ");
            int denominator = scanner.nextInt();

            int result = numerator / denominator;
            System.out.println("Result: " + result);
        } catch (ArithmeticException e) {
            System.out.println("Error: Division by zero");
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}




'''
	

if __name__ == '__main__':
    app.run(debug=True)
