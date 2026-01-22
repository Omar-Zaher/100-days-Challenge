
# ========== Functions ================
def sum(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Error: Division by zero" # Handle division by zero
    return a / b
# ====================================

num1 = float(input("Enter first number: "))
ending = False

# ******** Operation Mapping *************
op = {
    '+': sum,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# ========= Main Program =============
while ending == False:
    try:
        operations = input("Enter operation (+, -, *, /): ")

        num2 = float(input("Enter second number: "))

        calculation_function = op[operations] # Get the function based on user input
        answer = calculation_function(num1, num2)
        print(f"{num1} {operations} {num2} = {answer}")
            
        user_input = input(f"Do you want to perform another calculation on {answer}? (yes/no): ").lower()

        if user_input == 'yes':
            num1 = answer
        else:
            ending = True
            print("Goodbye!")
            
    # ******** Error Handling *************
    except KeyError:
        print("Invalid operation. Please enter one of +, -, *, /.")
        
    except ValueError:
        print("Invalid input. Please enter numeric values.")
# ====================================