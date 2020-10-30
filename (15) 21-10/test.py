import time
import math
from threading import Thread

start = 1 #int(input('Start: '))
end = 3091 #int(input('End: '))

start = time.perf_counter()

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
    return prime_numbers

if (end//1000) > 1:
    threads_count = end//1000
    per_thread = end // threads_count
    low = end - threads_count * per_thread
else:
    threads_count = 1

threads = []
for i in range(1, threads_count + 1):
    if i == threads_count:
        t = Thread(target = get_primary_numbers, args = (start, start + per_thread + low))
        threads.append(t)
        break
    t = Thread(target = get_primary_numbers, args = (start, start + per_thread))
    threads.append(t)
    start += per_thread

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

finish = time.perf_counter()

print('Finished in ', finish, 'seconds')
