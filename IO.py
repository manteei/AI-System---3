def greeting():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Добро пожаловать в игру 'Эволюция'!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Вы можете задать вопросы по типу:")
    print("1)Я <имя>, что обо мне известно?")
    print("2)Я <имя>, кто играет со мной?")
    print("3)Есть ли в игре <имя>?")
    print("4)Сколько баллов агрессии у <имя>?")
    print("5)Может ли <имя> съесть <имя>?")
    print("6)Какие дополнительные качества есть у игрока <имя>?")
    print("7)Я <имя>, могу ли я жить под водой?")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Для завершения введите \"выход\"")


def goodbye():
    print("До свидания!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def uncorrectRequest():
    print("Неверный запрос. Пожалуйста, уточните ваш запрос.")


def playerNotInGame(player_name):
    print("Упс... кажется игрока " + player_name + " нет.")


def playerInGame(player_name):
    print(player_name + " сейчас играет!")


def agressionOutput(player_name, count):
    print("У игрока " + player_name + " " + count + " балл(а) агрессии.")


def eatOutput(player_name1, player_name2):
    print("Игрок " + player_name1 + " съест игрока " + player_name2)


def notEatOutput(player_name1, player_name2):
    print("Игрок " + player_name1 + " не съест игрока " + player_name2)


def underwaterOutput(player_name):
    print("Да, " + player_name + " может жить под водой")


def onWaterOutput(player_name):
    print("Нет, " + player_name + " не может жить под водой")


def aboutOutput(player_name):
    print("Игрок " + player_name + " имеет следующие характеристики:")


def nutricionOutput(nutricion):
    print("- По типу питания " + nutricion)


def interactionOutput(interaction):
    print("- По типу взаимодействия " + interaction)


def habitatOutput(habitat):
    print("- По месту обитания " + habitat)


def allPlayersOutput(player_name, results):
    print("С вами сейчас в игре:")
    for name in results:
        if name['X'] != player_name:
            print(name['X'])


def printQualities(player_name, results):
    if len(results[0]['Qualities']) > 0:
        print("У игрока " + player_name + " следующие дополнительные качества:")
        for quality in results[0]['Qualities']:
            print(quality)
    else:
        print("У игрока " + player_name + " нет дополнительных качеств")
