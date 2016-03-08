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

# Поиск по условию

while True:
	studentName = input('\n\nВведие имя или фамилию студента:')
	amountNames = 0
	studentsList.sort()
	for searchResult in studentsList:
		name, last_name = searchResult.split(' ')
		if studentName == name or studentName == last_name or searchResult == studentName:
			print(searchResult)