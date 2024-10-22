input_data = open('input.txt', 'r')
data = input_data.read()

data = data.split()

n = int(data[0])
k = 0

while n != 0:
    if n%3 == 0:
        n -= 3

    elif n%3 == 1:
        n -= 1

    elif n%3 == 2:
        n -= 2

    k += 1

output = open('output.txt', 'w')
output.write(str(k))

input_data.close()
output.close()