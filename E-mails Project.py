import csv
import Modules

file = open('Email_Project/E-mails.csv', 'r', encoding='utf-8')
reader = csv.DictReader(file)

# Check the email validity
list_of_emails = []
for row in reader:
    email = row['Email']
    if Modules.emailva(email):
        list_of_emails.append(email)
    else:
        continue

# Get the domain names from valid emails
x = Modules.domain(list_of_emails)
print("Domains:", x)
y = sorted(list(x))

New_File = open('Email_Project/Domains.csv', 'w', newline='')
writer = csv.writer(New_File)
writer.writerow(['Domain'] )
for domain in y:
    writer.writerow([domain])

file.close()
New_File.close()    
