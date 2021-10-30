import re
from tqdm import tqdm
import time
import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument("input", help='Get path file input')
parser.add_argument("output", help='Get path file output')
args = parser.parse_args()


class Validator:
    """
    Класс валидатор
    Проверка данных на валидность
    """

    # конструктор класса
    def __init__(self):
        pass

    def check_email(email : str) -> bool:
        """
        Выполняет проверку корректности адреса электронной почты
        Если в строке присутствуют пробелы, запятые, двойные точки,
        а также неверно указан домен адреса, то будет возвращено False.

        Parameters
        ----------
            email : str
              Строка с проверяемым электронным адресом

        Returns
        -------
            bool:
              Булевый результат проверки на корректность
        """
        pattern = "^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern, email):
            return True
        return False

    def check_weight(weight : int) -> bool:
        """
        Выполняет проверку корректности веса
        Если вес выходит за пределы разумного возвращается False

        Parameters
        ----------
            weight : int
              Параметр для проверки

        Returns
        -------
            bool:
              Булевый результат проверки на корректность
        """

        if int(weight) < 130:
            return True
        return False

    def check_snils(snils : str)-> bool:
        """
        Выполняет проверку номера снилса на корректность
        Если номер снилса не содержит 11 цифр то возвращается False

        Parameters
        ----------
            snils : str
              Строка для проверки

        Returns
        -------
            bool:
              Булевый результат проверки на корректность
        """
        if len(snils) != 11:
            return False
        return True

    def check_passport_number(passport_number : int) -> bool:
        if passport_number != 6:
            return False
        return True

    def check_string(string) -> str:
        if type(string) != str:
            return False
        return True

    def check_age(age : int) -> bool:
        if type(age) == int:
            if age < 100:
                return True
        return False

    def check_address(address : str) -> bool:
        pattern = '[а-яА-Я.\s\d-]+\s+[0-9]+$'
        if type(address) == str:
            if re.match(pattern, address):
                return True
        return False

