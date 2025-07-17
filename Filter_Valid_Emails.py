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

p=["zainab@gmail.com",".ssw;@lls;.ws","mai@hotmail.com","ahmed@iti.net","omar@auc.com","@ekel.xsdc","swkjdos"]
print(list(filter(valid_email, p)))