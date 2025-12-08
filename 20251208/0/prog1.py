import asyncio

async def squarer(x):
    await asyncio.sleep(0)
    return x * x

async def doubler(x):
    await asyncio.sleep(0)
    return 2 * x

async def main():
    data = [3, 5]

    squares = await asyncio.gather(
        squarer(data[0]),
        squarer(data[1])
    )

    result = await asyncio.gather(
        doubler(squares[0]),
        doubler(squares[1])
    )

    print(result)

asyncio.run(main())
