# coding: utf-8
import os


# ------------------------------------------------------

# for path in os.listdir('.'):
#     print(path, os.path.getsize(path)) # ������ �����

# ------------------------------------------------------

# for path, dirs, files in os.walk('.'): # ��������� �� ������ ������
#     print (path)

# ------------------------------------------------------

#? �������� pid �������� ��������
#print(os.getpid())

# ------------------------------------------------------

# ? ������ � ���������� ���������

PATH = os.environ['PATH']
PATH += ":" + os.path.abspath('.')
os.environ['PATH'] = PATH

print(os.environ['PATH'])

PATH = os.environ['PATH']
PATH += ":" + os.path.abspath('.')
os.environ['PATH'] = PATH

print(os.environ['PATH'])

# ------------------------------------------------------

Big Endian
Little Endian

print(sys.byteorder) # 'big' ��� 'little'

# ------------------------------------------------------

for a in range(10):
    if a > 5:
        print(a)
        # ����� ����� �� ��������� ������

        # sys.exit(0) # ��� ��������

        # quit()
        # exit(0)

# ------------------------------------------------------

if __name__=='__main__':
    import argparse # ������� ��������� ��������� ������

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                       help='an integer for the accumulator')
    parser.add_argument('--hello', dest='hello', action='store',
                       type=str, default='-')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                       const=sum, default=max,
                       help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print(args.accumulate(args.integers))

    print(args.hello)

# ------------------------------------------------------
��������� ����������� �������

'''
x86 - 32   !
x64 - 64    ?  x32,x64
'''

from distutils.util import get_platform


print(get_platform())

import platform
print(platform.architecture())


print(sys.maxsize)


# ------------------------------------------------------
��������� ��������� ��� ����� � ��������� ������
print('-'*10)
print(sys.float_info)


# ------------------------------------------------------
? ������ ��������� � �������

print('getdefaultencoding:', sys.getdefaultencoding())

print('getfilesystemencoding:', sys.getfilesystemencoding())


# ------------------------------------------------------

���-�� �������� � ���������

sys.setrecursionlimit(100000)

print(sys.getrecursionlimit())

import shutil

shutil.copy2('md5_tst.py', 'md5_tst_tst.py') # �������� ����


os.remove('md5_tst_tst.py') # ������� ����


# ------------------------------------------------------

���� ����� �� �������
import glob

print( glob.glob("*.db") )