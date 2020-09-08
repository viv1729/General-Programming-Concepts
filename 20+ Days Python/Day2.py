"""
Question 5:
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.

Also please include simple test function to test the class methods
"""

class ReadDisplay():
    def getString(self):
        self.s = input("Enter String: ")
    
    def printString(self):
        print(f'String in uppercase: {self.s.upper()}')


if __name__ == "__test__":
    read_display = ReadDisplay()
    read_display.getString()
    read_display.printString()


"""
Question 6:
Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2*C*D)/H]

Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:

100,150,180

The output of the program should be:

18,22,24

"""

if __name__ == "__test__":
    C = 50
    H = 30

    arr = map(int, input("enter array: ").split(","))
    ans = [str(round((2*C*i/H)**.5)) for i in arr]

    print(",".join(ans))



"""
Question 7:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j

Note: i=0,1,..,X-1; j=0,1,...,Y-1. Suppose the following inputs are given to the program: 3,5

Then, the output of the program should be:

[[0, 0, 0, 0, 0], 
 [0, 1, 2, 3, 4], 
 [0, 2, 4, 6, 8]]

"""


"""
Not working: Array output is same for all arrays: [[0, 1, 2], [0, 1, 2]]
"""

X,Y = [int(i) for i in input("enter x,y: ").split(",")]

arr = [[0]*Y]*X
for i in range(X):
    for j in range(Y):
        print(i,j,arr[i][j], end=",")
        arr[i][j] = i*j
        print(arr[i][j])

print(arr)
for i in range(X):
    for j in range(Y):
        print(arr[i][j])


# 2d list comprehension
arr = [[i*j for i in range(Y)] for j in range(Y)]
print(arr)



"""
Question 9:
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:

Hello world
Practice makes perfect

Then, the output should be:

HELLO WORLD
PRACTICE MAKES PERFECT
"""

# will only read 1 line from console
arr = input().splitlines()
for s in arr:
    print(s.upper())


# using while
while True:
    x = input()
    if x:
        print(x.upper())
    else:
        break


# using yield, exitmap, and read method
def user_input():
    while True:
        x = input()
        if x:
            # return x won't work as it will return from the user_method() after reading 1 string only
            yield x
        else:
            break

for line in map(str.upper, user_input()):
    print(line)


