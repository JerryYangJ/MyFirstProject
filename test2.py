import requests


url = 'https://gpt.chatapi.art/backend-api/moderations'
headers ={
    # ':authority: gpt.chatapi.art
    # :method: POST
    # :path: /backend-api/moderations
    # :scheme: https
    # accept: */*
    # accept-encoding: gzip, deflate, br
    # accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
    # authorization: Bearer
    # content-length: 67
    'content-type': 'application/json',
    'origin': 'https://gpt.chatapi.art',
    'referer': 'https://gpt.chatapi.art/',
    # sec-ch-ua: "Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"
    # sec-ch-ua-mobile: ?0
    # sec-ch-ua-platform: "Windows"
    # sec-fetch-dest: empty
    # sec-fetch-mode: cors
    # sec-fetch-site: same-origin
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62'
}


data ={
    'input': "介绍下你自己",
    'model': "text-moderation-playground"
}

resp = requests.post(url=url, headers=headers, data=data)
print(resp.status_code)