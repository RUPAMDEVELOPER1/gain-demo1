1> def calculate_sum():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise TypeError("Inputs must be numerical values.")
        
        result = num1 + num2
        
        print("Sum:", result)
    except TypeError as e:
        print("Error:", e)
    except ValueError:
        print("Error: Please enter valid numerical values.")

calculate_sum()

2>def get_input():
    try:
        num = float(input("Enter a number: "))
        print("You entered:", num)
    except KeyboardInterrupt:
        print("\nInput was canceled by the user.")

get_input()
3>def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print("File content:\n", content)
    except UnicodeDecodeError as e:
        print("UnicodeDecodeError:", e)
        print("There was an encoding issue while reading the file.")

filename = input("Enter the filename: ")
read_file(filename)
4>Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist
def list_operation(input_list):
    try:
        length = input_list.length  # Attempting to access the 'length' attribute
        print("Length of the list:", length)
    except AttributeError as e:
        print("AttributeError:", e)
        print("The 'length' attribute does not exist for the provided list.")

# Example list
my_list = [1, 2, 3, 4, 5]

list_operation(my_list)

