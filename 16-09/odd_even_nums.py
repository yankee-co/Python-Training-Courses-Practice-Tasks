every = {i for i in range(1,9000) if i % 13 == 0}
odd = {i for i in every if i % 2 != 0}
even = every - odd
numDict = {
	"ODD" : sorted(list(odd)),
	"EVEN" : sorted(list(even))
}
for k, v in numDict.items():
	print(k, v)
