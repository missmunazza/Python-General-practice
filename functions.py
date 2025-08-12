def add_func(): 
    a = 5
    b = 10
    c = a + b 
    return c
result = add_func()
print("The result of the addition is:", result)


#dynamically took values
def add_func(a, b): 
    c = a + b 
    return c
a = 10
b = 25
result = add_func(a, b)
print( result)


def add_func(a, b): 
    c = a + b
    print("return value")
    return c
a = 100
b = 250000
result = add_func(a, b)
print( result)


def add_func(a, b): 
    c = a + b
    print("return value")
    return c
x = 100
z = 250000
result = add_func(x, z)
print( result)


def add_func(a, b, c): 
    c = a + b + c
    print("return value")
    return c
x = 100
j = 100
z = 250000
result = add_func(x, z, j)
print( result)


def profile(name, age, city, email, number):
    print(f"name: (name)")
    print(f"age: (age)")
    print(f"city: (city)")
    print(f"email: (email)")
    print(f"number: (number)")
    return name, age, city, email, number

name =  'john',
age = 30,
city = 'new York',
email = 'ali@gmail.com',
number = 123456789

result = profile(name, age, city, email, number)
print(result)



#make a function in which we can add, mult, sub, div any value
def func(a, b): 
    add = a + b 
    sub = a - b 
    mult = a * b 
    div = a / b

    return add, sub, mult, div
a = 10
b = 25
result = func(a, b)
print( result)


def profile(dict1):
    print(f"name: (name)")
    print(f"age: (age)")
    print(f"city: (city)")
    print(f"email: (email)")
    print(f"number: (number)")
    return name, age, city, email, number

dict1 = {
    'name':  'john',
    'age': 30,
    'city':'new York',
    'email': 'ali@gmail.com',
    'number': 123456789
}

result = profile(dict1)
print(result)


def profile(dicr):
    name = dicr.get('name')
    age = dicr.get('age')
    city = dicr.get('city')
    email = dicr.get('email')
    number = dicr.get('number')
    return name, age

dict1 = {
    'name':  'john',
    'age': 30,
    'city':'new York',
    'email': 'ali@gmail.com',
    'number': 123456789
}

result = profile(dict1)
print(result)