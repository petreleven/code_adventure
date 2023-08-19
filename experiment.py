import asyncio
import aiohttp
import pprint


async def download_json_data(url : str, session : aiohttp.ClientSession):
    async with session.get(url) as response:
        print("here")
        data = await response.json()
        print(data['img'])



async def download_kcd_metadata(sites : list):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.create_task(download_json_data(url, session)) 
            tasks.append(task)

        await asyncio.gather(*tasks, return_exceptions=True)   


if __name__=="__main__":
    sites = [f"https://xkcd.com/{i+1}/info.0.json" for i in range(1)]
    asyncio.get_event_loop().run_until_complete(download_kcd_metadata(sites))
