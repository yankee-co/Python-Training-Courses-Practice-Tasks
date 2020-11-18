import math
from multiprocessing import Pool


def get_primary_numbers(listedArgs):

    start = listedArgs[0]
    end = listedArgs[1]

    prime_numbers = []
    for number in range(start, end):
        for div in range(2, math.ceil(math.sqrt(number))):
            if number != div and number % div == 0:
                if number in prime_numbers:
                    prime_numbers.remove(number)
                break
            else:
                if number not in prime_numbers:
                    prime_numbers.append(number)
    return(prime_numbers)

if __name__ == '__main__':

    start = int(input('Start: '))
    end = int(input('End: '))

    processes_count = 4
    per_process = end // processes_count
    low = end - per_process * processes_count
    cycleStart = start
    listedArgs = []

    for index in range(1, processes_count + 1):
        if index == 4:
            listedArgs.append([cycleStart, cycleStart + per_process + low])
            break
        listedArgs.append([cycleStart, cycleStart + per_process])
        cycleStart += per_process

    p = Pool(processes_count)
    print(p.map(get_primary_numbers, listedArgs))
