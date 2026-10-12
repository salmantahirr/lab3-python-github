def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
def even_odd(num):
    if num % 2 == 0:
        return f"{num} is Even."
    else:
        return f"{num} is Odd."
def percentage(part, total):
    if total == 0:
        return "Error: Total cannot be zero for percentage calculation."
    return (part / total) * 100

def main():
  while True:
    print("Welcome to the Feature-Rich Calculator!")
    print("Select an operation:")
    print("1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Check Even/Odd \n 6. Calculate Percentage \n 7. Exit")
    choice = input()
    if choice in ["1", "2", "3", "4"]:
        print("Enter two numbers:")
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        if choice == "1":
            print(f"Result: {add(num1, num2)}")
        elif choice == "2":
            print(f"Result: {subtract(num1, num2)}")
        elif choice == "3":
            print(f"Result: {multiply(num1, num2)}")
        elif choice == "4":
            print(f"Result: {divide(num1, num2)}")
    elif choice == "5":
        print("Enter a number:")
        num = int(input("Number: "))
        print(even_odd(num))
    elif choice == "6":
        print("Enter part and total for percentage calculation:")
        part = float(input("Part: "))
        total = float(input("Total: "))
        print(f"Percentage: {percentage(part, total)}%")
    elif choice == "7":
        print("Exiting calculator. Thank you!")
        break
    elif choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
 main()
