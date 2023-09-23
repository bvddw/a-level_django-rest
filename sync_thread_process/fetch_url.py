"""
При тестировании, замечаем что синхронный и многопоточный способы почти не отличаются по времени,
а многопроцессорный - выигрывает во времени, по мере увеличение показателя степени. Для маленьких степеней он
работает дольше всего из-за трудоемкости разделения на процессы. Для больших показателей - это время незначительно по
сравнению с самим расчетом, поэтому выиграываем во времени. Многопроцессорный способ выигрывает когда у нас большой
объем данных для вычислений, многопоточный же - когда нам надо долго ждать ответ от чего-то, например сайт.
"""

import requests
import time
import threading
import multiprocessing


def fetch_url(url):
    response = requests.get(url)
    return response.status_code


def synchronous():
    start_time = time.time()

    for url in ["https://google.com", "https://amazon.com", "https://microsoft.com"]:
        for _ in range(5):
            fetch_url(url)

    end_time = time.time()
    return end_time - start_time


def threaded():
    start_time = time.time()

    threads = []
    for url in ["https://google.com", "https://amazon.com", "https://microsoft.com"]:
        for _ in range(5):
            thread = threading.Thread(target=fetch_url, args=(url,))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    return end_time - start_time


def multiprocess():
    start_time = time.time()

    processes = []
    for url in ["https://google.com", "https://amazon.com", "https://microsoft.com"]:
        for _ in range(5):
            process = multiprocessing.Process(target=fetch_url, args=(url,))
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
