import time
import asyncio
from timeit import default_timer as timer 


def run_task(name, seconds):
    print(f'{name} timer started at: {timer()}')
    time.sleep(seconds)
    print(f'{name} completed at: {timer()}')

start = timer()
run_task('Task 1', 2)
run_task('Task 2', 5)
run_task('Task 3', 3)
end = timer()

print(end - start)


async def run_task_async(name, seconds):
    print(f'{name} timer started at: {timer()}')
    await asyncio.sleep(seconds)
    print(f'{name} completed at: {timer()}')

async def main(): 
    start = timer()
    await asyncio.gather(
        run_task_async('Task 1', 2),
        run_task_async('Task 2', 5),
        run_task_async('Task 3', 3)
    )
    end = timer()
    print(end - start)

asyncio.run(main())