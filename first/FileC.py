file = open("first.txt", 'w')
file.write('this is it')
file.close()

read = open("first.txt", 'r')
print(read.read( ))
