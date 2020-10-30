def nums(one, two):
	# First way
	one, two = two, one
	print(one, two)

	#Second way using extra variable
	one, two = two, one # Changing back

	extra = one
	one = two
	two = extra

	print(one, two)

nums(12, 3)
