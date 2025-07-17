# You are given a list of email addresses in the format username@domain.
# Your task is to use the map() function along with a lambda expression to extract only the domain part from each email address.

p=["zainab@gmail.com","mai@hotmail.com","ahmed@iti.net","omar@auc.com"]
def domain(p):
    print(list(map(lambda x: x.split("@").pop(1), p)))

domain(p)