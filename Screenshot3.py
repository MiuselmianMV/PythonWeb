from typing import Callable


def ExercisesFromScreenshotThree(task1:Callable, task2:Callable, task3:Callable) -> None:
    task1()
    print("~"*50,end="\n")
    task2()
    print("~"*50,end="\n")
    task3()
    print("~"*50,end="\n")

    
def Ex1() -> None:
    text = "lorem ipsum 11 12 13 1  dolor sit amet, consectetur adipiscing elit. sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
    print("Ex1:\n subexercise 1")
    newText = SubExercise1(text)
    print(f"Text with capitalized first letters of each sentence: {newText}")
    print(f"Number of digits in the text: {SubExercise2(text)}")
    print(f"Number of punctuation marks in the text: {SubExercise3(text)}")
    print(f"Number of exclamation marks in the text: {SubExercise4(text)}")


def SubExercise1(text:str)->str:
    print(f"Original text: {text}")
    textLst = list()
    textSplit = text.split()
    
    for index in range(len(textSplit)):
        if index == 0:
            textSplit[index] = textSplit[index].capitalize()
        elif textSplit[index].endswith(".") and index != len(textSplit)-1:

            textSplit[index+1] = textSplit[index+1].capitalize()
        textLst.append(textSplit[index])

    text = " ".join(textLst)
    return text


def SubExercise2(text:str)->int:
    textSplit = text.split()
    counter = 0

    for index in range(len(textSplit)):
        if textSplit[index].isdigit():
            counter += 1
    
    return counter


def SubExercise3(text:str)->None:
    textSplit = text.split()
    counter = 0
    for index in range(len(textSplit)):
        if (textSplit[index].endswith(".") 
        or textSplit[index].endswith(",") 
        or textSplit[index].endswith("!") 
        or textSplit[index].endswith("?") 
        or textSplit[index].endswith(":") 
        or textSplit[index].endswith(";") 
        or textSplit[index] == "--"): 
            counter += 1
    
    return counter


def SubExercise4(text:str)->None:
    textSplit = text.split()
    counter = 0
    for index in range(len(textSplit)):
        if (textSplit[index].endswith("!") 
        or textSplit[index] == "!"): 
            counter += 1
    
    return counter

def Ex2() -> None:
    numbersLst = input("Enter numbers separated by spaces: ").split()
    numbersLst = [int(i) for i in numbersLst]

    number = int(input("Enter a number to count: "))
    print(f"Number of occurrences of {number} in the list: {numbersLst.count(number)}")

def Ex3()->None:
    numbersLst = input("Enter numbers separated by spaces: ").split()
    numbersLst = [int(i) for i in numbersLst]

    print(f"Sum of all numbers in the list: {sum(numbersLst)}")
    print(f"Middle average of all numbers in the list: {sum(numbersLst)/len(numbersLst)}")


    