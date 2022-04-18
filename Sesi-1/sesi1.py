# TIPE DATA
print('=====TIPE DATA=====')

# Integer
print(123456789, type(123456789))

# Float
print(2.3, type(2.3))
print(.4e7, type(.4e7))
print(4.2e-4, type(4.2e-4))

# String
print('Saya', type('Saya'))
print("Sa'ya", type("Sa'ya"))

# Boolean
print(True, type(True))
print(10 > 20, type(10 > 20))


# VARIABLE
print('=====VARIABLE=====')

# Assignment & Chained Assignment
a = 100
b = c = 200
print(a, b, c+a)

# Variable Type
var = 10
print(var)
var = 'Hello'
print(var)


# OPERATOR
print('=====OPERATOR=====')

# Arithmatic
print('a * b =', a * b)
print('a / b =', b / a)
print('a // b =', b // a)
print('a ** 2 =', a ** 2)

# Comparison
print('b == c', b == c)
print('a >= b', a >= b)


# STRING MANIPULATION
print('=====STRING MANIPULATION=====')

# Concatenation
s = 'foo'
t = 'bar'
print('s :', s)
print('t :', t)
print('s + t :', s + t)
print('s * 4 :', s * 4)

# Case Conversion
case = 'SaYa dAn kamU'
print('Capital\t:', case.capitalize())
print('Lower\t:', case.lower())
print('Upper\t:', case.upper())
print('Swap\t:', case.swapcase())
print('Title\t:', case.title())


# LIST
print('=====LIST=====')
list1 = ['Saya', 'Kamu', 'Dia']
list2 = ['SAYA', 'KAMU', 'DIA']
list3 = ['Kamu', 'Dia', 'Saya']
print(list1, type(list1))
print(list2, type(list2))
print(list3, type(list3))

# List Comparasion
print('list1 == list2 :', list1 == list2)
print('list1 == list3 :', list1 == list3)
print('list2 == list3 :', list2 == list3)

# Print List
print('list1[0]\t:', list1[0])
print('list1[-1]\t:', list1[-1])

# Slicing
print('list[1:2]\t:', list1[1:2])
print('list[1:3]\t:', list1[1:3])

# Modifying List Value
print('modif 1 :', list1 + ['Mereka'])
print('modif 2 :', list1 + ['Kita', 'Kami'])
list1[-1] = 'Kalian'
print('modif 3 :', list1)

# Delete
del list1[-1]
print('modif 4 :', list1)


# TUPLES
print('=====TUPLES=====')

# Create
tuple1 = ('Me', 'You', 'Us')
print(tuple1, type(tuple1))
print('tuple1[0] :', tuple1[0])

# Packing Unpacking
(t1, t2, t3) = ('Me', 'You', 'Us')
print('t1\t:', t1)
print('t2\t:', t2)
print('t3\t:', t3)


# DICTIONARY
print('=====DICTIONARY=====')

# Create
dict1 = {
    'Roses': 'Red',
    'Violets': 'Blue' 
}
print(dict1, type(dict1))

# Access Value
print('Roses are', dict1['Roses'])
print('Violets are', dict1['Violets'])

# Add Entry
dict1['Jasmine'] = 'Tea'
print(dict1)

# Update Entry
dict1['Jasmine'] = 'White'
print(dict1)

# Delete Entry
del dict1['Jasmine']

# Built-in methods
print('items()\t:', dict1.items())
print('keys()\t:', dict1.keys())
print('values():', dict1.values())