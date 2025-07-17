#Fill an array of 5 elements from the user, Sort it in descending and ascending orders then display the output.
def asc_des():
    y=[]
    for i in range(5):
        x=int(input("Enter your numbers by order:  "))
        y.append(x)
        ascending_order=sorted(y)
        discending_order=sorted(y, reverse=True)
    print(f'"main list = "{y}')
    print(f'"ascending_order = "{ascending_order}')
    print(f'"discending_order = "{discending_order}')




# Write a program that build a Mario pyramid like below:
def build_right_triangle():
    for i in range(5):
        print(' '*(4-i)+'*'*i)





# Write a program that counts up the number of vowels [a, e, i, o, u]contained in the string.
def Count_Vowels (x):
  x=x.lower()
  vowels="aeiou"
  y=0
  for i in x:
    if (i in vowels):
      y+=1
  print(y)





# Check the email valid
def emailva(email):
    try:
        if '@' in email and '.' in email:
            username, domain = email.split('@')
        else: return False
        if username and domain:
            x,y=domain.split('.')
        else: return False
        if x and y:
            return True
    except:
         return False





# Write a program that prints the locations of "i" character in any string you added.
def Finding_i(x):
  y=1
  for i in x:
    if (i == "i"):
      print(y)
    y+=1 






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








#Write a program that generate a multiplication table from 1 to the number passed.
def special_multiplication_table(x):
     y=1
     while y <= x:
          for i in range(1, y+1, 1):
               print(f"{y}*{i}={y*i}")
          y+=1







# Star pyramids in lists
def Star_Pyramids_In_Lists():
    l =[" "," "," "," "," "]
    for i in range(len(l)-1,-1,-1):
        l[i]="*"
        print(l)



