import asyncio

evsnd = asyncio.Event()
evmid0 = asyncio.Event()
evmid1 = asyncio.Event()

async def snd():
    evsnd.set()
    print("snd: generated evsnd")

async def mid(k):
    await evsnd.wait()
    print(f"mid{k}: received evsnd")

    if k == 0:
        evmid0.set()
        print("mid0: generated evmid0")
    else:
        evmid1.set()
        print("mid1: generated evmid1")

async def rcv():
    await evmid0.wait()
    print("rcv: received evmid0")

    await evmid1.wait()
    print("rcv: received evmid1")

async def main():
    tasks = [
        asyncio.create_task(rcv()),
        asyncio.create_task(mid(1)),
        asyncio.create_task(mid(0)),
        asyncio.create_task(snd()),
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())
