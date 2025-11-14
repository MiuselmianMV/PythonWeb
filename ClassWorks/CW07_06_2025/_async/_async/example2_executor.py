import asyncio


def highload_operation(value):
    result = 0
    for i in range(0, value):
        result += i
    return result


async def main(value):
    # выполнение синхронной задачм в pool-е и получение результата.
    result = await loop.run_in_executor(None, highload_operation, value)
    print('Result is {}'.format(result))


loop = asyncio.get_event_loop()
tasks = asyncio.wait([
    loop.create_task(main(10_000_000)),  #В Python подчёркивания используются для разделения групп цифр в числах, как запятые в непрограммных форматах. Эти подчёркивания игнорируются интерпретатором и не влияют на значение числа.
    loop.create_task(main(10_000_001)),
])
loop.run_until_complete(tasks)
loop.close()
