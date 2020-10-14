min_val = int(input("Enter start value: "))
max_val = int(input("Enter finish value: "))

i = min_val

while i <= max_val:
	print(i, end = " ")
	i+=1

print()

for i in range(min_val, max_val+1):
	print(i, end = " ")