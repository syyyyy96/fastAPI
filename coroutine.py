# 동기식
# 1) 함수 정의 : def foo():
# 2) 함수 호출 : foo() => 함수 실행 

# 비동기식
# 1) 코루틴 함수 정의 : async def boo():
# 2) 코르틴 함수 호출 : coro = boo() => 코르틴 객체 생성 
# 3) 코르틴 함수 실행 

import asyncio

async def hello():
    print("hello")

coro1 = hello()

asyncio.run(coro1)



