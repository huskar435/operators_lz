input_data = open("input.txt","r")
data = input_data.read()
data = data.split()
a = int(data[0])
for i in range(1,100000):
    a