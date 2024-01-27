"""
thread =    a flow of execution. Like a separate order of instructions.
                    However each thread takes a turn running to achieve concurrency
                    GIL = (global interpreter lock)
                    allows only one thread to hold the control of the Python interpreter at any one time

cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
            use multiprocessing

io bound =  program/task spends most of it's time waiting for external events (user input, web scraping)
            use multithreading

# Creating a multithreaded program to simulate concurrent activities:
# In this example, three threads are spawned to represent tasks of eating breakfast, drinking coffee,
# and studying. The `time.sleep()` function is used to simulate time-consuming activities.
# Each thread runs independently, and the `join()` method is used to ensure that the main program
# waits for all threads to finish before proceeding.

# Note: While threads are suitable for IO-bound tasks, for CPU-bound tasks, multiprocessing is generally
# preferred due to the Global Interpreter Lock (GIL) in Python, which limits true parallelism in threads.

"""

# import threading
# import time

# def eat_breakfast():
#     time.sleep(3)
#     print("You eat breakfast")

# def drink_coffee():
#     time.sleep(4)
#     print("You drank coffee")

# def study():
#     time.sleep(5)
#     print("You finish studying")

# x = threading.Thread(target=eat_breakfast, args=())
# x.start()
# y = threading.Thread(target=drink_coffee, args=())
# y.start()
# z = threading.Thread(target=study, args=())
# z.start()

# x.join()
# y.join()
# z.join()

# # eat_breakfast()
# # drink_coffee()
# # study()

# print(threading.active_count())
# print(threading.enumerate())
# print(time.perf_counter())

# --------------------------------------------------------------------------------
import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping in {seconds} second(s)...')
    time.sleep(seconds)
    return f"Done Sleeping...{seconds}"

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

# threads = []
# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)
 
# for thread in threads:
#     thread.join()

finish = time.perf_counter()

print(f"finished in {round(finish-start, 1)} second(s)")

