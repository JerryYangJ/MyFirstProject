"""
@author: JerryYang
@file: moviess_m3u8_加密（协程版）.py
@time: 2023/6/25 21:20
@desc: 注意：
        报错一：
            RuntimeError: Event loop is closed
            Exception ignored in: <function _ProactorBasePipeTransport.__del__ at 0x0000022D1E669900>
        可能原因（网上说明）：
            1.注意：在调用Main()方法时，不能使用语句：asyncio.run(Main())虽然会得到想要的响应，但会报错。
            2.大佬的总结是asyncio.run()会自动关闭循环,并且调用_ProactorBasePipeTransport.__del__报错, 而asyncio.run_until_complete()不会。

        尝试解决方案：实测方法3有效
            1.主线程运行方式更改为：-------（无效）
                loop = asyncio.get_event_loop()
                loop.run_until_complete(main())
            2.尝试不使用aiofiles，只使用aiohttp
            3.在run前增加如下代码：asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())---------（有效）

        报错二：
            aiohttp.client_exceptions.ClientPayloadError: Response payload is not completed

        报错三：
            aiohttp.client_exceptions.ServerDisconnectedError: Server disconnected
        尝试解决方案：
            1.设置最大并发数：connector = aiohttp.TCPConnector(limit=5)
            2.用协程池限制最大并发数：semaphore = asyncio.Semaphore(5)  # 设置最大并发数为5---------（有效）

        报错四：
            aiohttp.ClientTimeout
        尝试解决方案：
            1.设置最超时时间：timeout = aiohttp.ClientTimeout(total=900)---------（有效）
            2.通过try-except增加报错后重新请求：---------（有效）


"""
import os
import time
import asyncio
import aiohttp
import aiofiles
import traceback


m3u8_url = 'https://www.bjzk010.com/guocanju/jinyizhixia/4-8.html'


async def down_ts(ts_line, ts_name, headers, save_path, session):
    """
    下载ts文件
    :param ts_line: ts地址
    :param ts_name: ts文件名
    :return: 数据和名字
    """
    # 向视频片段下载链接发送请求，获取数据。
    try:
        async with session.get(url=ts_line, headers=headers) as ts_resp:
            a = await ts_resp.content.read()
            print(f'{ts_name}完成下载')
            # async with aiofiles.open(f'{save_path}/{ts_name}.ts', 'wb') as f:
            #     a = await ts_resp.content.read()
            #     await f.write(a)
            #     print(f'{ts_name}完成下载')
    except Exception as e:
        print(f'{ts_name}:{ts_line}下载失败！准备重新下载')
        await asyncio.sleep(2)
        try:
            async with session.get(url=ts_line, headers=headers) as ts_resp:
                a = await ts_resp.content.read()
                print(f'{ts_name}重新下载成功')
                # async with aiofiles.open(f'{save_path}/{ts_name}.ts', 'wb') as f:
                #     # await f.write(await ts_resp.content.read())
                #     a = await ts_resp.content.read()
                #     await f.write(a)
                #     print(f'{ts_name}重新下载成功')
        except Exception as e:
            traceback.print_exc()
            print(f'{ts_name}:{ts_line}重新下载失败，请手工下载!')
    # if a:
    return ts_name, a

async def main():
    # 请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
    }
    # 读取m3u8文件路径
    m3u8_file_path = 'D:\下载\index (26).m3u8'
    # 保存路径
    save_path = './movie/锦衣之下(27)/'
    # 保存文件前判断文件存储路径是否存在，不存在则创建路径
    if not os.path.exists(save_path):
        os.mkdir(save_path)
        time.sleep(1)

    tasks = []

    # # 设置超时时间
    # timeout = aiohttp.ClientTimeout(total=900)
    # # 设置并发数量(设置过大容易出现Server Disconnected错误
    # connector = aiohttp.TCPConnector(limit=5)
    # # 创建一个异步session
    # async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
    #     # 读取m3u8文件，提取url，创建协程对象
    #     with open(m3u8_file_path, 'r') as f:
    #         n = 1
    #         for ts_line in f:
    #             ts_line = ts_line.strip()
    #             if not ts_line.startswith("#"):
    #                 # ts_line = base_url + ts_line
    #                 print(f'{n}:{ts_line}')
    #                 # task = asyncio.create_task(down_ts(ts_line, n, headers, save_path, session))
    #                 # tasks.append(task)
    #                 n += 1
    #     # # 启动协程对象
    #     # await asyncio.gather(*tasks)
    # print("Download completd!!")

    # 用协程池限制最大并发数
    semaphore = asyncio.Semaphore(5)  # 设置最大并发数为5

    # 设置超时时间
    timeout = aiohttp.ClientTimeout(total=900)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        # 读取m3u8文件，提取url，创建协程对象
        with open(m3u8_file_path, 'r') as f:
            n = 1
            for ts_line in f:
                async with semaphore:
                    ts_line = ts_line.strip()
                    if not ts_line.startswith("#"):
                        print(f'{n}:{ts_line}')
                        task = asyncio.create_task(down_ts(ts_line, n, headers, save_path, session))
                        tasks.append(task)
                        n += 1
        # 启动协程对象
        results = await asyncio.gather(*tasks)
    print("Download completd!!")

    # 对下载的ts片段进行合并
    names = []
    data_list = []
    for result in results:
        # print(result[0])
        names.append(result[0])
        data_list.append(result[1])
    # 合并数据
    output_file = save_path.split('/')[-2] + '.mp4'  # 合并后的mp4文件名
    with open(save_path + output_file, 'wb') as outfile:
        for data in data_list:
            outfile.write(data)
    print("完成合并，保存路径", save_path+output_file)


if __name__ == '__main__':
    # 方法一：此方案可以解决Event loop is closed报错问题
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())

    # 方法二:可以运行，但仍无法解决报错
        # RuntimeError: Event loop is closed
        # Exception ignored in: <function _ProactorBasePipeTransport.__del__ at 0x00000186C57B5FC0>
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # loop.close()

