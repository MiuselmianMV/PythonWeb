def addBook(title: str, author: str, genre: str, year: int,
            pages: int, publisher: str, collection: dict) -> str:
    book = {
        'title': title.lower(),
        'author': author,
        'genre': genre,
        'year': year,
        'pages': pages,
        'publisher': publisher
    }

    collection[len(collection)] = book
    return "New book was successfully added!"


def showCollection(collection: dict) -> None:
    for i in collection:
        book = collection[i]
        print(f"Book number {i}: \n"
              f"Title: {book['title'].title()}\n"
              f"Author: {book['author']}\n"
              f"Genre: {book['genre']}\n"
              f"Year: {book['year']}\n"
              f"Pages: {book['pages']}\n"
              f"Publisher: {book['publisher']}\n")
        print("-" * 50)


def findBook(title: str, collection: dict) -> int | None:
    for key in collection:
        if collection[key]['title'] == title.lower():
            return key
    return None


def updateBook(title: str, collection: dict, author: str = None, genre: str = None,
               year: int = None, pages: int = None, publisher: str = None) -> str:
    book_id = findBook(title, collection)
    if book_id is not None:
        book = collection[book_id]
        if author:
            book['author'] = author
        if genre:
            book['genre'] = genre
        if year:
            book['year'] = year
        if pages:
            book['pages'] = pages
        if publisher:
            book['publisher'] = publisher
        return f"Book '{title}' was successfully updated!"
    else:
        return f"Book '{title}' was not found in the collection."


def deleteBook(title: str, collection: dict) -> str:
    for key in list(collection.keys()):
        if collection[key]['title'] == title.lower():
            collection.pop(key)
            return f"Book '{title}' was successfully deleted!"
    return f"Book '{title}' was not found in the collection."


def exercise():
    library = dict()

    # Добавляем книги
    print(addBook("War and Peace", "Leo Tolstoy", "Historical", 1869, 1225, "The Russian Messenger", library))
    print(addBook("1984", "George Orwell", "Dystopian", 1949, 328, "Secker & Warburg", library))
    print(addBook("The Hobbit", "J.R.R. Tolkien", "Fantasy", 1937, 310, "Allen & Unwin", library))

    print("\nAll books in collection:")
    showCollection(library)

    print("~" * 50)
    print(f"Finding book '1984':")
    book_id = findBook("1984", library)
    print(library[book_id] if book_id is not None else "Not found")

    print("~" * 50)
    print(deleteBook("The Hobbit", library))
    print(deleteBook("Nonexistent Book", library))

    print("~" * 50)
    print(updateBook("War and Peace", library, publisher="New Publisher"))
    book_id = findBook("War and Peace", library)
    print(f"Updated info: {library[book_id] if book_id is not None else 'Not found'}")


exercise()
