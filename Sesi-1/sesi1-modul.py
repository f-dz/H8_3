# Integer
print(123123123123123123123123123123123123123123123123 + 1)
print(10)
print(type(10))

# Floating-Point Numbers
print(4.2)
print(type(4.2))
print(4.)
print(.2)
print(.4e7)
print(4.2e-4)

# Strings
print("Hacktiv8")
print(type("Hacktiv8"))
print('')
print("This string contains a single quote (') character.")
print('This string contains a double quote (") character.')

# Boolean Type, Boolean Context, and “Truthiness”
print(type(True))
print(type(False))

# Variable Assignment
n = 300
print(n)
n
n = 1000
print(n)
n
a = b = c = 300
print(a, b, c)

# Variable Types in Python
var = 23.5
print(var)
var = "Now I'm a string"
print(var)

# Variable Names
name = "Hacktiv8"
Age = 54
has_laptops = True
print(name, Age, has_laptops)
# 9_kepala_naga = True
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8
print(age, Age, aGe, AGE, a_g_e, _age, age_, _AGE_)

a = 10
b = 20
a + b
a = 10
b = 20
a + b - 5

# Aritmetic Operators
a = 4
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
10 / 5

# Comparison Operators
a = 10
b = 20
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)
a = 30
b = 30
print(a == b)
print(a <= b)
print(a >= b)

# String Manipulation
# + Operators
s = 'foo'
t = 'bar'
u = 'baz'
print(s + t)
print(s + t + u)
print('Hacktiv8 ' + 'Inalum')
# * Operators
s = 'foo.'
s * 4
# in Operators
s = 'foo'
print(s in 'That food for us')
print(s in 'That good for us')

# Case Conversion
s = 'HackTIV8'
# Capitalize
print(s.capitalize())
# Lower
print(s.lower())
# Swapcase
print(s.swapcase())
# Title
print(s.title())
# Uppercase
print(s.upper())

# Python Lists
a = ['foo', 'bar', 'baz', 'qux']
print(a)

# Lists Are Ordered
a = ['foo', 'bar', 'baz', 'qux']
b = ['baz', 'qux', 'bar', 'foo']
a == b
# Lists Can Contain Arbitrary Objects
a = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]
print(a)
# List Elements Can Be Accessed by Index
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[0])
print(a[5])
print(a[-1])
print(a[-6])
# Slicing
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a[2:5]
# The concatenation (+) and replication (*) operators:
print(a)
print(a + ['grault', 'garply'])
print(a * 2)
# len(), min(), max()
print(a)
print(len(a))
print(min(a))
print(max(a))

# Modifying a Single List Value
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a)
a[2] = 10
a[-1] = 20
print(a)
del a[3]
print(a)

# Modifying Multiple List Values
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[1:4])
a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]
print(a)

# Python Tuples
# Defining and Using Tuples
t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
print(t)
print(t[0])
print(t[-1])
# packing and unpacking
(s1, s2, s3, s4) = ('foo', 'bar', 'baz', 'qux')
s1

# Python Dictionary
# Defining a Dictionary
MLB_team = {
    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle': 'Mariners'
}
# Accessing Dictionary Values
print(MLB_team['Minnesota'])
print(MLB_team['Colorado'])
# error
# MLB_team['Toronto']
#Adding an entry 
MLB_team['Kansas City'] = 'Royals'
MLB_team
# Update an entry
MLB_team['Seattle'] = 'Seahawks'
MLB_team
# Delete an entry
del MLB_team['Seattle']
MLB_team

# Building a Dictionary Incrementally
person = {}
type(person)
person['fname'] = 'Hack'
person['lname'] = 'Inalum'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}

person

print(person['fname'])
print(person['lname'])

print(person['children'])
print(person['children'][1])

print(person['pets'])
print(person['pets']['cat'])

# Built-in Methods
d = {'a': 10, 'b': 20, 'c': 30}
# items
print(d.items())
# keys
print(d.keys())
# values
print(d.values())

# Python Statements
print('Hello, World!')

x = [1, 2, 3]
print(x)

# Line Continuation
person1_age = 42
person2_age = 16
person3_age = 71

someone_is_of_working_age = (person1_age >= 18 and person1_age <= 65) or (person2_age >= 18 and person2_age <= 65) or (person3_age >= 18 and person3_age <= 65)
someone_is_of_working_age

someone_is_of_working_age = (
    (person1_age >= 18 and person1_age <= 65)
    or (person2_age >= 18 and person2_age <= 65)
    or (person3_age >= 18 and person3_age <= 65)
)

someone_is_of_working_age