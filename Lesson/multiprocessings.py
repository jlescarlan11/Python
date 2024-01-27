"""
multiprocessing =   running tasks in parallel on differen cpy cores, by passes GIL used for threading
                    multiprocessing = better for cpu bound tasks (heavy cpu usage)
                    multithreading = better for io bounf tasks (waiting around)
"""

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    
    print(cpu_count())

    a = Process(target=counter, args=(1000,))
    b =Process(target=counter, args=(1000,))
    a.start()
    b.start()
    
    a.join()
    b.join

    print("Finished in: ", time.perf_counter(), "seconds")

if __name__ == '__main__':
    main()