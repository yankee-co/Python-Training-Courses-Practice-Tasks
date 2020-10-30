with open('datafile.txt', 'r') as file:
	file.seek(0, 2)
	size = file.tell()
	file.seek(0)

	count = 0
	b = ''
	floatsum = 0.0
	sec_count = -1
	num_count = 0

	while count <= size:

		b += file.read(count - sec_count)

		if ',' in b:
			b = b.replace(',','')
			floatsum += float(b)
			b = ''
			num_count += 1

		elif size - count <= 0:
			b = b.replace(',','')
			floatsum += float(b)
			num_count += 1

		sec_count+=1
		count+=1

	print("Average: ", floatsum/num_count)
	#0.4989664117770019
