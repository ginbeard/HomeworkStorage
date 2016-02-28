# -*- coding: utf-8 -*-

import os							
path = 'E:\\Homework2\\'
fileList = open(path + 'hw2_attachment.txt', 'r+')
studentsList = []

for line in fileList:
	studentsList.append(line[:-1])

cycle = True
	
while cycle:	#цикл на меню
	menu = input('Введите 1 для добавления студента в список.\n\
Введите 2 для поиска студента по индексу.\n\
Введите 3 для поиска студентов по срезу.\n\
Введите 4 для вывода количесва студентов с буквосочетанием "n".\n\
Введите 5 для создания списка студентов с одинаковыми именами.\n\
Введите любой символ для выхода из программы.\n\n\
Ввод:')
	addStudent = '1'    #переменные пунктов меню
	seekStudent = '2'
	seekGroup = '3'
	seekLetter = '4'
	seekNames = '5'
	exitProgram = '6'

	if menu == addStudent:	 #блок добавления нового студента
		newStudent = input('\n\nВведите имя и фамилию нового судента:')
		studentsList.append(newStudent)
		fileList = open(path + 'hw2_attachment.txt', 'a')
		fileList.write(newStudent)
		fileList.write('\n')
		studentsList.sort()
		print('\n\n', studentsList, '\n\n')
		
	elif menu == seekStudent:	#блок поиска студентов по индексам
		studentsList.sort()
		oldStudent = int(input('\n\nВведите индекс судента в списке:'))
		print('\n\n', studentsList[oldStudent], '\n\n')
		
	elif menu == seekGroup:   #блок поиска студентов по срезу
		studentsList.sort()
		startList = int(input('\nВведите начало среза:\n'))
		endList = int(input('\nВведите конец среза:\n'))
		print('\n\n', 'Срез от', startList, 'до', endList, studentsList[startList:endList], '\n\n')

	elif menu == seekLetter:    #блок поиска студентов по буквосочетанию
		quantityLetters = input('\n\nВведие буквосочетание:')
		amountNames = 0
		studentsList.sort()
		for searchResult in studentsList:
			if quantityLetters in searchResult:
				amountNames += 1
		print('\n\nНайдено', amountNames, 'студентов.\n\n')

	elif menu == seekNames:    #блок поиска студентов с одинаковыми именами и фамилиями
		quantityNames = input('\n\nВведие имя студента:')
		studentsList.sort()
		searchResultList = []
		for searchResult2 in studentsList:
			if quantityNames in searchResult2:
				searchResultList.append(searchResult2)
		print('\n\n', searchResultList, '\n\n')
		
	else:
		print('\n\nДо свидания!')
		break
	
	
	

