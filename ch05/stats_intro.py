from collections import Counter
import matplotlib.pyplot as plt
import random 
from typing import List
import math
import sys
import os
from pathlib import Path
current_path = os.path.dirname(os.path.abspath(__file__))
parent_dir = Path(current_path).parent
# adding ch04 to the system path
sys.path.append(os.path.join(parent_dir, "ch04"))
from linear_algebra import sum_of_squares


num_friends = []

# most people fall between 1-15 friends
for i in range(150):
    num_friends.append(random.randint(1, 15))

for i in range(54):
    num_friends.append(random.randint(1, 100))


num_points = len(num_friends)
largest_value = max(num_friends)            # 100
smallest_value = min(num_friends)           # 1

print(f'num_points = {num_points}, largest_value = {largest_value}, smallest_value = {smallest_value} ')

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]           # 1
second_smallest_value = sorted_values[1]    # 1
second_largest_value = sorted_values[-2]    # 49

print(f'smallest_value = {smallest_value}, second_smallest_value = {second_smallest_value}, second_largest_value = {second_largest_value} ')


def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)

friend_mean = mean(num_friends)   # 7.333333
print(f'friend_mean = {friend_mean}')

# The underscores indicate that these are "private" functions, as they're
# intended to be called by our median function but not by other people
# using our statistics library.
def _median_odd(xs: List[float]) -> float:
    """If len(xs) is odd, the median is the middle element"""
    return sorted(xs)[len(xs) // 2]

def _median_even(xs: List[float]) -> float:
    """If len(xs) is even, it's the average of the middle two elements"""
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2  # e.g. length 4 => hi_midpoint 2
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2

def median(v: List[float]) -> float:
    """Finds the 'middle-most' value of v"""
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)

assert median([1, 10, 2, 9, 5]) == 5
assert median([1, 9, 2, 10]) == (2 + 9) / 2
print(f'median num_friends = {median(num_friends)}')

"""
quantile, which represents the value under which a certain percentile
of the data lies
"""
def quantile(xs: List[float], p: float) -> float:
    """Returns the pth-percentile value in x"""
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]

quantiles = [quantile(num_friends, p) for p in [0.10, 0.25, 0.75, 0.90]]
print(f'quantiles = {quantiles}')

"""
mode is the most commonly occurring value
"""
def mode(x: List[float]) -> List[float]:
    """Returns a list, since there might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
            if count == max_count]

print(f'mode(num_friends) = {mode(num_friends)}')


def de_mean(xs: List[float]) -> List[float]:
    """Translate xs by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(xs)
    return [x - x_bar for x in xs]

def variance(xs: List[float]) -> float:
    """Almost the average squared deviation from the mean"""
    assert len(xs) >= 2, "variance requires at least two elements"

    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n - 1)

def my_own_variance(xs: List[float]) -> float:
    """Almost the average squared deviation from the mean"""
    assert len(xs) >= 2, "variance requires at least two elements"
    mean_xs = mean(xs)
    sum_of_squares = 0
    length_xs = len(xs)
    for x in xs:
        sum_of_squares += (x - mean_xs) ** 2

    print(f'mean_xs = {mean_xs}, sum_of_squares = {sum_of_squares}')
    return sum_of_squares / (length_xs - 1)


""" get the variance 
yep, I wrote my own just to make sure I understand 
"""
variance_friends = variance(num_friends)
variance_friends_mine = my_own_variance(num_friends)
print(f'variance_friends = {variance_friends}, variance_friends_mine = {variance_friends_mine}')


def standard_deviation(xs: List[float]) -> float:
    """The standard deviation is the square root of the variance"""
    return math.sqrt(variance(xs))

standard_deviation_friends = standard_deviation(num_friends)
print(f'standard_deviation_friends = {standard_deviation_friends}')

"""
A more robust alternative computes the difference between the
75th percentile value and the 25th percentile value:
"""
def interquartile_range(xs: List[float]) -> float:
    """Returns the difference between the 75%-ile and the 25%-ile"""
    return quantile(xs, 0.75) - quantile(xs, 0.25)


interquartile_range_friends = interquartile_range(num_friends)
print(f'interquartile_range_friends = {interquartile_range_friends}')
