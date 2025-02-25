#1
import re
txt = input("Enter a word: ")
a = r"ab*.*"
if re.fullmatch(a, txt):
    print("Mathces")
else:
    print("Does not match")

#2
import re
txt = input("Enter a word: ")
a = r"ab{2,3}"
if re.fullmatch(a, txt):
    print("Matches")
else:
    print("Does not match!")

#3
import re
def sequence(txt):
    a = r'\b[a-z]+_[a-z]+\b'
    match = re.findall(a, txt)
    return match
txt = input("Enter a sentence: ")
matches = sequence(txt)
if matches:
    print(f"Found matches: {matches}")
else:
    print("Does not match")

#4
import re
def find(text):
    a = r'\b[a-z]+_[a-z]+\b'
    res = re.findall(a, text)
    return res
b = input("Enter a sentence: ")
sequences = find(b)
if sequences:
    print("Found sequences:", sequences)
else:
    print("Does not match")

#5
import re
a = r"a.*b"
text = input("Enter a word: ")
if re.fullmatch(a, text):
    print("Matches")
else:
    print("Does not match!")

#6
import re
text = input("Enter a string: ")
res = re.sub(r"[ ,.]", ":", text)
print(res)

#7
import re
def snake_to_camel(snake):
    return re.sub(r'_([a-z])', lambda match:match.group(1).upper(), snake)
text = input("Enter a snake case string: ")
camel = snake_to_camel(text)
print("Camel case string:", camel)

#8
import re
text = input("Enter a string: ")
split = re.findall(r'[A-Z][a-z]*', text)
print(split)

#9
import re
text = input("Enter a string: ")
res = re.sub(r'(?<!^)([A-Z])', r' \1', text)
print(res)

#10
import re
text = input("Enter a camel case string: ")
snake = re.sub(r'([A-Z])', r'_\1', text).lower()
print(snake)
if snake.startswith('_'):
    snake = snake[1:]
print(snake)