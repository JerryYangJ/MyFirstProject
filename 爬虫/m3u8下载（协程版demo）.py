"""
@author: JerryYang
@file: m3u8下载（协程版demo）.py
@time: 2023/6/23 11:53
@desc: 代码中，download_u3u8函数使用aiohttp库建立异步的HTTP会话，通过GET请求下载u3u8文件，并解析该文件以获取所有分片的URL。然后，它创建一个
        协程任务列表tasks，每个任务都是一个download_segment协程，用于下载单个分片。最后，使用asyncio.gather并发运行所有的下载任务。
"""


import asyncio
import aiohttp

async def download_segment(session, url, file_name):
    async with session.get(url) as response:
        if response.status == 200:
            with open(file_name, 'wb') as f:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    f.write(chunk)
        else:
            print(f"Failed to download segment from {url}")

async def download_u3u8(url, output_dir):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                m3u8_content = await response.text()
                segments = parse_m3u8(m3u8_content)  # 解析m3u8文件获取所有的分片URL
                tasks = []
                for i, segment_url in enumerate(segments):
                    file_name = f"{output_dir}/segment_{i}.ts"
                    task = asyncio.create_task(download_segment(session, segment_url, file_name))
                    tasks.append(task)
                await asyncio.gather(*tasks)  # 并发下载所有分片
                print("Download completed.")
            else:
                print(f"Failed to download u3u8 file from {url}")

def parse_m3u8(m3u8_content):
    # 解析m3u8文件获取所有的分片URL，这里需要根据具体的m3u8文件格式进行解析
    # 示例中假设m3u8文件中的分片URL以换行符分隔
    return m3u8_content.strip().split('\n')

# 示例用法
url = "http://example.com/your_u3u8_file.u3u8"
output_dir = "downloaded_segments"
asyncio.run(download_u3u8(url, output_dir))
