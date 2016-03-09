# -*- coding: utf-8 -*-

# Андрей привет. Я понимаю что это гавнокод, но специально ничего править не стал.
# Писал одним глазом, вторым смотрел на морской бой. Выкладываю как есть.
# Будет время сделаю его красивым, самому интересно.

import random, time

x = 'f e  4   $   #   g U   > @   #   4&* lk   h   c   Y  u ? . < . , > ? ##'
lencount = 78
result = ''

while True:
	for result in x:
		while lencount > 0:
			lencount -= 1
			a = random.choice(x)
			result += a
		time.sleep(0.04)
		print(result)
		lencount += 78

