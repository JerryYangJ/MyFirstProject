"""
@author: JerryYang
@file: m3u8.py
@time: 2023/6/19 14:37
@desc:
"""
from movies_m3u8_加密 import decode_ts
from movies_m3u8_加密 import down_ts

down_ts(ts_line, ts_name, save_path, key)
decode_ts(data, key)