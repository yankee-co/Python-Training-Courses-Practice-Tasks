def oddGen(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
            yield i


for i in oddGen(30, 50):
    print(i)
