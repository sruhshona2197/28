

# 60. Callable Object
class Multiply:
    def __call__(self, a, b):
        return a * b

m = Multiply()
print(m(5, 6))


# 61. Custom Exception
class AgeError(Exception):
    pass

class Person:
    def __init__(self, age):
        if age < 18:
            raise AgeError("Too young")
        self.age = age

try:
    p = Person(15)
except AgeError as e:
    print(e)


# 62. Encapsulation
class Account:
    def __init__(self):
        self.__money = 1000

    def get_money(self):
        return self.__money

a = Account()
print(a.get_money())


# 63. Method Chaining
class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, x):
        self.value += x
        return self

    def sub(self, x):
        self.value -= x
        return self

c = Calculator()
print(c.add(10).sub(3).value)
