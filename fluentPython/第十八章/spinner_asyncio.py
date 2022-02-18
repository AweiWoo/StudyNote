import asyncio
import itertools
import sys

@asyncio.coroutine  #此装饰器突出表面下面函数是协程
def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            yield from asyncio.sleep(.1)  #这样的休眠不会阻塞事件循环
        except asyncio.CancelledError:
            break
    write(' ' * len(status) + '\x08' * len(status))

@asyncio.coroutine
def slow_function():      #协程，使用休眠假装进行 I/O 操作，使用yield from继续执行事件循环
    yield from asyncio.sleep(5) #把控制权交给主循环，在休眠结束后恢复这个协程
    return 42

@asyncio.coroutine
def supervisor():     #协程
    spinner = asyncio.async(spin('thinking!')) #排定spin协程的运行时间，使用一个Task对象包装spin协程，并立即返回
    print('spinner object:' , spinner)  #spinner object: <Task pending coro=<spin() running....
    #获取返回值后，事件循环继续运行，因为slow_function 函数最后使用 yield from asyncio.sleep(3) 表达式把控制权交回给了主循环
    result = yield from slow_function()  
    spinner.cancel() #协程可以捕获这个异常，也可以延迟取消，甚至拒绝取消。
    return result

def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor())
    loop.close()
    print('Answer', result)

if __name__ == '__main__':
    main()
