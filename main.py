import re
from tqdm import tqdm
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("input", help='Введите путь к файлу с данными для обработки')
parser.add_argument("output", help='Введите путь куда сохранить обработанные данные')
args = parser.parse_args()


class Validator:
    """
    Класс валидатор
    Проверка данных на валидность
    """

    # конструктор класса
    def __init__(self):
        pass

    def check_email(email: str) -> bool:
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

    def check_weight(weight: int) -> bool:
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
        if type(weight) == int:
            if weight < 130:
                return True
        return False

    def check_snils(snils: str) -> bool:
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

    def check_passport_number(passport_number: int) -> bool:
        """
        Выполняет проверку номера паспорта на корректность
        Если номер паспорта состоит не из 6 цифр то возвращается False

            Parameters
            ----------
                passport_number : int
                  Параметр для проверки

            Returns
            -------
                bool:
                    Булевый результат проверки на корректность
        """

        a = f'{passport_number}'
        if len(a) != 6:
            return False
        return True

    def check_string(string) -> bool:
        """
        Выполняет проверку типа данных параметра
        Если пераметр не имеет тип данных str возвращено False

            Parameters
            ----------
                string : str
                  Параметр для проверки типа данных

            Returns
            -------
                bool:
                    Булевый результат проверки на корректность
        """
        if type(string) != str:
            return False
        return True

    def check_age(age: int) -> bool:
        """
        Выполняет проверку возраста на корректность
        Если возраст превышает отметку в 100 то возвращается False

            Parameters
            ----------
                age : int
                  Параметр для проверки

            Returns
            -------
                bool:
                    Булевый результат проверки на корректность
        """
        if type(age) == int:
            if age < 100:
                return True
        return False

    def check_address(address: str) -> bool:
        """
        Выполняет проверку корректности адреса
        Если адрес не является строкой или указан не в формате "улица пробел номер дома" то возвращено False

            Parameters
            ----------
                address : str
                  Параметр для проверки

            Returns
            -------
                bool:
                    Булевый результат проверки на корректность
        """
        pattern = '[а-яА-Я.\s\d-]+\s+[0-9]+$'
        if type(address) == str:
            if re.match(pattern, address):
                return True
        return False


# считывание данных из файла с заданием в виде списка словарей
data = json.load(open(args.input, encoding='windows-1251'))

# переменные для подсчета статистики обработанных данных
true_data = list()
email = 0
weight = 0
snils = 0
passport_number = 0
university = 0
age = 0
political_views = 0
worldview = 0
addsress = 0

# Валидация данных с прогрессбаром
with tqdm(total=len(data)) as progressbar:
    for person in data:
        temp = True
        if not Validator.check_email(person['email']):
            email += 1
            temp = False
        if not Validator.check_weight(person['weight']):
            weight += 1
            temp = False
        if not Validator.check_snils(person['snils']):
            snils += 1
            temp = False
        if not Validator.check_passport_number(person['passport_number']):
            passport_number += 1
            temp = False
        if not Validator.check_string(person["university"]):
            university += 1
            temp = False
        if not Validator.check_age(person['age']):
            age += 1
            temp = False
        if not Validator.check_string(person['political_views']):
            political_views += 1
            temp = False
        if not Validator.check_string(person['worldview']):
            worldview += 1
            temp = False
        if not Validator.check_address(person['address']):
            addsress += 1
            temp = False
        if temp:
            true_data.append(person)
        progressbar.update(1)

# запись валидных данных в новый файл
out_put = open(args.output, 'w', encoding='utf-8')
result_data = json.dumps(true_data, ensure_ascii=False, indent=4)
out_put.write(result_data)
out_put.close()

print("Число валидных записей: ", len(true_data))
print("Число невалидных записей:", len(data)-len(true_data))
print("\nСтатистика невалидных записей по типам ошибок: ")
print("Email: ", email)
print("Weight: ", weight)
print("Snils: ", snils)
print("Passport number: ", passport_number)
print("University: ", university)
print("Age: ", age)
print("Political view: ", political_views)
print("Worldview: ", worldview)
print("Address: ", addsress)

# python main.py D:\\73.txt D:\\test.txt
