from collections import Counter


monday = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']
tuesday = ['ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLUE', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE']
wednesday = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE']
thursday = ['BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']
friday = ['GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE']

all_color = monday+tuesday+wednesday+thursday+friday
color_counts = Counter(all_color)


color = {'BLUE': 31, 'WHITE': 16, 'GREEN': 10, 'ORANGE': 9, 'RED': 9, 'BROWN': 6, 'YELLOW': 5, 'PINK': 5, 'CREAM': 2, 'ARSH': 1, 'BLACK': 1}

sorted_color = dict(sorted(color.items(), key=lambda item: item[0]))

print(sorted_color)

# Calculate the sum of all values
mean = sum(color.values()) / len(color)

# Get the sorted values
sorted_values = sorted(color.values())

# Calculate the median
length = len(sorted_values)
if length % 2 == 0:
    middle = length // 2
    median = (sorted_values[middle - 1] + sorted_values[middle]) / 2
else:
    median = sorted_values[length // 2]

# Calculate the meandian
meandian = (mean + median) / 2

print(meandian)


squared_differences = [(value - mean) ** 2 for value in color.values()]

# Calculate the variance
variance = sum(squared_differences) / len(squared_differences)

print(variance)


import random

binary_number = ''.join(random.choice('01') for _ in range(4))

# Convert the binary number to base 10
decimal_number = int(binary_number, 2)

# Print the results
print("Binary Number:", binary_number)
print("Decimal Number:", decimal_number)



def fibonacci_sum(n):
    fib_sequence = [0, 1]  # Initial Fibonacci sequence
    for i in range(2, 50):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return sum(fib_sequence)

# Calculate the sum of the first 50 Fibonacci numbers
sum_of_fibonacci = fibonacci_sum(50)
print("Fibonacci numbers:", sum_of_fibonacci)
