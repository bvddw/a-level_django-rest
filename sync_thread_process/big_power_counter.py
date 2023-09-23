"""
When testing, we notice that the synchronous and multithreading methods are almost the same in time,
and the multiprocessor method wins in time as the exponent increases. For small degrees it takes the longest due to
the complexity of dividing into processes. For large indicators, this time is insignificant compared to the
calculation itself, so we gain time. The multiprocessor method wins when we have a large amount of data for
calculations, while the multithreading method wins when we need to wait a long time for a response from something,
for example a website.
"""


import time
import threading
import multiprocessing


def big_power(number):
    result = number ** 10000000
    return result


def synchronous():
    start_time = time.time()

    for number in [2, 3, 5]:
        big_power(number)

    end_time = time.time()
    return end_time - start_time


def threaded():
    start_time = time.time()

    threads = []
    for number in [2, 3, 5]:
        thread = threading.Thread(target=big_power, args=(number,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    return end_time - start_time


def multiprocess():
    start_time = time.time()

    processes = []
    for number in [2, 3, 5]:
        process = multiprocessing.Process(target=big_power, args=(number,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()
    return end_time - start_time


if __name__ == "__main__":
    sync_time = synchronous()
    thread_time = threaded()
    process_time = multiprocess()

    print(f"Synchronous Time: {sync_time} seconds")
    print(f"Threaded Time: {thread_time} seconds")
    print(f"Multiprocess Time: {process_time} seconds")
