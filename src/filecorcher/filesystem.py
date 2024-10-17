import os
import logging
import datetime
import re

def numfixlen(num, L):
    """Установка символьной длины целого числа

        Args:
        num (str): Исходное число
        L (int[]): Необходимая длина числа

    """
    while len(num) < L:
        num = "0" + num
    return num

def getnewname(name, pattern, counter = 0):
    """Вычисления нового имени файла по паттерну

        Args:
        name (str): Исходное имя файла
        pattern (str): Паттерн нового имени
        counter (int, optional): Счётчик файла. Defaults to 0

    """
    newname = ""
    for i in pattern:
        if "<counter>" in i:
            #print(int(i[6:]))
            newname = newname + numfixlen(str(counter), int(i[9:]))
        elif i == "<filename>":
            newname = newname + name
        else:
            newname = newname + i
    newname[len(newname)-1]
    return newname


    

def rename(path, pattern="filename", filter = "*", sortedkey = '', writelog = True):
    """Переименовывания набора файлов\директорий по паттерну

        Args:
        path (str): Путь к директории с файлами
        pattern (str, optional): Паттерн для нового имени файлов. Defaults to "filename".
        filter (str, optional): Фильтр типа объектов переименовывания. Defaults to '*'.
        #TODO РЕАЛИЗОВАТЬ МЕТОД СОРТИРОВКИ
        sortedkey (str, optional): Ключевой параметр сортировки файлов. Defaults to ''.

    """
    if path[len(path)-1] != '/':
        path = path + "/"
    operationname = path + "rename_" + datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    if writelog:
        logging.basicConfig(level=logging.INFO, filename= path + operationname + "/" + operationname + ".log", filemode="w")
    if filter == "directory":
        logging.info("Filter: directory")
        dirlist = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
        logging.info("Create folders name list")
    else:
        dirlist = []
        logging.info("Filter: files with format {filter}")
        alldirlist = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        logging.info("Create all files name list")
        for i in range(len(alldirlist)):
            if (re.fullmatch(".*\."+filter, alldirlist[i])):
                dirlist.append(alldirlist[i])
        logging.info("File names filtered. Selected files: {len(dirlist)}")
    counter = 0
    #TODO РЕАЛИЗОВАТЬ МЕТОД СОРТИРОВКИ
    #dirlist.sort(key=sortedkey)
    logging.info("Starting rename")
    for name in dirlist:
        newname = getnewname(name, pattern, counter)
        logging.info(name + '\t' + "=>" + '\t' + newname)
        os.rename(path + "/" + name, path + "/" + newname)
        counter = counter + 1