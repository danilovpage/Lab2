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

        pattern = '[1-130]'
        if int(weight) < 130:
            return True
        return False
