# ITERATOR
print('=====ITERATOR=====')

def square(nums):
    for num in nums:
        yield (num * num)

num = [1, 2, 3, 4, 5].__iter__()
print(square(num))
print(next(square(num)))
print(next(square(num)))
print(next(square(num)))
print(next(square(num)))
print(next(square(num)))
# print(next(square(num))) #ERROR


# GENERATOR
print('=====GENERATOR======')

def grade_gen():
    yield 'A'
    yield 'B'
    yield 'C'
    yield 'D'
    yield 'E'
for grade in grade_gen():
    print(grade)

my_num = (i for i in range(3))
for num in my_num:
    print(num)

def say_hello(name):
    return f"Hello {name}"

def greet_bob(greeter_func):
    return greeter_func('Me')

print(greet_bob(say_hello))


# DECORATOR
print('=====DECORATOR======')

def my_dec(funct):
    def wrap():
        print('Before')
        funct()
        print('After')
    return wrap

@my_dec
def say_bye():
    print('Bye..')

say_bye()