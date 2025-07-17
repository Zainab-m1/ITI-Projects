
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
            



p=[{"name":"omar","pass":"123"},{"name":"zainab","pass":"550"}]
x=(input("What is your name?  ")).lower()
name_pass(p,x)
