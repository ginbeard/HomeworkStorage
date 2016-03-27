# coding: utf-8
import sqlite3

# ��������� ��� ������� ����
conn = sqlite3.connect('example.db')

# ������� ������ - ����� ������� � ������� ��
c = conn.cursor()


# ��������� ������ SQL
conn.executescript('''
CREATE TABLE students (id INTEGER, name text, date text);
CREATE TABLE books (id INTEGER, name text, date text);
INSERT INTO students VALUES (0, 'Ivan', '1980-01-05');
INSERT INTO students VALUES (1, 'Mariya', '1985-03-15');
''')



try:
    # ������� �������
    c.execute('CREATE TABLE students (id INTEGER, name text, date text)')

    # ��������� ��������� � ��
    conn.commit()

    print('create students...')

except sqlite3.OperationalError:
    pass


try:
    # ������� �������
    c.execute('CREATE TABLE books (id INTEGER, name text, date text)')

    # ��������� ��������� � ��
    conn.commit()

    print('create books...')

except sqlite3.OperationalError:
    pass


# ����� ������ �� �������
#cur = c.execute("SELECT * FROM students")

# ����� 1-�� ������ (������) �� �������
#print(c.fetchone())

# �������� ���������� ������� � �������
#print('rowcount:', cur.rowcount, 'description:', cur.description)



# ���������� ������
c.execute("INSERT INTO students VALUES (0, 'Ivan', '1980-01-05')")

c.execute("INSERT INTO students VALUES (1, 'Mariya', '1985-03-15')")




conn.commit()


# ��������� ����������
conn.close()