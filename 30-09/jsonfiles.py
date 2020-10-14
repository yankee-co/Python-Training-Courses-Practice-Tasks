import json

with open('res.txt', 'w') as file:
	val = json.dumps([i for i in range(1,9000)])
	#print(val)
	file.write(val)

with open('res.txt', 'r') as file:
	lines = file.read()
	lines = json.loads(lines)
	print(lines)
	#print(type(lines)) # list