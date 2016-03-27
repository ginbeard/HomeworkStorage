# Echo client program
import socket

HOST = 'localhost'        # The remote host      127.0.0.1
PORT = 50007              # The same port as used by the server


# ������� ������ ������ (������ ����������)
# - ��� �����, ��� ���������� = TCP + IP, ���������
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ����������� � �������� �� ������ � �����
s.connect( (HOST, PORT) )

# ���������� ������ - ������ ������
s.sendall(b'Hello, world')

# �������� ����� �� �������
# - 1024 - ����������� �� ����������
data = s.recv(1024)

# ��������� �����
s.close()

# ����� �� ����� ���������� ������
print('Received', repr(data))