import csv


def load_csv_list() -> list:
    """
    загрузка данных из csv файла
    :return: список нужного формата
     """
    csv_list = []
    with open("../src/items.csv", encoding="CP1251") as csv_file:
        take_csv_data = csv.reader(csv_file, delimiter=",")
        count = 0
        for roe in take_csv_data:
            if count != 0:
                csv_list.append(roe)
            count += 1
    return csv_list