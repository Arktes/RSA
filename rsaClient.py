import socket

def isPrime(n):
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 40400))
data = input("Введите p, q: ")
data = data.split(' ')
p = int(data[0])
q = int(data[1])
n = p * q
fi = (p - 1) * (q - 1)

j = 3
while j < fi:
    if (isPrime(j) and fi % j != 0):
        e = j
        break
    j += 1

data.append(str(e))
privateExp = 0
d = 1
while True:
    if ((d*e)%fi==1):
        privateExp = d
        break
    d += 1

data = ' '.join(data)
data = data.encode('utf-8')
s.send(data)
print("Отправленные данные: " + str(p) + " " + str(q) + " " + str(e))

data = s.recv(1024)
coded_m = int(data.decode('utf-8'))
print("Получены данные: " + str(coded_m))
message = pow(coded_m, privateExp) % n
s.close()

print("Message is " + str(message))
input("всё")
