# ДЕКАРАТОРЫ

# def decorator(function_to_decorate):

	# def new_func():
		# print(u'Я код, который отработает до вызова функции')

		# function_to_decorate() #сама функция
		
		# print (u'А я код срабатывающий после')
	
	# return new_func

# @decorator #можно и вот так, использовать собачку)	
# def func():
	# print('Hello from func')
	
# func = decorator(func)

# func()

##################################################################################################################

# import time
# from datetime import datetime  #чтобы вычислить время

# def decorator(func): #пример добавления вычисления времени

	# def new_func():
		# starttime = datetime.now()

		# func()
	
		# print(u'Время выполнения', datetime.now() - starttime)
	
	# return new_func

# @decorator
# def long_func():
	
	# time.sleep(1.234)

# long_func()S

#####################################################################################################################

 






















