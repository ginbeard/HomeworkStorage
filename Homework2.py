# -*- coding: utf-8 -*-

import os							
path = 'E:\\Homework2\\'
fileList = open(path + 'studentsFile.txt', 'r+')
studentsList = []

for line in fileList:
	studentsList.append(line[:-1])

menu = input('Введите 1 для добавления студента в список.\n\
Введите 2 для поиска студента по индексу.\n\
Введите 3 для поиска студентов по срезу.\n\
Введите 4 для вывода количесва студентов с буквосочетанием "n".\n\
Введите 5 для создания списка студентов с одинаковыми именами.\n\
Введите любой символ для выхода из программы.\n\
Ввод:')

addStudent = '1'
seekStudent = '2'
seekGroup = '3'
seekLetter = '4'
seekNames = '5'
exitProgram = '6'

if menu == addStudent:
	newStudent = input('Введите имя и фамилию нового судента:')
	studentsList.append(newStudent)
	fileList = open(path + 'studentsFile.txt', 'a')
	fileList.write(newStudent)
	fileList.write('\n')
	studentsList.sort()
	print(studentsList)
	
elif menu == seekStudent:
	studentsList.sort()
	oldStudent = int(input('Введите индекс судента в списке:'))
	print(studentsList[oldStudent])
	
elif menu == seekGroup:
	studentsList.sort()
	startList = int(input('Введите начало среза:\n'))
	endList = int(input('Введите конец среза:\n'))
	print('Срез от', startList, 'до', endList, studentsList[startList:endList])

elif menu == seekLetter:
	quantityLetters = input('Введие буквосочетание:')
	amountNames = 0
	studentsList.sort()
	for searchResult in studentsList:
		if quantityLetters in searchResult:
			amountNames += 1
	print(amountNames)

elif menu == seekNames:
	quantityNames = input('Введие имя студента:')
	studentsList.sort()
	searchResultList = []
	for searchResult2 in studentsList:
		if quantityNames in searchResult2:
			searchResultList.append(searchResult2)
	print(searchResultList)
	
else:
	print('До свидания!')
