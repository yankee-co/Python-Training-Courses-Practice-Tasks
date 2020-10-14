"""
order = int(input("Ordered number is: "))

fibonacci = [1, 1, 2]

for i in range(3, order):
	x = fibonacci[i - 1] + fibonacci[i - 2]
	fibonacci.append(x)
	if x == order:
		print("Ordered number on the ", i+1," place")
		break
"""

"""
first = 1
second = 1
x = 3
i = 0

while x != order:
	i+=1
	x = second + first
	if x == order:
		print("Ordered number on the ", i + 1, " place.")
	first = second
	second = x
	if x > order:
		print("No match")
		break
"""

# 1 1 2 3 5 8 13 21

x = int(input("Find place of the num in fibonacci list: "))
b = 0
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
for i in fibonacci:
	if fibonacci[b] == x:
		print(x, "on the ", b+1, " place")
		break
	else:
		if fibonacci[b] == fibonacci[-1]:
			print("List finished, no match")
		else:
			b+=1

	
