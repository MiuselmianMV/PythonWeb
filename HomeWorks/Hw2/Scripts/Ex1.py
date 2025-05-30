# Задание 1
# Создайте программу, хранящую информацию о великих баскетболистах. Нужно хранить ФИО баскетболиста и
# его рост. Требуется реализовать возможность добавления,
# удаления, поиска, замены данных. Используйте словарь
# для хранения информации.


def addPlayer(name: str, height: int, players: dict):
    player = {
        'name': name,
        'height': height
    }

    players[len(players)] = player


def findPlayer(name: str, players: dict):
    for player in players:
        if players[player]['name'] == name:
            return players[player]
    else:
        return "Player not found"


def deletePlayer(name: str, players: dict):
    for player in players:
        if players[player]['name'] == name:
            return players.pop(player)
    else:
        return "Player not found"


def showDict(players: dict):
    for i in players:
        player = players[i]
        print(f"{player['name']} - {player['height']}")


def exercise():
    players = dict()
    addPlayer("MJ", 120, players)
    addPlayer("Po", 140, players)
    addPlayer("Rd", 220, players)
    addPlayer("Wd", 240, players)
    showDict(players)
    print("~" * 50)
    print("Let's delete player MJ and see what we've deleted: ")

    print(f"Deleted player: {deletePlayer('MJ', players)}")
    showDict(players)

    print("~" * 50)

    print("Is there a player MJ?")
    print(findPlayer("MJ", players))

    print("~" * 50)

    print("Is there a player Wd?")
    print(findPlayer("Wd", players))


