# def valid_email(email):
#     b=c=0
#     v=email.strip()
#     for i in range(len(v)):
#          if v[i]=="@": b=i
#          if v[i]==".": c=i
#     try:
#         if (c-b)>2 and b!=0 and v[0].isalpha() and v[b+1:c].isalpha(): 
#             return True
#     except:
#         return False
         
# for n in range (5):  
#     if valid_email(input("Please enter your email:  ")):
#         print('Welcome')
#         break
# else:
#     raise ("Don't enter again. ")




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



for i in range(5):
    email = input("Enter your email: ")
    if emailva(email):
        break
    
else:
    raise ("Don't enter again. ")

print(f"Email: {email}")
        

