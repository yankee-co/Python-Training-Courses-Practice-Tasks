minute = int(input("Enter minutes: "))

first = range(1,16)
second = range(16,31)
third = range(31,46)
fourth = range(46,61)

if minute in first:
	print("It's in first quater")
elif minute in second:
	print("It's in second quater")
elif minute in third:
	print("It's in third quater")
elif minute in fourth:
	print("It's in fourth quater")
else:
	print("Some data given wrong")