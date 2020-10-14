import collections

#if isinstance(e, collections.Iterable) and not isinstance(e, str):
    # e is iterable

def joiner(*args):
	someList = []
	for i in args:
		if isinstance(i, collections.Iterable) and not isinstance(i, str):
			for i in i:
				someList.append(i)
		else:
			someList.append(i)
	return someList

print(joiner(5, 6, ['7', 8])) # [5, 6, '7', 8]
