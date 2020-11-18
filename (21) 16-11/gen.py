def num():
    if number > :
        for number in range(12):
            for x in range(2, number):
                if number % x == 0:
                    break
            else:
                yield number


gen = num()
for i in gen:
    print(i)
gen.send(95)
