async def f():
    return 123


coroutine = f()
try:
    coroutine.send(None)
except StopIteration as e:
    print('The answer was:', e.value)
