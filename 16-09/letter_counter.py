string = input("Enter text: ")

countDict = {}
chars = [n for n in string]
examples = set(chars)

if '\t' in examples:
	examples.remove('\t')
if ' ' in examples:
	examples.remove(' ')

print("Character | Counter")

for n in chars:
	if n != '\t' or n != ' ':
		for n in examples:
			countDict.update({
				n : chars.count(n)
				})
	else:
		continue
for k, v in countDict.items():
	print(k, v)