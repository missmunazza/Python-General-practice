a = 5
b = 5
if a == b:
    print("a is equal to b")

a = 5
b = 10
if a == b:
    print("a is equal to b")
    print( a == b)
elif a < b:
    print("a is less than b")
    print( a < b)
    print( a == b)
else:
    print("a is not equal to b")

a = 5
b = 10
if a == b:
    print("a is equal to b")
    print( a == b)
elif a > b:
    print("a is less than b")
    print( a < b)
    print( a == b)
else:
    print("a is not equal to b")
    print( a > b)
    print( a == b)


a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 335
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 5
b = 10
c = 15
if a and b:
    print("Both a and b are non-zero")

#not
a = 5
b = 10
c = None
if a and b and c:
    print("Both a and b are non-zero")
else:
    print("At least one of a or b is zero")

#or
a = 5
b = 10
c = None
if a or b or c:
    print("Both a and b are non-zero")
else:
    print("At least one of a or b is zero")


list1 = [5, 10, 15, 20, 25]
if 5 in list1:
    print("5 is in the list")
else:
    print("5 is not in the list")

list1 = [5, 10, 15, 20, 25]
if 55 in list1:
    print("5 is in the list")
else:
    print("5 is not in the list")

#not
a = 5
b = 10
c = None
if not a and not b:
    print("Both a and b are non-zero")
else:
    print("At least one of a or b is zero")

#nested if
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  elif x == 30:
    print("x is also above 30")
  else:
    print("but not above 20.")


x = 41
if x < 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  elif x == 30:
    print("x is also above 30")
  else:
    print("but not above 20.")


x = 5
if x > 20:
    print("and also above 20!")
elif x == 30:
    print("x is also above 30")
else:
    print("but not above 20.")


if x == 20:
    print("and also above 20!")
elif x == 30:
    print("x is also above 30")
else:
    print("but not above 20.")