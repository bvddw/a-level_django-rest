import asyncio
import aiohttp
import time


async def fetch_url(session, url):
    start_time = time.time()
    response = await session.get(url)
    result = response.text
    return result, time.time() - start_time


async def main():
    urls = [
        "https://google.com",
        "https://google.com",
        "https://google.com",
        "https://google.com",
        "https://google.com",

        "https://amazon.com",
        "https://amazon.com",
        "https://amazon.com",
        "https://amazon.com",
        "https://amazon.com",

        "https://microsoft.com",
        "https://microsoft.com",
        "https://microsoft.com",
        "https://microsoft.com",
        "https://microsoft.com",
    ]

    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[fetch_url(session, url) for url in urls])

    for cur_result in results:
        print(cur_result)

asyncio.run(main())