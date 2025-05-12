from typing import Callable
import random


def ExercisesFromScreenshotTwo(task1:Callable, task2:Callable)->None:
    """
    This function executes exercises from the second screenshot.
    """
    task1()
    print("~"*50,end="\n")
    task2()
    print("~"*50,end="\n")


def Ex1()->None:
    """
    This function executes the first exercise of the task.
    """
    lst = [random.randint(-50, 50) for _ in range(10)]
    print(f"List: {lst}")
    
    print("Sum of negative elements:", sum(i for i in lst if i < 0))
    
    print("Sum of even elements:", sum(i for i in lst if i % 2 == 0))

    print("Sum of odd elements:", sum(i for i in lst if i % 2 != 0))

    print("Product of elements with indexes divisible by 3:",
          Product(i for i in range(len(lst)) if i % 3 == 0))
    start = lst.index(min(lst))
    end = lst.index(max(lst))
    if start > end:
        start, end = end, start
    print("Product of elements between min and max:",
          Product(i for i in lst[start + 1 : end]))
    
    first_positive_index, last_positive_index = FindFirstPositiveIndex(lst), FindLastPositiveIndex(lst)    

    print("Sum of elements between first and last positive elements:",
          sum(i for i in lst[first_positive_index + 1 : last_positive_index]))


def FindFirstPositiveIndex(lst: list) -> int:
    """
    Эта функция находит индекс первого положительного элемента в списке."""
    for i in range(len(lst)):
        if lst[i] > 0:
            first_positive_index = i
            break
    return first_positive_index


def FindLastPositiveIndex(lst: list) -> int:
    """
    Эта функция находит индекс последнего положительного элемента в списке."""
    for i in range(len(lst)-1, 0, -1):
        if lst[i] > 0:
            last_positive_index = i
            break
    return last_positive_index


def Product(lst: list) -> int:
    """
    Эта функция принимает список и возвращает произведение всех элементов списка.
    """
    result = 1

    for i in lst:
        result *= i
        
    return result

def Ex2()->None:
    randLst = [random.randint(-50, 50) for _ in range(10)]
    print(f"List: {randLst}")

    print(f"List with only even elements: {[i for i in randLst if i%2 == 0]}")
    print(f"List with only odd elements: {[i for i in randLst if i%2 != 0]}")
    print(f"List with only negative elements: {[i for i in randLst if i < 0]}")
    print(f"List with only positive elements: {[i for i in randLst if i > 0]}")
