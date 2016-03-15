# coding: utf-8

import random, time

class Tank:
	
	def __init__(self, name, attack = 10, mobility = 10, hitpoints = 10):
		self.name = name
		self.attack = attack
		self.mobility = mobility
		self.hitpoints = hitpoints
		
	def show_stats(self):
		print('-' * 50, '\n', self.name, '\n', '\n Attack=', self.attack, 'Mobility=', self.mobility, 'Hitpoints=', self.hitpoints, '\n\n\n')
			
	def shot(self, enemy_tank):
		
		shot = random.randint(1, 100)
		
		if shot > (self.attack - enemy_tank.mobility):
			print('*' * 20, self.name, 'missed!')
		else:
			if (enemy_tank.hitpoints - self.attack) > 0:
				enemy_tank.hitpoints -= self.attack
				print('*' * 20, enemy_tank.name, 'got', self.attack, 'damage')
			else:
				enemy_tank.hitpoints -= self.attack
				print('*' * 20, enemy_tank.name, 'destroyer!!!') 
				alltanks.remove(target_tank)
	
	
class L_tank(Tank):
	def __init__(self, name):
		super().__init__(name, attack = 50, mobility = 30, hitpoints = 100)
		
class M_tank(Tank):
	def __init__(self, name):
		super().__init__(name, attack = 70, mobility = 20, hitpoints = 200)
				
class H_tank(Tank):
	def __init__(self, name):
		super().__init__(name, attack = 90, mobility = 10, hitpoints = 300)	

		
light_tank = L_tank('light_tank')
medium_tank = M_tank('medium_tank') 
heavy_tank = H_tank('heavy_tank')

alltanks = [light_tank, medium_tank, heavy_tank]

battle = 1
turn_counter = 0
chooseLT = '1'
chooseMT = '2'
chooseHT = '3'

newgame = input('\n\n For start game press any key\n\n')

while battle:

	while True:
		active_tank = random.choice(alltanks)
		target_tank = random.choice(alltanks)
		if active_tank == target_tank:
			pass
		else:
			turn_counter += 1
			time.sleep (3)
			print('*' * 20, 'TURN № ', turn_counter, '\n')
			print('*' * 20, active_tank.name, 'makes the shot at the', target_tank.name, '!!!', '\n')
			break

	active_tank.shot(target_tank)
	
	for stats in alltanks:
		stats.show_stats()
	
	if len(alltanks) is 1:
		print('*' * 20, active_tank.name, 'has won!!!')
		break
		
		
		