input_data = open("input.txt","r")
data = input_data.read()
data = data.split()
a = 0
b = int(data[0])
q = int(data[1])
n = int(data[2])
for a in range(1,1000):
    if ((b *(1 - (q ** n))) / ( 1- q)) == a:
     str(a)
output_data = open("output.txt","w")
output_data.write(str(a))
input_data.close()
output_data.close()   
