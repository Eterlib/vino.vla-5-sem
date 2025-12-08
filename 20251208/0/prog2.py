import asyncio

async def squarer(x):
    await asyncio.sleep(0)
    return x * x

async def doubler(x):
    await asyncio.sleep(0)
    return 2 * x

async def main():
    data = [3, 5]

    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(squarer(data[0]))
        t2 = tg.create_task(squarer(data[1]))

    squares = [t1.result(), t2.result()]

    async with asyncio.TaskGroup() as tg:
        d1 = tg.create_task(doubler(squares[0]))
        d2 = tg.create_task(doubler(squares[1]))

    result = [d1.result(), d2.result()]
    print(result)

asyncio.run(main())
