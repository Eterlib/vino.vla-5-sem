import asyncio

q1 = asyncio.Queue()
q2 = asyncio.Queue()

async def prod():
    for i in range(5):
        val = f"value_{i}"
        await q1.put(val)
        print(f"prod: put {val} to q1")
        await asyncio.sleep(1)

async def mid():
    while True:
        val = await q1.get()
        print(f"mid: got {val} from q1")

        await q2.put(val)
        print(f"mid: put {val} to q2")

async def cons():
    while True:
        val = await q2.get()
        print(f"cons: got {val} from q2")

async def main():
    tasks = [
        asyncio.create_task(prod()),
        asyncio.create_task(mid()),
        asyncio.create_task(cons()),
    ]

    await tasks[0]

    await asyncio.sleep(1)

    for t in tasks[1:]:
        t.cancel()

asyncio.run(main())
