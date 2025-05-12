import random

def ExercisesFromScreenshotOne()->None:
    """
    This function executes the first exercise of the task.
    """
    randLst1 = [random.randint(1, 100) for _ in range(10)]
    randLst2 = [random.randint(1, 100) for _ in range(10)]

    print(f"List 1:{randLst1} ")
    print(f"List 2:{randLst2} ")

    print("~"*50,end="\n")
    #1
    lst3 = []
    lst3.extend(randLst1)
    lst3.extend(randLst2)

    print(f"Third list with elements from both lists: {lst3}", end="\n\n")
    
    print("~"*50,end="\n")
    #2
    lst3 = list(set(lst3))

    #Удаляем дубликаты из списка, преобразовав его в множество, а затем обратно в список
    print(f"Third list with elements from both lists without repeatings: {lst3}", end="\n\n")

    print("~"*50,end="\n")
     
    #3
    lst3 = list(set(randLst1) & set(randLst2)) # list(set.intersection(randLst1, randLst2))
    #Находим пересечение двух множеств
    print(f"Third list with common elements from both lists: {lst3}", end="\n\n")
    
    print("~"*50,end="\n")
    #4
    lst3 = list(set.union(set(randLst1), set(randLst2))) 

    print(f"Third list with unique elements from both lists: {lst3}", end="\n\n")

    print("~"*50,end="\n")
    #5
    lst3 = [max(randLst1), min(randLst1), max(randLst2), min(randLst2)]
    #Находим максимальные и минимальные элементы из двух списков
    print(f"Third list with max and min elements from both lists: {lst3}", end="\n\n")
    print("~"*50,end="\n")
