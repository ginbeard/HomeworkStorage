# coding: utf-8


import pickle

studentsList = ['Сергей Иванов', 'Петр Аваков', 'Илья Муромец', 'Василий Соловьев',
				'Сергей Гринн', 'Илья Бринн', 'Денис Кузьмин', 'Инна Горохова', 'Анна Валишевская',
				'Илья Пупки', 'Сергей Табуреткин', 'Василий Теркин', 'Анна Посаженникова', 'Егор Буров',
				'Алексей Гремящий', 'Андрей Краснов']

storageFile = 'storage.data'    # создаем переменную с именем файла, куда сохраним список студентов 

file = open(storageFile, 'wb')   # открываем файл для записи...
pickle.dump(studentsList, file)  # ... пишем
file.close()				     # ... закрываем

del studentsList    # удаляем переменную из памяти

fileNew = open(storageFile, 'rb')    # открываем файл
studentsList = pickle.load(fileNew)  # вычитываем в переменную
print('\n', studentsList, '\n') 	 # печатаем



import csv

with open('file.csv', 'w', newline='') as csvfile:   # пишем список студентов в csv
	writer = csv.writer(csvfile, delimiter=' ', quotechar="'", quoting=csv.QUOTE_MINIMAL)
	writer.writerow(studentsList)
	
with open('file.csv', 'r') as csvfile:  # читаем его от туда
		reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in reader:
			print(', '.join(row))
	
	
		
import json

jsonStudents = json.dumps(studentsList) # преобразуем в формат json

listFromjson = json.loads(jsonStudents) # преобразуем обратно

print('\n', listFromjson, '\n')    # печатаем



















