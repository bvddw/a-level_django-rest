import asyncio
import time


async def big_power_counter(name, number):
    start_time = time.time()
    result = 1
    for i in range(1, 1000000):
        await asyncio.sleep(0)
        result *= number
    return name, time.time() - start_time


async def main():
    tasks = [
        big_power_counter("two", 2),
        big_power_counter("three", 3),
        big_power_counter("five", 5),
    ]

    results = await asyncio.gather(*tasks)

    for name, execution_time in results:
        print(f"{name}: Execution Time: {execution_time:.2f} seconds")


asyncio.run(main())