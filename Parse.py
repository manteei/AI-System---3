from pyswip import Prolog

from Requests import isPlayerInGame, countAgression, willEat, findQualities, checkUnderwater, findNutricion, \
    findHabitat, findInteraction, findAllPlayers
from IO import goodbye, uncorrectRequest


def parser(user_input):
    if user_input.lower() == "выход":
        goodbye()
        return 0
    elif "есть ли в игре" in user_input.lower():
        parts = user_input.split()
        player_name = parts[-1][:-1]
        query = f"player_now('{player_name}')"
        isPlayerInGame(query, player_name, True)
    elif "сколько баллов агрессии у" in user_input.lower():
        parts = user_input.split()
        player_name = parts[-1][:-1]
        query = f"count_attack({player_name}, X)"
        countAgression(query, player_name)
    elif "может ли" and "съесть" in user_input.lower():
        parts = user_input.split()
        player_name1 = parts[2]
        player_name2 = parts[4][:-1]
        query = f"player_now('{player_name1}')"
        flag1 = isPlayerInGame(query, player_name1, False)
        query = f"player_now('{player_name2}')"
        flag2 = isPlayerInGame(query, player_name2, False)
        if flag1 and flag2:
            query = f"will_eat({player_name1}, {player_name2})"
            willEat(query, player_name1, player_name2)
    elif "какие дополнительные качества есть у игрока" in user_input.lower():
        parts = user_input.split()
        player_name = parts[-1][:-1]
        query = f"player_now('{player_name}')"
        flag = isPlayerInGame(query, player_name, False)
        if flag:
            query = f"findall(Quality, player_qualities({player_name}, Quality), Qualities)"
            findQualities(query, player_name)
    elif "могу ли я жить под водой" in user_input.lower():
        parts = user_input.split()
        player_name = parts[1][:-1]
        query = f"player_now('{player_name}')"
        flag = isPlayerInGame(query, player_name, False)
        if flag:
            query = f"is_underwater('{player_name}')"
            checkUnderwater(query, player_name)
    elif "что обо мне известно" in user_input.lower():
        parts = user_input.split()
        player_name = parts[1][:-1]
        query = f"player_now('{player_name}')"
        flag = isPlayerInGame(query, player_name, False)
        if flag:
            query = f"player_nutricion('{player_name}', Nut)"
            findNutricion(query, player_name)
            query = f"player_interaction('{player_name}', In)"
            findInteraction(query)
            query = f"player_habitat('{player_name}', Hab)"
            findHabitat(query)
    elif "кто играет со мной" in user_input.lower():
        parts = user_input.split()
        player_name = parts[1][:-1]
        query = f"player_now('{player_name}')"
        flag = isPlayerInGame(query, player_name, False)
        if flag:
            query = f"player_now(X)"
            findAllPlayers(query, player_name)

    else:
        uncorrectRequest()

