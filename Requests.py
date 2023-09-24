import pyswip
from pyswip import Prolog
from IO import playerInGame, playerNotInGame, agressionOutput, eatOutput, notEatOutput, printQualities, \
    underwaterOutput, onWaterOutput, aboutOutput, nutricionOutput, interactionOutput, habitatOutput, allPlayersOutput


def sendQuery(query):
    prolog = Prolog()
    prolog.consult("evolution.pl")
    try:
        results = list(prolog.query(query))
        return [True, results]
    except pyswip.prolog.PrologError:
        print("Ой... вы вводите что-то совсем не то.")
        return [False]


def isPlayerInGame(query, player_name, flag):
    flag2 = True
    results = sendQuery(query)
    if results[0]:
        if flag:
            if results[1]:
                playerInGame(player_name)
            else:
                playerNotInGame(player_name)
        else:
            if not results[1]:
                playerNotInGame(player_name)
                flag2 = False
        return flag2


def countAgression(query, player_name):
    results = sendQuery(query)
    if results[0]:
        if results[1]:
            count = str(results[1][0]["X"])
            agressionOutput(player_name, count)
        else:
            playerNotInGame(player_name)


def willEat(query, player_name1, player_name2):
    results = sendQuery(query)
    if results[0]:
        if results[1]:
            eatOutput(player_name1, player_name2)
        else:
            notEatOutput(player_name1, player_name2)


def checkUnderwater(query, player_name):
    results = sendQuery(query)
    if results[0]:
        if results[1]:
            underwaterOutput(player_name)
        else:
            onWaterOutput(player_name)


def findNutricion(query, player_name):
    aboutOutput(player_name)
    results = sendQuery(query)
    if results[0]:
        if results[1]:
            nutricionOutput(results[1][0]["Nut"])


def findInteraction(query):
    results = sendQuery(query)
    if results[0]:
        if results[1]:
            interactionOutput(results[1][0]["In"])


def findHabitat(query):
    results = sendQuery(query)
    if results[0]:
        if results[1]:
            habitatOutput(results[1][0]["Hab"])


def findAllPlayers(query, player_name):
    results = sendQuery(query)
    if results[0]:
        allPlayersOutput(player_name, results[1])


def findQualities(query, player_name):
    results = sendQuery(query)
    if results[0]:
        printQualities(player_name, results[1])
