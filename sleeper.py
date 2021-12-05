import random
import time

def sleep_time( min = int, max = int ): # Sleep time Zzz
    duration = random.randint(min, max)
    print(f'Sleep for {duration} sec.')
    for sleep_count in range(1, duration)[::-1]:
        time.sleep(1)
    print('Resume')

sleep_time(5, 9)