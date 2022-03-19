### BUG ALERT: Application doesnt exist when entering invalid input. Instead it restarts the application from ending operator input.


#import logo from art.py
from art import logo


###Creating calculating functions section
#Creat add function
def add(number1, number2):
  return number1 + number2
#Creat subtract function 
def subtract(number1, number2):
  return number1 - number2
#Creat multiply function 
def multiply(number1, number2):
  return number1 * number2
#Creat divide function 
def divide(number1, number2):
  return number1 / number2

#Creating a dictionary to associate each operator with its function
#Operators as keys and functions as values
operation = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}


##################################################################################################################


def calc_app():
  '''Creating a function that allows user to restart again (using recursion)'''
  
  print(logo)
  print("||WELCOME TO YOUR PERSONAL CALCULATOR||\n")
  
  #User input first number 
  first_number = float(input("Enter first number: "))

  #Ask user if they want to continue calcolating or exit the program part_1
  should_continue = True #flag for while loop
  while should_continue:

    #User selects operator 
    operator = input("Choose an operator +   -   *   /  : ")
    #User input second number 
    second_number = float(input("Enter next number: "))


    #based on the operator the user chose, operation dict will be replaced by a value aka (function).
    calc_functions = operation[operator] #operation['+'] for example will tab into related function
    calc_result = calc_functions(first_number, second_number) #example add(first_number, second_number)

    #print results
    print(f"{first_number} {operator} {second_number} = {calc_result}")
    
    #Ask user if they want to continue calculating or if they want to restart a new calculation part_2
    continue_calc = input(f"Type \'y\' if you wish to continue calculating {calc_result} or type \'n\' to start a new calculation: ").lower()
    if continue_calc == 'n': #invokes recursion by calling the function inside itself starting the application from printing logo
      should_continue = False
      calc_app()
    elif continue_calc == 'y':#replaces first_number input with calc_result and starts the application from while should_continue
      first_number = calc_result
      should_continue = True
    else: #debug
      print("Invalid selection. Exit program")

#calling the calculator program
calc_app()
