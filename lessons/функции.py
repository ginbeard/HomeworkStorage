# ФУНКЦИИ

def add(x, y): #создаем функцию add
	return x + y #складываем и возвращаем
print (add(20, 5))
print (add('Hello ', 'World'))


def newfunc():
	def add(x, y):
	return x + y

	
def func():
	pass #блок кода который ничего не делает
print(func())


def summ(lst):   #функция ссумирования элементов списка
	summa = 0	 #работает с кортежем но с множествами получится конфуз
	for a in lst:	#нельзя складывать разные элементы, число и строку например
		summa += a
	return summa

	
lst = [2,4,6,7,10]
ret = summ(lst)
print(ret)

def some_file_work(text):    #функция записи в файл
	f = open ('rrr', 'a')
	s = '{}\n'.format(text) #вставляем значение text вместо {}
	f.write(s)
	f.close()

some_file_work('Hello')
some_file_work('my name')
some_file_work('is ...')


def func(a,b,c=2):  #с = необязательный аргумент
	return a + b + c
ret = func(10, 20, 30) # если с не задать то берется значение по умолчанию = 2
print(ret)


def debug (*args): #задаем изменяемый tuple аргументов
	print('args len:', len(args))
	for a in args:
		print(a)
	return args
	
debug()
debug(1, 2, 3)
print(debug(1, 2, 3))


def func (**kwarks): #создает dictionary аргументов
	print('имя:', kwargs ['name'])
	return kwarks

func (name='Ivan')


def painting (lenght, wide, letter): #функция рисования линии
	line = ((letter * lenght) + '\n') * wide
	print(line)
painting (20, 3, 'X')
	

add = lambda x, y: x + y
print(add(10, 20))
print((lambda x, y: x + y)(10,20)) #анонимной функции не обязательно давать имя

lst = [
	['Ivan', 'Novikov'],
	['Maria', 'Kozevnikova'],
	['Will', 'Smith']
]

lst.sort(key=lambda lst2: lst2[1])
print(lst)

coef = lambda name, surename: len(name)/len(surename) #считаем отношение имени и фамилии в списках
for name, surename in lst:
	print(name, coef(name, surename))

















