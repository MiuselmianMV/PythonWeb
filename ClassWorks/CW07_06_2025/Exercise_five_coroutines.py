import asyncio


async def print_numbers():
    for i in range(1, 6):
        print(f"Номер - {i}")
        await asyncio.sleep(1)


async def countdown(name: str, seconds: int):
    for i in range(seconds, 0, -1):
        print(f"{name} - {i} ...")
        await asyncio.sleep(1)
    print(f"{name} закончился!")


async def wait_for_15_sec_and_print_hello_world(num:int) -> str:
    for i in range(num, 0, -1):
        print(f"{i}...")
        await asyncio.sleep(1)
    print("Hello, World!")
    return "Hello printed"


async def get_product_of_sum_and_difference(a: int, b: int) -> int:
    print("start calculating...")
    await asyncio.sleep(1)
    print("finished calculating...")
    return (a + b) * (a - b)


async def print_hello():
    for _ in range(3):
        print("Hello!")
        await asyncio.sleep(1)


async def main():
    await asyncio.gather(
        print_numbers(),
        print_hello(),
        wait_for_15_sec_and_print_hello_world(10),
        get_product_of_sum_and_difference(7, 13),
        countdown("Обратный отсчёт", 5))

if __name__ == "__main__":
    asyncio.run(main())
