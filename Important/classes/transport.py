class Transport:

    index = 0

    def __init__(self, speed = 0, wheel_count = 0, mass = 0, color = (0, 0, 0)):
        self.index = Transport.index = Transport.index + 1
        self.speed = speed
        self.wheel_count = wheel_count
        self.mass = mass
        self.color = color
        self.pos = 0

    def drive(self, time):
        self.pos += self.speed * time

    def show_pos(self):
        print(self, ':', self.pos)

    def crash(self, o):
        print(u'�����������:', self.index, u'�', o.name)
        self.pos = 0
        o.pos = 0

    def fire(self, o):
        pass

    # ��� ������ �� ����� � ������� ������� ������
    def __str__(self):
        return '{}-{}'.format(self.__class__.__name__, self.index)

    # ��� ������ �� ����� (��� ������) � ������� ������
    def __repr__(self):
        return 'R:'+self.__str__()