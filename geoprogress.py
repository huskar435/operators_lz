input_data = open('input.txt', 'r')
data = input_data.read()

data = data.split()

b1 = int(data[0])
q = int(data[1])
n = int(data[2])

s = int(b1*(1-q**n)/(1-q))

output = open('output.txt', 'w')
output.write(str(s))

input_data.close()
output.close()
