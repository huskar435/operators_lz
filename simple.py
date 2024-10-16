input_data = open("input.txt","r")
data = input_data.read()
data = data.split()
a = int(data[0])
for i in range(1,25):
    if  (i <1) and (a % i == 0):
        a = ("N")
else:
    a = ("Y")
output_data = open("output.txt","w")
output_data.write(a)
input_data.close()
output_data.close()  
