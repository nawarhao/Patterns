#Take input 
print("Half pyramid pattern of starms (*):")
n = int(input("enter the number of rows: "))
#outer loop to handle number of rows
for i in range(n):
    #inner loop to handle number of colons
    for j in range (i+1):
        #display result
        print("* ", end="")
    print()
    
#Take input from user
rows = int(input("Please enter the total number of rows :"))
number = 1 #initialise by 1

print("Floyd's Triangle")
#outer loop for number of rows
for i in range(1, rows + 1):
    #inner loop for number of columns
    for j in range (1, i+1):
        #display result
        print(number, end= '  ')
        number = number + 1
    print()
    
    #take input from user
rowSize = int(input("enter the number of rows: "))
if rowSize%2==0: #conditions
    halfDiamRow = int(rowSize/2)
else:
    halfDiamRow = int(rowSize/2)+1
space = halfDiamRow-1
    #loop for upper part
for i in range(1, halfDiamRow+1): #loop for rows
    for j in range(1, space+1): #loop for columns
        print(end=" ")
    space = space - 1
    num = 1
    for j in range(2*i-1):
        print(end=str(num))
        #incrementing number at each column
        num = num+1
    print()
    space = 1
    #loop for lower part
for i in range(1, halfDiamRow): #loop for rows
    for j in range(1, space+1): #loop for columns
        print(end=" ")
        space = space+1
        num = 1
    for j in range(1,2*(halfDiamRow-i)):
        print(end=str(num)) #display result
        #incrementing number at each column
        num = num+1
    print()