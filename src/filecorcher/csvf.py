import os
import logging
import datetime
import pandas as pd

def sepcol(path, filename, sepcols, freezecols = [], separator = ";", encoding = "utf-8", writelog = True):
    """Разделение таблицы на несколько таблиц по колонкам

        Args:
        data (pd.DataFrame): Входные данные - таблица для обработки
        sepcols (int[]): Индексы столбцов, которые необходимо разделить по файлам
        freezecols (int[], optional): Индексы столбцов, которые необходимо сохранить в каждом файле. Defaults to [].
        separator (str, optional): Разделитель столбцов. Defaults to ";".
        encoding (str, optional): Кодировка файла. Defaults to "utf-8".
        writelog (bool, optional): Флаг записи логов в файл. Defaults to True.

    """
    if path[len(path)-1] != '/':
        path = path + "/"
    operationname = "sepcol_" + datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    os.makedirs(operationname)
    print()
    logging.basicConfig(level=logging.INFO, filename= path + operationname + "/" + operationname + ".log", filemode="w")
    logging.info("Opening file [" + path + filename + "]")
    try:
        data = pd.read_csv(path+filename, encoding=encoding, sep=separator)
    except:
        logging.error("Error opening file")
    else:
        logging.info("File opened successfully")
    res = []
    logging.info("Start separating")
    input_columns = '[' + ''.join(data.columns) + ']'
    logging.info("Input file with columns " + input_columns)
    for i in range(len(sepcols)):
        ind = freezecols.copy()
        ind.append(sepcols[i])
        res.append(data.iloc[:,ind])
        sep_columns = '[' + ''.join(data.columns[ind]) + ']'
        logging.info("Create new file with columns " + sep_columns)
        try:
            res[i].to_csv(path + operationname + "/" + str(i)+".csv", sep=separator, index=False)
        except:
            logging.error("Error creating file")
        else:
            logging.info("File created successfully [" + path + operationname + "/" + str(i)+".csv" + "]")