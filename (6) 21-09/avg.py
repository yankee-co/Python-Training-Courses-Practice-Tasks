def avg(a, b) -> float:
    counter = 0
    numSum = 0
    for n in range(a, b + 1):
        numSum += n
        counter += 1
    return numSum / counter


print(avg(1, 10))
print(avg(9000, 100500))
