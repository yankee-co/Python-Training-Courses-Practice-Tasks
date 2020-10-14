nums = input("Enter nums: ")
sums = 0
print(nums.split(' '))
for i in nums.split(' '):
	if i != '':
		sums+=int(i)
	else:
		continue
print(sums)