# ------- Calculator ---------
from art import logo

# add
def add(n1, n2):
  return n1 + n2


# subtract
def sub(n1, n2):
  return n1 - n2


# Multiply
def multiply(n1, n2):
  return n1 * n2


# Divide
def divide(n1, n2):
  return n1 / n2


operations = {"+": add, "-": sub, "*": multiply, "/": divide}


def calculator():
  print(logo)
  num1 = float(input("What's the firt number: "))
  for keys in operations:
    print(keys)
  continue_calculation = True
  while continue_calculation:

    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number: "))
    function = operations[operation_symbol]
    answer = function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    if input(
        f"Type 'y' to continue calculating with {answer}, type 's' to start new caluclation, or type 'n' to exist: "
    ) == "y":
      num1 = answer
    elif input(
        f"Type 'y' to continue calculating with {answer}, type 's' to start new caluclation, or type 'n' to exist: "
    ) == "s":
      calculator()
    else:
      continue_calculation = False


calculator()
