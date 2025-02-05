#EX1
def Recipe():
    grams = int(input("Write grams:"))
    ounces = 28.3495231 * grams
    print(grams, "grams =", ounces, "ounces")
Recipe()

#EX2
def Fahrenheit():
    F = int(input("Fahrenheit temperature:"))
    C = (5/9) * (F -32)
    print(F, "farenheit", C, "celsius")
Fahrenheit()

#EX3
def solve():
    numheads = int(input("Input number of heads:"))
    numlegs = int(input("Input number of legs:"))
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens 
        if(chickens * 2 + rabbits * 4) == numlegs:
            print("Chickens:", chickens, "Rabbits:", rabbits)
            return
    print("No solution")
solve()

#EX4
def prime(i):
    for x in range(2, i):
        if i == 1:
            return False
        if i % x == 0:
            return False
    return True

list = [1, 3, 4, 5, 8, 12, 11]
def filter_prime(some_list):
    arr=[]
    for i in some_list:
        if prime(i) == True:
            arr.append(i)
    return arr
list1 = filter_prime(list)

#EX5
import itertools
def permutations():
    str = input("Write a string:")
    p = [''.join(perm) for perm in itertools.permutations(str)]
    print(p)
permutations()

#EX6
def reverse_sentence():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    words.reverse()
    print(" ".join(words))

reverse_sentence()

#EX7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
nums = list(map(int, input("Input numbers: ").split()))
print(has_33(nums))

#EX8
def spy_game(nums):
    pattern = [0, 0, 7]
    index = 0
    for num in nums:
        if num == pattern[index]:
            index += 1
        if index == len(pattern):
            return True
    return False
nums = list(map(int, input("Input numbers: ").split()))
print(spy_game(nums))

#EX9
import math
def sphere_volume():
    radius = float(input("Input number: "))
    volume = (4/3) * 3.14 * radius ** 3
    print(volume)
sphere_volume()

#EX10
def unique_elements(lst):
    result = []
    for num in lst:
        if num not in result:
            result.append(num)
    return result

numbers = list(map(int, input("Enter numbers: ").split()))
print(unique_elements(numbers))

#EX11
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
word = input("Enter word or sentence:")
print(is_palindrome(word))

#EX12
def histogram(lst):
    for num in lst:
        print("*" * num)
nums = list(map(int, input("Inuput numbers separated by spaces:").split()))
histogram(nums)

#EX13
import random
def guess_number():
    name = input("Hello! What is your name?\n")
    number = random.randint(1, 20)
    print(f"\nWell, {name}, I am thinking of a number between 1 an 20.")
    attempts = 0
    while True:
        guess = int(input("\nTake a guess\n"))
        attempts += 1
        if guess < number:
            print("\nYour guess is too low.")
        elif guess > number:
            print("\nYour guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses")
            break
guess_number()

#EX14
from function import has_33

nums = list(map(int, input("Input numbers: ").split()))
print(has_33(nums))