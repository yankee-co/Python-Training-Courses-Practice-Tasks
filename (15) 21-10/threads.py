import math, threading

start = 1 #int(input('Start: '))
end = 4911 #int(input('End: '))

def get_primary_numbers(start: int, end: int):
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
    print(prime_numbers)
    return(prime_numbers)

if end//1000 > 1: threads_count = end//1000
else: threads_count = 1 # 3
per_thread = end // threads_count #  1030
low = end - per_thread * threads_count #  2

#print(threads_count, per_thread, low)

cycleStart = start
threads = []

for index in range(1, threads_count + 1):
    if index == threads_count:
        t = threading.Thread(target = get_primary_numbers, args = (cycleStart, cycleStart + per_thread + low))
        threads.append(t)
        break
    t = threading.Thread(target = get_primary_numbers, args = (cycleStart, cycleStart + per_thread))
    threads.append(t)
    cycleStart += per_thread

for thread in threads:
    thread.start()

threading._shutdown()
