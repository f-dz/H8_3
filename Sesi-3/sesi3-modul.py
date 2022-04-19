# FUNCTION
# Function Creation
def my_function(p, l):
    '''Function to calculate area of a square'''
    print(p * l)

def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)

# Calling a Function
def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)
printme("I'm first call to user defined function!")
printme("Again second call to the same function")

# Pass by reference vs value
def changeme( mylist ):
   '''This changes a passed list into this function'''
   mylist = mylist+[1,2,3,4]
   print("\nValues inside the function : ", mylist)
   return mylist
mylist = [10,20,30]
print("\nValues outside the function - before : ", mylist)
mylist = changeme( mylist )
print("\nValues outside the function - after  : ", mylist)

def changeme( mylist ):
   '''This changes a passed list into this function'''
   mylist = [1, 2, 3, 4] # This would assign new reference in mylist
   print("Values inside the function  : ", mylist)
mylist = [10, 20, 30]
changeme( mylist )
print("Values outside the function : ", mylist)

# Function Arguments
# **Required arguments**
def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)
printme("Hello")

def calculate_rect(length, width):
  '''This function is used to calculate area of rectangle'''
  print('Area : ', length*width)

length = 100
width = 20
calculate_rect(length, width)

# **Keyword Arguments**
def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)
printme(str_input = "Hacktiv8")

def printinfo( name, age ):
   '''This prints a passed info into this function'''
   print("Name : ", name)
   print("Age. : ", age)
printinfo( age=4, name="a" )

def printinfo( name, age = 26 ):
   '''This prints a passed info into this function'''
   print("Name : ", name)
   print("Age  : ", age)
   print("")
printinfo( age=50, name="hacktiv8" )
printinfo( name="hacktiv" )

def printinfo( name, age = 26 ):
   '''This prints a passed info into this function'''
   print("Name : ", name)
   print("Age  : ", age)
   print("")
printinfo( age=50, name="hacktiv8" )

# **Variable-length Arguments**
def functionname(args, *var_args_tuple ):
   '''function_docstring'''
   function_suite
   return [expression]

def printinfo( arg1, *vartuple ):
# def printinfo(arg1, arg2, arg3, arg4):
   '''This prints a variable passed arguments'''
   print('arg1     : ', arg1)
   print('vartuple : ', vartuple)
   print('')
   for var in vartuple:
      print('isi vartuple : ', var) 
printinfo( 10 )
printinfo( 70, 60, 50, "a" )

def functionname(args, *var_args_tuple ):
   '''function_docstring'''
   function_suite
   return [expression]

def functionname(args, **var_args_dict ):
   '''function_docstring'''
   function_suite
   return [expression]

# Create a function with nonkeyword variables
def person_car(total_data, **kwargs):
  '''Create a function to print who owns what car'''
  print('Total Data : ', total_data)
  for key, value in kwargs.items():
    print('Person : ', key)
    print('Car    : ', value)
    print('')
person_car(3, jimmy='chevrolet', frank='ford', tina='honda')
person_car(3)

# The Anonymous Functions
sum = lambda arg1, arg2: arg1 + arg2
print("Value of total : ", sum( 10, 20 ))
print("Value of total : ", sum( 20, 20 ))

# The `return` Statement
def sum(arg1, arg2):
    # Add both the parameters and return them."
    total = arg1 + arg2
    return total
total = sum(10, 20)
print("Result function : ", total)

# Scope of Variables
# Declare a global variable
total = 0
def sum( arg1, arg2 ):
   total = arg1 + arg2; 
   print("Inside the function local total   : ", total)
sum( 10, 20 )
print("Outside the function global total : ", total)

# Declare a global variable
total = 0
def sum( arg1, arg2 ):
   total = arg1 + arg2; 
   print("Inside the function local total   : ", total)
   return total
print("Outside the function global total - before : ", total)
total = sum( 10, 20 )
print("Outside the function global total - after  : ", total)

# Docstring
def sum_number(num1, num2):
  '''
  This function is used to sum of 2 variables.
  :param num1: Input number 1 | int or float
  :param num2: Input number 2 | int or float
  
  :return: num3: Sum of number | int or float
  '''
  num3 = num1 + num2
  return num3
print(sum_number.__doc__)


# MODULE
import sys
print(sys.path)
