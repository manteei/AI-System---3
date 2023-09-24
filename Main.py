from pyswip import Prolog

from Requests import isPlayerInGame
from IO import greeting
from Parse import parser

def main():
    greeting()
    while True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        user_input = input("Введите ваш запрос: ")
        if parser(user_input) == 0:
            break


if __name__ == "__main__":
    main()
