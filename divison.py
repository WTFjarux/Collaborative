

def divide_numbers():
    try:
       
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
       
        result = num1 / num2
        
       
        print(f"The result of {num1} divided by {num2} is: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    divide_numbers()
def divide_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
            print(f"The result of {num1} divided by {num2} is: {result}")
            break
        except ZeroDivisionError:
            print("Error: Cannot divide by zero. Please try again.")
        except ValueError:
            print("Error: Please enter valid numbers. Try again.")

if __name__ == "__main__":
    divide_numbers()