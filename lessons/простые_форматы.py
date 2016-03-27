 # ПРОСТЫЕ ФОРМАТЫ
 
 # Создаем 2 функции
 # 1-я пишет в csv список списков
 # 2-я чтение из csv этих списков
 
import csv, random

with open('eggs.csv', 'w') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',',	quotechar='|', quoting=csv.QUOTE_MINIMAL)
	spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
	spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

with open('eggs.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in spamreader:
			print(', '.join(row))


РЕШЕНИЕ
			
def list_generator(cols, rows):
	return[ [str(random.randint(0, 9)) for i in range(cols)] for j in range(rows) ]
	
def print_list(lst):
	for row in lst:
		print(*row, sep=', ')

def write_csv(filename, lst):		
	with open(filename, 'w', newline='') as csvfile:
		writer = csv.writer(csvfile, delimiter=DELIMETR,
							quotechar=QUOTECHAR, quoting=QUOTE)
		for row in lst:
			writer.writerow(row)

def read_csv(filename):
	with open(filename, newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter=DELIMETR, quotechar=QUOTECHAR)
		return [row for row in reader]
		
def main():
	lst = list_generator(5, 5) # генерируем таблицу
	write_csv('filename.csv', lst) # записываем
	lst = read_csv('filename.csv') # читаем обратно
	
	print_list(lst) # выводим на экран

	
if __name__=='main':
	main()

########################################################################################################################

import json

lst = ['foo', {'bar': ('baz', None, 1.0, 2)}]

line = json.dumps(lst) # преобразует в формат json

print(line)

lst2 = json.loads(line) # преобразует обратно

print('lst2:', lst2) 


Имя и пароль записываем в json 
Получает на вход json и проверяет авторизацию пользователя, отвечает True or False

def write_user():  
	login = input('login:')
	
	password = input('password:')
	
	d = {login: password}
	
	return json.dumps(d)
	
def check_user(json_string):
	right_users = {'Alex': '1234', 'Masha': 'ghghg'}

	d = json.loads(json_string)
	name = list(d.keys())[0]
	if name in right_users:
		if d[name] == right_users[name]:
			return True
	else:
		print('Invalid user name')
	return False

print(check_user(write_user()))
	
#######################################################################################################################

XML

import xml.etree.ElementTree as ET
root = ET.fromstring(xml) # получаем корневой элемент

for child in root:
	print(child.tag, child.attrib)
	for ch2 in chld:
		if ch2.text is not None:
			print(ch2.tag, ch2.text)
		else:
			print(ch2.tag, ch2.attrib)


	
	
	
	
	
	
	
	
	
	
	
	