import asyncio
import time

# 1) await는 반드시 비동기 함수 안에서만 사용 가능하다 
# def hello(): ❌
#    await asyncio.sleep(3)

# 2) await 할 수 있는 코드 앞에서만 await를 쑬 수 있다
async def hi():
    print("start hello..")
    await asyncio.sleep(2)
    print("end hello..")

async def main():
    print("start main..")
    coro = hi()
    await coro
    print("end main..")

asyncio.run(main())