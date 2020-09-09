import socket
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 40400))
s.listen(1)
c, a = s.accept()

print('connected: ' + str(a))

while True:
    data = c.recv(1024)
    data = data.decode('utf-8')
    if data:
        break

new_data = data.split(' ')
p = int(new_data[0])
q = int(new_data[1])
openExp = int(new_data[2])
print("Получены данные: " + new_data[0] + " " + new_data[1] + " " + new_data[2])

message = random.randint(0, p*q)
c.send(str(pow(message, openExp) % (p * q)).encode('utf-8'))
print("Отправлены данные: " + str(pow(message, openExp) % (p * q)))
c.close()

print("Message is " + str(message))
input("всё")
