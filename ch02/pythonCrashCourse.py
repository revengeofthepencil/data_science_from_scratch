import re
from collections import defaultdict
from collections import Counter
import random
import time

#regex
my_regex = re.compile("[0-9]+", re.I)

testStrings = ['8970780',
'hello 123 and #2',
'what??'
]

for testString in testStrings:
	print(testString)
	regexMatch = my_regex.findall(testString)
	print(regexMatch)

print('\n')

# lambda default dict
# Defining the dict
d = defaultdict(lambda:'Not here')
d["a"] = 1
d["b"] = 2
  
print(d["a"])
print(d["b"])
print(d["c"])

print('\n')


#strings

name1 = 'Johnny'
name2 = 'Cash'

full_name = f"{name1} {name2}"
print(f"first name = '{name1}', last name = '{name2}', full name = '{full_name}'")

print('\n')

#exceptions

try:
    print(0 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")

print('\n')

# list stuff!
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f'original list = {x}')

every_third = x[::3]                 # [-1, 3, 6, 9]
print(f'every third = {every_third}')

five_to_three = x[5:2:-1]            # [5, 4, 3]
print(f'five_to_three reversed = {five_to_three}')

has_666 = 666 in x
has_2 = 2 in x

print(f'has_2 = {has_2}, has_666 = {has_666}')

two_items = [1, 2]
firstOne, secondOne = two_items
print(f'first one = {firstOne}, second one = {secondOne}')

_, just_second = two_items
print(f'just second = {just_second}')

print('\n')

# Tuples
def sum_and_product(x, y):
    return (x + y), (x * y)

args_for_sp = 2,3
sp = sum_and_product(args_for_sp[0], args_for_sp[1])
s, p = sum_and_product(args_for_sp[0], args_for_sp[1]) 

print(f'args_for_sp = {args_for_sp} s = {s}, p = {p}, sp = {sp}')

print('\n')

# dictionaries
empty_dict = {}
grades = {"Joel": 80, "Tim": 95}
print(f'empty_dict = {empty_dict}, grades = {grades}')

joel_has_grade = "Joel" in grades     # True
kate_has_grade = "Kate" in grades     # False
print(f'joel_has_grade = {joel_has_grade}, kate_has_grade = {kate_has_grade}')

grades_keys   = grades.keys()     # iterable for the keys
grades_values = grades.values()   # iterable for the values

print(f'grade keys = {grades_keys}, grade vals = {grades_values}')

for k, v in grades.items():
	print(f'got k = {k}, v = {v}')


print('\n')

# counter
# 
# This is pretty neat. From the text:
# A Counter turns a sequence of values into a defaultdict(int)-like object
# mapping keys to counts

test_list = [0, 1, 2, 4,9, 9, 9, 0, 9]
c = Counter(test_list)          # c is (basically) {0: 2, 1: 1, 2: 1}
print(f'test_list = {test_list}, resulting count = {c}')

common_stuff = c.most_common(2)
print(f'2 most common = {common_stuff}')

print('\n')

# flow control with range!

for x in range(10):
    if x == 3:
        continue  # go immediately to the next iteration
    if x == 5:
        break     # quit the loop entirely
    print(x)

print('\n')

# sorting. Check the "sorted" function to return a copy. I had forgotten all about that

x = [4, 1, 2, 3]
print(f'original x = {x}')
y = sorted(x)     # y is [1, 2, 3, 4], x is unchanged
print(f'original y = {y}')
print(f'x after sorted = {x}')
x.sort()          # now x is [1, 2, 3, 4]
print(f'x after sort = {x}')

# sort the list by absolute value from largest to smallest
x = sorted([-4, 1, -2, 3], key=abs, reverse=True)  # is [-4, 3, -2, 1]
print(f'sort reverse with abs = {x}')

print('\n')

# list comprehensions

even_numbers = [x for x in range(5) if x % 2 == 0]  # [0, 2, 4]
print(f'even nums in range 5 = {even_numbers}')
squares      = [x * x for x in range(5)]            # [0, 1, 4, 9, 16]
print(f'squares in range 5 = {squares}')
even_squares = [x * x for x in even_numbers]        # [0, 4, 16]
print(f'even_squares = {even_squares}')

# turn into dict or set
square_dict = {x: x * x for x in [3,4,18,1,0,.2311]}  
print(f'square_dict = {square_dict}')
square_set  = {x * x for x in [1, -1]}    
print(f'square_dict = {square_set}')

print('\n')

# generators

def generate_range(n):
    print(f'in generate_range with {n}')
    i = 0
    while i < n:
        yield i   # every call to yield produces a value of the generator
        i += 1

for i in generate_range(10):
    print(f"i: {i}")

print('\n')

# enumerate gives the index
names = ["Alice", "Bob", "Charlie", "Debbie"]
for i, name in enumerate(names):
    print(f"name {i} is {name}")

print('\n')

# Randomness
random.seed(10)  # this ensures we get the same results every time
four_uniform_randoms = [random.random() for _ in range(4)]
print(four_uniform_randoms)

rand_range_10 = random.randrange(10)    # choose randomly from range(10) = [0, 1, ..., 9]
rand_range_3_6 = random.randrange(3, 6)  # choose randomly from range(3, 6) = [3, 4, 5]
print(f'rand_range_10 = {rand_range_10}, rand_range_3_6 = {rand_range_3_6}')

now = time.time()
random.seed(now)  # this should vary from one run to the next

rand_range_10 = random.randrange(10)    # choose randomly from range(10) = [0, 1, ..., 9]
rand_range_3_6 = random.randrange(3, 6)  # choose randomly from range(3, 6) = [3, 4, 5]
print(f'seeing with time, rand_range_10 = {rand_range_10}, rand_range_3_6 = {rand_range_3_6}')

up_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(up_to_ten)
print(f'shuffled up to ten = {up_to_ten}')

my_best_friend = random.choice(["Alice", "Bob", "Charlie"])
print(f'random.choice = {my_best_friend}')

lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6) 
print(f'sample with no duplicates = {winning_numbers}')

four_with_replacement = [random.choice(range(10)) for _ in range(4)]
print(f'four_with_replacement. maybe duplciates? {four_with_replacement}')

print('\n')

# regex


re_examples = [                        # All of these are True, because
    not re.match("a", "cat"),              #  'cat' doesn't start with 'a'
    re.search("a", "cat"),                 #  'cat' has an 'a' in it
    not re.search("c", "dog"),             #  'dog' doesn't have a 'c' in it.
    3 == len(re.split("[ab]", "carbs")),   #  Split on a or b to ['c','r','s'].
    "R-D-" == re.sub("[0-9]", "-", "R2D2") #  Replace digits with dashes.
    ]

assert all(re_examples), "all the regex examples should be True"

"""
One important thing to note is that re.match checks whether the beginning
of a string matches a regular expression, while re.search checks whether 
any part of a string matches a regular expression. At some point you will 
mix these two up and it will cause you grief.
"""

print('n')
