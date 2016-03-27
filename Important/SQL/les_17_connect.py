# coding: utf-8
import sqlite3


class ExampleConnect:


    def __init__(self):
        # ��������� ��� ������� ����
        self.__conn = sqlite3.connect('example.db')

        # ������� ������ - ����� ������� � ������� ��
        self.__cursor = self.__conn.cursor()


    def __del__(self):
        # ����������

        print('��������� ����������...')

        # �������� ����������
        self.__conn.close()


    def select(self):
        '�������� ���������'
        for row in self.__cursor.execute("SELECT * FROM students"):
            print(row)


    def create(self):
        '''
        �������� ���� ������
        :return: None
        '''

        self.__create_table('students')
        self.__create_table('books')

        # ���������� ������
        #self.__cursor.execute("INSERT INTO students VALUES (0, 'Ivan', '1980-01-05')")
        #self.__cursor.execute("INSERT INTO students VALUES (1, 'Mariya', '1985-03-15')")

        # ��������� ������� ������
        self.__cursor.executemany("insert into students values (?, ?, ?)", [
            (0, 'Ivan', '1980-01-05'),
            (1, 'Mariya', '1985-03-15')
        ])

        self.__conn.commit()

    def update_Mariya(self):
        self.__cursor.execute("UPDATE students set name=? where name=?", ('Masha', 'Mariya'))

        # ��������� ��������� � ��
        self.__conn.commit()


    def __create_table(self, table_name):

        try:
            # ������� �������
            self.__cursor.execute('CREATE TABLE {} (id INTEGER, name text, date text)'.format(
                table_name))

            # ��������� ��������� � ��
            self.__conn.commit()

            print('create {}...'.format(table_name))

        except ImportError: #sqlite3.OperationalError:
            pass



if __name__=='__main__':

    connect = ExampleConnect()

    print(connect.select.__doc__)
    print(connect.create.__doc__)
