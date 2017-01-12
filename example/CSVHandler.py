# -*- coding:utf-8 -*-
from urllib.request import urlopen
from io import StringIO
import csv
data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii','ignore')
dataFile = StringIO(data)
# csvReader = csv.reader(dataFile)
# for row in csvReader:
# 	print(row)
dictReader = csv.DictReader(dataFile)
print(dictReader.fieldnames)
for row in dictReader:
	print(row)