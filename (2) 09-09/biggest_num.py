first = float(input("Enter first num: "))
second = float(input("Enter second num: "))
third = float(input("Enter third num: "))

# 1

"""
list = (first, second, third)
print(max(list))
"""

# 2

"""
if first > second and first > third:
	max_val = first
if second > first and second > third:
	max_val = second
if third > second and third > first:
	max_val = third
"""

# 3

max_val = first if first > second else second
max_val = second if second > third else third
print(max_val)
