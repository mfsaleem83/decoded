# Challange 1.1
print("hello world")
a = 1
b = 2

print(a+b)
print

# challenge 1.2


def add(x, y):
    return x+y


result = add(3, 5)
print(f"{result}")


def add(x, y):
    return x + y


def sum_and_diff(x, y):
    return x + y, x - y


result = add(5, 3)
print("Result is", result)

s, d = sum_and_diff(5, 3)
result = sum_and_diff(5, 3)
print("Sum and diff", s, d)

sum = result[0]
diff = result[1]
print(f"sum={sum} diff={diff}")

# challenge 1.3

a = 1
b = 1.11
c = True
d = "Test String"
e = (1, 2)
f = [1, 3]
g = {"a", "b", "c"}
h = {"key1": "value1", "key2": "value2"}

print(f"a= {type(a)}")
print(f"b= {type(b)}")
print(f"c= {type(c)}")
print(f"d= {type(d)}")
print(f"e= {type(e)}")
print(f"f= {type(f)}")
print(f"g= {type(g)}")
print(f"h= {type(h)}")

if not c:
    c = False
print(c)
