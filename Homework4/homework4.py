# -*- coding: utf-8 -*-

import os							
path = 'F:\\Homework4\\'
fileList = open(path + 'hw2_attachment.txt', 'r+')
studentsList = []

for line in fileList:
	studentsList.append(line[:-1])

def list_sort_print(lst): # функция сортировки
	lst.sort()
	print('*' * 70, '\nТут применилась функция сортировки\n', '*' * 70)
	
def search_func(x, y):  # функция поиска элементов и создания нового списка
	for searchResult in y:
		if quantityNames in searchResult:
			newList.append(searchResult)
	print('*' * 70, '\nТут применилась вторая функция создания нового списка\n', '*' * 70)

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
		list_sort_print(studentsList)
		print('\n\n', studentsList, '\n\n')
		
	elif menu == seekStudent:	#блок поиска студентов по индексам
		list_sort_print(studentsList)
		oldStudent = int(input('\n\nВведите индекс судента в списке:'))
		print('\n\n', studentsList[oldStudent], '\n\n')
		
	elif menu == seekGroup:   #блок поиска студентов по срезу
		list_sort_print(studentsList)
		startList = int(input('\nВведите начало среза:\n'))
		endList = int(input('\nВведите конец среза:\n'))
		print('\n\n', 'Срез от', startList, 'до', endList, studentsList[startList:endList], '\n\n')

	elif menu == seekLetter:    #блок поиска студентов по буквосочетанию
		letters = input('\n\nВведие буквосочетание:')
		amountNames = 0
		list_sort_print(studentsList)
		for searchResult in studentsList:
			if letters in searchResult:
				amountNames += 1
		print('\n\nНайдено', amountNames, 'студентов.\n\n')

	elif menu == seekNames:    #блок поиска студентов с одинаковыми именами и фамилиями
		quantityNames = input('\n\nВведие имя студента:')
		list_sort_print(studentsList)
		newList = []
		search_func(newList, studentsList)
		print('\n\n', newList, '\n\n')
		
	else:
		print('\n\nДо свидания!')
		break
	
	
	

