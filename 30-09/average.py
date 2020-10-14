#	1 WAY

print("FIRST WAY")
with open('datafile.txt','r') as file:
	strlist = file[0].split(',')
	counter = 0
	numsum = 0
	for i in strlist:
		numsum+=float(i)
		counter+=1
	print('There\'s',counter,'float nums. Sum of all of them is', numsum,'Average: ', numsum/counter)

""" Output: There's 100501 float nums. Sum of all of them is 50146.62335000047 Average:  0.4989664117770019 """

#	2 WAY

print("SECOND WAY")
with open('datafile.txt') as file:
	counter = 0
	numsum = 0
	for each in file.read().split(','):
		numsum += float(each)
		counter += 1
	print('There\'s',counter,'float nums. Sum of all of them is', numsum,'Average: ', numsum/counter)

""" Output: There's 100501 float nums. Sum of all of them is 50146.62335000047 Average:  0.4989664117770019 """
