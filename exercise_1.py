input1= str(input("Enter a string: "))
output=""
for i in range(len(input1)-1,-1,-1):
    output+=input1[i]
print(output)