# passing arguments to the function


# positional Argument
def greet1(name, message):
  print("f'Hello, {name}! {message}'")


greet1("John", "How are you?")

# keyword Argument
greet1(name="John", message="How are you?")


# Default Argument
def greet(name, message="How are you?"):
  print("f'Hello, {name}! {message}'")


# variable-length argument list
def multiply(*args):
  result = 1
  for num in args:
    result *= num
  return result


print(multiply(2, 3, 4, 5))


# Arbitrary Keyword Arguments
def print_info(**kwargs):
  for key, value in kwargs.items():
    print(f"{key}: {value}")


print_info(name="John", age=30, city="New York")


# passing by reference
def modify_list(my_list):
  my_list.append(4)


original_list = [1, 2, 3]
modify_list(original_list)
print(original_list)
