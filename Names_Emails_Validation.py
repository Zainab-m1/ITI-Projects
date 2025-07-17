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
        


emails_names_validation()



