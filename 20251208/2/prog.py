import asyncio
import random
async def merge(A1, A2, start, middle, finish, event_in1, event_in2, event_out):
    await event_in1.wait()
    await event_in2.wait()

    i, j, k = start, middle, start
    while i < middle and j < finish:
        if A1[i] <= A1[j]:
            A2[k] = A1[i]
            i += 1
        else:
            A2[k] = A1[j]
            j += 1
        k += 1

    while i < middle:
        A2[k] = A1[i]
        i += 1
        k += 1

    while j < finish:
        A2[k] = A1[j]
        j += 1
        k += 1

    event_out.set()


async def mtasks(A):
    n = len(A)

    Awork = list(A)
    B = [None] * n

    tasks = []
    if n <= 1:
        return tasks, Awork

    events = []
    for start in range(0, n, 1):
        e = asyncio.Event()
        e.set()
        events.append(e)

    empty_ready = asyncio.Event()
    empty_ready.set()

    src, dst = Awork, B
    size = 1

    while size < n:
        new_events = []
        run_len = 2 * size

        run_index = 0
        for start in range(0, n, run_len):
            middle = min(start + size, n)
            finish = min(start + run_len, n)

            left_event = events[run_index]
            run_index += 1

            if middle < finish:
                right_event = events[run_index]
                run_index += 1
            else:
                right_event = empty_ready

            out_event = asyncio.Event()
            new_events.append(out_event)

            tasks.append(
                merge(src, dst, start, middle, finish,
                      left_event, right_event, out_event)
            )

        src, dst = dst, src
        events = new_events
        size *= 2

    return tasks, src

import sys
exec(sys.stdin.read())
