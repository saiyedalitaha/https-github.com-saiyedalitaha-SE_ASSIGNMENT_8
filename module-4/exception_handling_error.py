def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Please provide numbers.")
    else:
        print("Result:", result)
    finally:
        print("Execution completed.")


divide_numbers(10, 2)  
divide_numbers(10, 0)  
divide_numbers(10, 'a')  
