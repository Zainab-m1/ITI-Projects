
def special_multiplication_table(x):
     y=1
     while y <= x:
          for i in range(1, y+1, 1):
               print(f"{y}*{i}={y*i}")
          y+=1

n = int(input('Enter a number:  '))
special_multiplication_table(n)