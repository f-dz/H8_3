# CONDITIONAL
x = 0
y = 5

if x < y:                            # Truthy
    print('yes')

if y < x:                            # Falsy
    print('yes')

if x:                                # Falsy
    print('yes')

if y:                                # Truthy
    print('yes')

if 'aul' in 'grault':                # Truthy
    print('yes')

if 'quux' in ['foo', 'bar', 'baz']:  # Falsy
    print('yes')

# Grouping Statements: Indentation and Blocks
if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
    
print('After conditional')

if 'foo' in ['foo', 'bar', 'baz']:        #  x
    print('Outer condition is true')      #  x
    if 10 > 20:                           #  x
        print('Inner condition 1')        #        x
    print('Between inner conditions')     #  x
    if 10 < 20:                           #  x
        print('Inner condition 2')        #  x
    print('End of outer condition')       #  x
print('After outer condition')            #  x

x = 20
if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')

x = 120
if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')

hargaBuku = 20000
hargaMajalah = 5000
uang = 2000
if uang > hargaBuku:
    print("beli buku")
else:
    print("uang tidak cukup")

hargaBuku = 20000
hargaMajalah = 5000
uang = 2000
if uang > hargaBuku:
    print("beli buku")
elif uang > hargaMajalah:
    print("beli majalah")
else:
    print("uang tidak cukup")

name = 'Hacktiv8'
if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Hacktiv8':
    print('Hello Hacktiv8')
elif name == 'Arnold':
    print('Hello Arnold')
else:
    print("I don't know who you are!")

if 'a' in 'bar':
    print('foo')
elif 1/0:
    print("This won't happen")
elif var:
    print("This won't either")

# One-Line if Statements
if 'f' in 'foo': print('1'); print('2'); print('3')
if 'z' in 'foo': print('1'); print('2'); print('3')

x = 2
if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')

x = 3
if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')

x = 3
if x == 1:
    print('foo')
    print('bar')
    print('baz')
elif x == 2:
    print('qux')
    print('quux')
else:
    print('corge')
    print('grault')

# Conditional Expressions (Python’s Ternary Operator)
raining = False
print("Let's go to the", 'beach' if not raining else 'library')

raining = True
print("Let's go to the", 'beach' if not raining else 'library')

age = 12
s = 'teen' if age < 21 else 'adult'
s

'yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no'

a = 10
b = 5
if a > b:
    m = a
else:
    m = b


# The Python pass Statement
# if True:
# print('foo')

if True:
    pass
print('foo')


# LOOPING
# Python "while" Loops
n = 5
while n > 0:
    n -= 1
    print(n)

i = 1
while i < 6:
  print(i)
  i += 1

# The Python break and continue Statements

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break # Break Statement
    print(n)
print('Loop ended.')

n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')

# The else Clause
n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('Loop done.')

n = 5
while n > 0:
    n -= 1
    print(n)
    if n == 2:
        break
else:
    print('Loop done.')

# Infinite Loops
# while True:
#     print('foo')

# Nested while Loops
age = 22
gender = 'F'
if age < 18:
    if gender == 'M':
        print('son')
    else:
        print('daughter')
elif age >= 18 and age < 65:
    if gender == 'M':
        print('father')
    else:
        print('mother')
else:
    if gender == 'M':
        print('grandfather')
    else:
        print('grandmother')

a = ['foo', 'bar']
while len(a):
    print(a.pop(0))
    b = ['baz', 'qux']
    while len(b):
        print('>', b.pop(0))

# One-Line while Loops
n = 5
while n > 0: n -= 1; print(n)

a = ['foo', 'bar', 'baz']
for i in a:
    print(i)

d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(k)

for k in d:
    print(d[k])

for k in d.values():
    print(k)

for k, v in d.items(): 
    print(k, ":", v)

# Iterating Through a Dictionary
d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(k)

for k in d:
    print(d[k])

for v in d.values():
    print(v)

# The range() Function
for n in (0, 1, 2, 3, 4):
    print(n)

# Altering for Loop Behavior
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        break
    print(i)

for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        continue
    print(i)

for i in ['foo', 'bar', 'baz', 'qux']:
    print(i)
else:
    print('Done.')  # Will execute

for i in ['foo', 'bar', 'baz', 'qux']:
  if i == 'bar':
    break
  print(i)
else:
  print('Done.')