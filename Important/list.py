# со списком выполняются все операции как и со строками
# cписок может модержать вложенный список


s = list('список')
print(s)

lst = ['s', 'p', ['isok', 5, 6, 5], 2, 'p']

print(lst[0])
print(lst.count('p'))

lst.append('TTT') #добавляет элемент в конец списка
lst.insert(3, 'ZZZ') #добаляет элемент в указанное место

lst.remove('p') #удаляет первое вхождение элемента
lst.pop(3) #удаление по индексу







