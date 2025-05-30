# Задание 3
# Создайте программу «Фирма». Нужно хранить информацию о человеке: ФИО, телефон, рабочий email,
# название должности, номер кабинета, skype. Требуется
# реализовать возможность добавления, удаления, поиска, замены данных. Используйте словарь для хранения
# информации.

def addEmployee(name: str, phone_number: str, email: str, position: str, roomNumber: int,
                skypeName: str, dictionary: dict) -> str:
    employee = {
        'name': name.lower(),
        'phone_number': phone_number,
        'email': email,
        'position': position,
        'roomNumber': roomNumber,
        'skypeName': skypeName,
    }

    dictionary[len(dictionary)] = employee

    return "New employee was successfully added!"


def showDict(employees: dict) -> None:
    for i in employees:
        employee = employees[i]
        print(f"Employee number {i}: \n"
              f"{employee['name']}\n "
              f"{employee['phone_number']}\n"
              f"{employee['email']}\n"
              f"{employee['position']}\n"
              f"{employee['roomNumber']}\n"
              f"{employee['skypeName']}\n"
              )
        print("-" * 50)


def updateEmployee(name: str, dictionary: dict, phone_number: str = None, email: str = None,
                   position: str = None, roomNumber: int = None, skypeName: str = None) -> str:
    emp_id = findEmployee(name, dictionary)
    if emp_id is not None:
        employee = dictionary[emp_id]
        if phone_number:
            employee['phone_number'] = phone_number
        if email:
            employee['email'] = email
        if position:
            employee['position'] = position
        if roomNumber:
            employee['roomNumber'] = roomNumber
        if skypeName:
            employee['skypeName'] = skypeName
        return f"Employee {name} was successfully updated!"
    else:
        return f"The employee {name} wasn't found in the dictionary"



def deleteEmployee(name: str, dictionary: dict) -> str:
    for i in list(dictionary.keys()):
        if dictionary[i]['name'] == name.lower():
            dictionary.pop(i)
            return f"The employee {name} was successfully deleted!"
    return f"The employee {name} wasn't found in the dictionary"


def findEmployee(name: str, dictionary: dict) -> int | None:
    for i in dictionary:
        if dictionary[i]['name'] == name.lower():
            return i
    else:
        return None


def exercise():
    firm: dict = dict()
    print(addEmployee("A", "+12345", "asd@asdf", "Middle manager", 1, "A_skype", firm))
    print(addEmployee("B", "+54321", "[pqwer@asdf", "Senior manager", 2, "B_skype", firm))
    print(addEmployee("C", "+23145", "lwqerqew@asdf", "Junior manager", 3, "C_skype", firm))

    showDict(firm)
    print("~" * 50)

    emp_id = findEmployee("A", firm)
    print(f"Let's find employee A: {firm[emp_id] if emp_id is not None else 'Not found'}")

    emp_id = findEmployee("D", firm)
    print(f"Let's find employee D(not in the dict): {firm[emp_id] if emp_id is not None else 'Not found'}")

    print("~" * 50)
    print(deleteEmployee("A", firm))
    print(f"Let's delete employee D(not in the dict): {deleteEmployee('D', firm)}")

    print("~" * 50)
    print(f"Let's update employee C: {updateEmployee('C', firm, skypeName='C_newSkype')}")
    emp_id = findEmployee("C", firm)
    print(f"New info: {firm[emp_id] if emp_id is not None else 'Not found'}")


