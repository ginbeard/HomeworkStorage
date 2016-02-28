# -*- coding: utf-8 -*-

import os							
pythonCounter = 0					#счетчик
path = 'E:\\Homework1\\'			#путь донужной папки
filelist = os.listdir(path)			#создаем список нужных файлов

for fileName in filelist:					#цикл прохождения по списку файлов
	infile = open(path + fileName, 'r')		#открываем файлы...
	fileContent = infile.read()				#...и читаем их
	for word in fileContent.split():		#цикл прохождения вычитанного текста с разделением по пробелу на слова
		if word.lower() == 'python':		#если проверяемое и приведенное к нижнему регистру слово = python...
			pythonCounter += 1				#...добавляем к счетчику +1
print(pythonCounter)						#печатаем результат

result = open('E:\\Homework1\\hw1_result.txt', 'w')  #создаем файл для записи результата
result.write(str(pythonCounter))					 #записываем результат
