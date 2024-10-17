import pandas as pd
import csvf
import filesystem as fs
import logging
import datetime
import os
writelog = True

path = "C:/Users/Антон/filecorcher/test"
filename = "test.csv"
csvf.sepcol(path, filename, [2, 3, 4], [0, 1], encoding="windows-1251")

path = "C:/Users/Антон/filecorcher/test/testfolder"
pattern = ["<counter>3", "_", "<filename>"]
print(fs.rename(path, pattern, "directory", writelog=writelog))