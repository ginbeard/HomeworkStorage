import random

from airplane import Airplane

from car import Car

from tank import Tank


machines = [
    Car(),
    Car(),
    Car(),
    Tank(),
    Airplane(),
    Airplane(),
]


for m in machines:
    m.show_pos()


for m in machines:
    time = random.randint(1, 150)
    m.drive(time)

for m in machines:
    m.fire(random.choice(machines))


print('-'*20)

for m in machines:
    m.show_pos()

print('-'*20)

print(machines)


print(machines[0].__dict__)

for name in Car.__dict__:
    print(name, ':', Car.__dict__[name])


print(Car.__bases__)