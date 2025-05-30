# Задание 2
# Создайте программу «Англо-французский словарь».
# Нужно хранить слово на английском языке и его перевод
# на французский. Требуется реализовать возможность добавления, удаления, поиска, замены данных. Используйте
# словарь для хранения информации.

def addOrUpdateWord(word: str, translation: str, dictionary: dict) -> str:
    if word in dictionary:
        text = "Old translation was updated"
    else:
        text = "New word was added to dictionary"

    dictionary[word.lower()] = translation
    return text


def deleteWord(word: str, dictionary: dict) -> str:
    try:
        dictionary.pop(word.lower())
        return f"The word {word} was successfully deleted!"
    except KeyError:
        return f"The word {word} wasn't found in the dictionary"


def findWord(word: str, dictionary: dict) -> str:
    return dictionary.get(word.lower(), f"Unfortunately word {word} isn't in the dictionary")


def showDict(words: dict):
    for word in words:
        print(f"{word.capitalize()} - {words[word].capitalize()}")




def exercise():
    dictionary: dict = {}
    print(addOrUpdateWord("Work", "kqwe", dictionary))
    print(addOrUpdateWord("tree", "qouwe", dictionary))
    print(addOrUpdateWord("hi", "bonjour", dictionary))
    print(addOrUpdateWord("Bye", "se lya vi", dictionary))
    print(addOrUpdateWord("love", "amor", dictionary))
    print("Original dict: ")
    showDict(dictionary)

    print("~"*50)
    print(deleteWord("hi", dictionary))
    print(deleteWord("Work", dictionary))
    print("Let's try to delete word that isn't in the dictionary: ")
    print(deleteWord("j",dictionary))

    print("~"*50)
    print(f"Find the translation to the word 'hi': {findWord('hi', dictionary)}")
    print(f"Find the translation to the word 'lie': {findWord('lie', dictionary)}")
    print(f"Find the translation to the word 'bye': {findWord('bye', dictionary)}")


