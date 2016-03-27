-*- coding: utf-8 -*-

print('{0}, {1}, {2}'.format('a', 'b', 'c')) # это все форматы

print('{0}, {1}, {2}'.format(*'abc')) 

print('Coorditanes: {latitude}, {longitude}'.format(latitude='37.24N', longitude='115,81W'))

print('{:+f}; {:-f}'.format(3.14, -3,14))

forbsList = [
			['Barak', 'Obama', 100.1413, 0.1],
			['Angela', 'Merkel', 200.14314, 0.2],
			['Tony', 'Blar', 300.3424, 0.3],
			['Bashar', 'Asad', 400.2342, 0.4],
			['Tom', 'Cruse', 500.2342, 0.5]
			]

for person in forbsList:
	print('{0:<10}|{1:<10}|{2:>10.2f}|{3:^10.2%}'.format(*person))


lst_1 = ['Bill', 'Monica', 'Yura']
dict_1 = {'Bill':5, 'Monica':6, 'Yura':7}
lst_2 = [1, 2, 17]

for x, y in zip(dict_1.values(), lst_2): # ZIP объединяет 2 итерируемых объекта поэлементно в кортеж
		print(x, y)

enumrate # добавляет порядковый номер элементу
		
lst_1 = [1, 2, 3, 4]
lst_2 = [1, 2, 3, 10]

print(list(map(pow, lst_1, lst_2))) # применяет функцию ко всем попарным элементам

num = 0xff
print(bin(num)[2:])


import itertools
for index, a in enumerate(itertools.count(10, step=1)):
	print(a)

	if index > 10:
		break


import itertools
for i, a in enumerate(itertools.cycle('ABCD')):
	print(a)
	
	if i > 10:
		break





