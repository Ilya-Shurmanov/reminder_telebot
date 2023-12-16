import asyncio


async def test(a, b):
    print('func called')
    print(a + b)

asyncio.run(test(1, 2))

