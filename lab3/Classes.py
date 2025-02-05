#EX1
class String():
    def __init__(self):
        self.text = ""
    
    def getString(self):
        self.text = input("Write a string:")

    def printString(self):
        print(self.text.upper())

s = String()
s.getString()
s.printString()

#EX2
class Shape():
    def area(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

length = int(input("lendth: "))
sqr = Square(length)
print(sqr.area())

#EX3

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width  
length = int(input("length: "))
width = int(input("width: "))
rect = Rectangle(length, width)
print(rect.area())          

#EX4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, another):
        return math.sqrt((self.x - another.x) ** 2 + (self.y - another.y) ** 2)

x1, y1 = map(int, input("Input first values:").split())
x2, y2 = map(int, input("Input second values:").split())
p1 = Point(x1, y1)
p2 = Point(x2, y2)
p1.show()
p2.show()
print(p1.dist(p2))

#EX5
class Account:
  def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance
  def info(self):
    print(self.owner)
    print(self.balance)
  def deposit(self, amount):
    self.balance += amount
  def withdraw(self, amount):
    if self.balance - amount < 0:
      print('no enough money to withdraw')
    else:
      self.balance -= amount
rob = Account('Rob', 25000)
rob.info()
rob.withdraw(26000)
rob.deposit(1000)
rob.withdraw(26000)
rob.info()

#EX6
numbers = list(map(int, input("Enter numbers:").split()))

is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, x))

prime_numbers = list(filter(is_prime, numbers))

print("Prime numbers:", prime_numbers)