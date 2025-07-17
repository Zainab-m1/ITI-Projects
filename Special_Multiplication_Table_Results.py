# Write a program that generate a multiplication table from 1 to the number passed.
# If the input is 3, the output is [[1], [2, 4], [3, 6, 9]]


def list_multiplication_table(x):
    l1=[]
    for i in range(1,x+1):
        l2=[]
        for j in range(i,(i*i)+i,i):
            l2.append(j)
        l1.append(l2)
        del l2
    print(l1)

n=int(input("Enter your number:  "))
list_multiplication_table(n)
