# Some Functional Programming Principles

# # Recursive Functions: means a Function that calls itself

def check_exit():
    command = input("FP> ")
    if command.lower() == "exit":
        exit()
    else:
        check_exit()

# # Pure Functions: Functions that does'nt have side effects

names = ['Hussain', 'Teebah']

# # # Inpure Funtion

def add_name_inpurely(new_name):
    names.append(new_name)

# # # Pure Function

def add_name_purely(names, new_name):
    new_names = list(names)
    new_names.append(new_name)


# # Currying: I don't know how to explain

# # # without currying:

def add_numbers_without_currying(number1, number2, number3):
    return number1 + number2 + number3

# # # # we call it like this "add_numbers_without_currying(1, 2, 3)" then it returns "6"

# # # with Currying

def add_numbers_with_currying(number1):
    def add_numbers_with_currying(number2):
        def add_numbers_with_currying(number3):
            return number1 + number2 + number3
        return add_numbers_with_currying
    return add_numbers_with_currying

# # # # we call it like this "add_numbers_with_currying(1)(2)(3)" then it returns "6"
