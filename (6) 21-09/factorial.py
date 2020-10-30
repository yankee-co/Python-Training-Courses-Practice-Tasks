def fact(num: int) -> int:
	if num == 0: return 1
	b = 1
	for i in range(1, num+1):
		b *= i
	return b

print(fact(6)) # 720
print(fact(5)) # 120
print(fact(0)) # 1