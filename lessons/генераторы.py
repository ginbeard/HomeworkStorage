# ГЕНЕРАТОРЫ

# lst = [x * 2 for x in range(10)]

# print(slv)

# gen = (x*2 for x in range(100000))  #это генератор

# for a in gen:
	# вычисление значения а
	# if a > 100000 - 10:
	# print(a)


# import os	
	
# students = ['Name', 'Name2', 'Name3']

# gen = (student for student in students) 

# print(next(gen))
# print(next(gen))
# print(next(gen))

# files = (f for f in os.listdir('.'))

# print(next(files))


#УНИВЕРСАЛЬНЫЙ ГЕНЕРАТОР

import sys, os

def find_word_in_file(filename, word):
	if filename.endswith('.txt'):
		for line in open(filename):
			if word in line:
				return filename
	return None

def ask_is_dir(directory, lst, word):
	directory = os.path.abspath(directory)
	# print('directory:', directory)
	if not os.path.isdir(directory):
		raise NotDirectoryError()
	
	for name in os.listdir(directory):
		name = os.path.join(directory, name)
		
		# print('name:', name)
		
		if not os.path.isdir(name):
			finded_file = find_word_in_file(name, word)
			if finded_file:
				lst.append(finded_file)
		else:
			ask_is_dir(name, llst, word)

if __name__ =='__main__': #проверка на то, что запустили как программу

	directory = sys.argv[1] #получаем аргумент запуска програмы
	word = sys.argv[2]
	
	lst = []

	ask_is_dir(directory, lst, word)
	gen = (name for name in lst) #запускаем конструкцию
	for name in gen:
		print(name)


#РАСШИРЕННЫЙ ГЕНЕРАТОР



	
	
	
	
	
	
	

	
	
	

