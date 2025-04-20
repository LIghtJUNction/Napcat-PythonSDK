# -*- coding: utf-8 -*-
import asyncio
from napcat.clients.http.v1 import AsyncHttpClient

from napcat.api.account.get_friend_list import GetFriendListAPI, Request, Response # type: ignore[import]
# 初始化

client : AsyncHttpClient = AsyncHttpClient(
    base_url="http://127.0.0.1:10144",
    token="10144",
    timeout=60.0,
    debug=True 
)

# 测试连接

_client = client.client

# print(client.client)



async def main():
    # 测试连接
    API = GetFriendListAPI()

    API.request = Request(
        no_cache = False
    )

    await client.send(
        API=API
    )

    print(API.response)

asyncio.run(main())