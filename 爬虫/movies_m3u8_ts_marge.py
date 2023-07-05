"""
@author: JerryYang
@file: movies_m3u8_ts_marge.py
@time: 2023/6/8 21:06
@desc: OK（合并后的文件在ts文件同目录，扩展名为mp4
"""
import os


def get_sorted_filenames(folder_path):
    """

    获取指定文件夹下的所有文件名，并返回一个按数字大小排序的列表。

    """

    filenames = []

    for filename in os.listdir(folder_path):

        if os.path.isfile(os.path.join(folder_path, filename)):
            num = int(filename.split('.')[0])  # 从文件名中提取数字部分

            filenames.append((num, filename))  # 将数字和文件名组成元组，添加到列表中

    filenames.sort()  # 对列表进行排序

    return [f[1] for f in filenames]


# def get_filenames(save_path):
#     """
#
#     获取指定文件夹下的所有文件名，并返回一个列表。
#
#     """
#
#     filenames = []
#
#     for filename in os.listdir(save_path):
#
#         if os.path.isfile(os.path.join(save_path, filename)):
#             filenames.append(filename)
#
#     return filenames


def merge_ts_files(output_file, ts_files, save_path):
    '''
    合并ts文件
    :param output_file: 合并后的文件名
    :param ts_files: 需要合并的TS文件列表
    :param save_path: 文件路径
    :return:
    '''
    with open(save_path + output_file, 'wb') as outfile:
        for ts_file in ts_files:
            with open(save_path + ts_file, 'rb') as infile:
                outfile.write(infile.read())


if __name__ == '__main__':
    save_path = 'D:/pythonProject/爬虫/movie/锦衣之下(7)/'

    ts_files = get_sorted_filenames(save_path)  # 需要合并的TS文件列表
    print(ts_files)

    output_file = save_path.split('/')[-2]+'.mp4'  # 合并后的TS文件名
    print(output_file)

    merge_ts_files(output_file, ts_files, save_path)
