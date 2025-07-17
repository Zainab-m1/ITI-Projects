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




# You are given a list of email addresses in the format username@domain.
# Your task is to use the map() function along with a lambda expression to extract only the domain part from each email address.

def domain(p):
    return(set(map(lambda x: x.split("@").pop(1), p)))





# Names & Emails Validation
def emails_names_validation():
    x=input("Enter your name : ")
    for l in range (5):
            if not (x.isalpha() and (x[0]!=" " and len(x)!=1)):
                print("enter your name again: ")
                x=input("enter your name : ")
    else:
        exit

    for d in range (5):
        y=input("enter your email : ")
        try:
            v=y.strip()
            w=v.split("@")
            if (len(w)!=2 and not(w[0][0].isalpha())):
                exit
            elif len(w)==2: 
                e=w[1].split('.')
                p=["com","."]
            if not (e[0] in p and len(e[0])<2 and len(e[1])<2):
                exit 
            else:
                break  
        except:
            print ("Unvalid email!") 
            break
    else:
        print("your name is "+ x)
        print("your email is "+ y)        
        






# Check name & password in an existing list
def name_pass(p,x):
    n=0
    for i in p:
        if i["name"] != x and n==len(p)-1:
                print("Not valid")
                exit()
        elif i["name"].lower != x.lower and n<len(p)-1:
            n+=1
        else:
            y=input("What is your Pass?  ")
            n=0
            for t in p:
                if t["pass"] != y and n==len(p)-1:
                        print("Not valid")
                        exit()
                elif t["pass"] != y and n<len(p)-1:
                    n+=1
                else:
                    print ("Valid Account")
                    exit()
            




#You are given a list of email addresses, some of which are invalid.
# Your task is to use the filter() function to return only the valid email addresses.
def valid_email(email):
    b=c=0
    v=email.strip()
    for i in range(len(v)):
         if v[i]=="@": b=i
         if v[i]==".": c=i
         if (c-b)>2 and b!=0 and v[0].isalpha() and v[b+1:c].isalpha(): 
            return True
    return False




