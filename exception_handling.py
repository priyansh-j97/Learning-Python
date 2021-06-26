#types of common errors: ValueError and ZeroDivisionError

while True:
    try:
        value = int(input("Write your value here: "))
        print(5/value)
        break
    except ValueError:
        print("ValueError: Invalid input data type. Please enter a number.")
    except ZeroDivisionError:
        print("ZeroDivisionError: Please enter a number apart from zero.")
    except: #not recommended, as it ignores the error and further on runs the code
        break
    finally: #runs every time in the loop
        print("Loop Completed\n")