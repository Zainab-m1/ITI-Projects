# Code 1: (Fun Lab) Open a Website Randomly
'''
import webbrowser
import random

websites = [
    "https://www.google.com",
    "https://www.wikipedia.org",
    "https://www.github.com",
    "https://www.reddit.com",
    "https://www.youtube.com",
    "https://www.python.org",
    "https://www.medium.com",
    "https://www.quora.com",
    "https://www.linkedin.com",
    "https://www.twitter.com",
    "https://www.facebook.com",
    "https://www.instagram.com",
    "https://www.amazon.com"

]

selected_website = random.choice(websites)
print(f"Opening: {selected_website}")
webbrowser.open(selected_website)

'''



# Code 2: (Main OOP Project) 

class person:
    def __init__(self, name, money):
        try:
            self.name = name
            self.money = int(money)
            print(f"Welcome {self.name}")
        except ValueError:
            self.__init__(self, self.name, input("Please enter a real number for money: "))
        
    def sleep(self, hours):
        try:
            hours = int(hours)
            if hours < 0 or hours > 24:
                self.sleep(input("Invalid input. Please enter a real number: "))
                return
            elif hours < 8:
                self.mood = "tired"
                print(f"{self.name} is {self.mood}.")
            elif hours > 8:
                self.mood = "lazy"
                print(f"{self.name} is {self.mood}.")
            else:
                self.mood = "happy"
                print(f"{self.name} is {self.mood}.")
        except ValueError:
            self.sleep(input("Invalid input. Please enter a number for hours: "))
            return
    
    def eat(self,meals):
        try:
            meals = int(meals)
            if meals < 0:
                    self.eat(input("Invalid input. Please enter a real number: "))
                    return
            elif meals == 3:
                    self.healthRate = 100
                    print(f"{self.name} is healthy and {self.name}'s health_rate = {self.healthRate}.")
            elif meals == 2:
                    self.healthRate = 75
                    print(f"{self.name} is okay and {self.name}'s health_rate = {self.healthRate}.")
            elif meals == 1:   
                    self.healthRate = 50
                    print(f"{self.name} is hungry and {self.name}'s health_rate = {self.healthRate}.")
            elif meals == 0 :
                    self.healthRate = 0
                    print(f"{self.name} is starving and {self.name}'s health_rate = {self.healthRate}.")
            elif meals > 3:
                    self.healthRate = 100
                    print(f"{self.name} is overfed.")
        except ValueError:
            self.eat(input("Invalid input. Please enter a number for meals: "))
            return

    def buy(self, items):
        try:
            self.items = int(items)
            if self.items < 0 and self.money >= 0:
                self.items = input("Invalid input. Please enter a real number for items: ")
                self.buy(self.items, self.money)
                return
            if self.money < 0 and self.items >= 0:
                self.money = input("Please enter a real number for money: ")
                self.buy(self.items, self.money)
                return
            if self.items < 0 and self.money < 0:
                self.items = input("Invalid input. Please enter a real number for items: ")
                self.money = input("Please enter a real number for money: ")
                self.buy(self.items, self.money)
                return
            elif self.items >= 1:
                self.money -= 10 * self.items  
                if self.money < 0:
                    self.money += 10 * self.items  
                    print(f"{self.name} does not have enough money to buy {self.items} items. Money : {self.money}.")
                else:
                    print(f"{self.name} bought {self.items} items (price = 10 / item). Money left: {self.money}.")
            elif items == 0:
                print(f"{self.name} did not buy any items. Money left: {self.money}.")

        except ValueError:
            self.items = input("Invalid input. Please enter a real number for items: ")
            self.buy(self.items, self.money)
            return
            

class employee(person):

    def __init__(self,name):
        self.name = name
        super().__init__(name, money)

    def work(self, hours): 
        try:
            hours = int(hours)
            if hours < 0 or hours > 24:
                self.work(input("Invalid input. Please enter a real number: "))
                return
            elif hours == 8:
                self.mood = "happy"
                print(f"{self.name} is {self.mood}.")
            elif hours > 8:
                self.mood = "tired"
                print(f"{self.name} is {self.mood}.")
            elif hours < 8:
                self.mood = "lazy"
                print(f"{self.name} is {self.mood}.")
        except ValueError:
            self.work(input("Invalid input. Please enter a number for hours: "))
            return 
        
    def drive(self, distanceToWork, fuelrate, car_name):
        self.car_name = car_name
        if self.car_name == "No Car":
            print(f"{self.name} does not have a car to drive.")
            return
        self.car = car(self.name, car_name)
        try:
            self.distanceToWork = int(distanceToWork)
            self.fuelrate = int(fuelrate)
            if self.distanceToWork < 0:
                self.distanceToWork = input("Invalid input. Please enter a real number for distance: ")
                self.drive(self.distanceToWork, self.fuelrate)
                return  
            if self.fuelrate < 0:
                self.fuelrate = input("Please enter a real number for fuel rate: ")
                self.drive(self.distanceToWork, self.fuelrate)
                return
            if self.distanceToWork == 0:
                print(f"{self.name} is not driving anywhere.")
                x=car(self.name, self.car_name)
                x.stop(self.distanceToWork)      
                return
            elif self.distanceToWork > 0 :
                print(f"{self.name} is driving for {self.distanceToWork} km.")
                self.fuelrate -= self.fuelrate * 0.9 * (self.distanceToWork / 10)
                if self.fuelrate < 5:
                    self.car.stop(self.distanceToWork)
                    return
            self.velocity = 200
            self.time = self.distanceToWork / 200
            self.car.run(self.distanceToWork, self.velocity, self.fuelrate)
        except ValueError:
            self.distanceToWork = input("Invalid input. Please enter a real number for distance: ")
            self.fuelrate = input("Please enter a real number for fuel rate: ")
            self.drive(self.distanceToWork, self.fuelrate)

    def refuel(self, gasAmount):
        try:
            gasAmount = int(gasAmount)
            if gasAmount < 0 or (self.fuelrate + gasAmount) > 100:
                self.refuel(input("Please enter a real number for gas amount: "))
                return      
            elif gasAmount > 0:
                self.money -= gasAmount * 2 #liter price is 2
                if self.money < 0:
                    print("Invalid input. You don't have enough money.")
                    return
                self.fuelrate += gasAmount
                print(f"{self.name} refueled the car with {gasAmount} liters. Money left: {self.money}.")
        except ValueError:
            self.refuel(input("Invalid input. Please enter a real number for gas amount: "))

    
    def send_email(self, email):
        self.email = email
        if '@' in self.email and '.' in self.email:
            user_name, domain = self.email.split('@')
            if user_name and domain:
                x,y=domain.split('.')
                if x and y:
                    print(f"{self.name} sent an email by {self.email}.")
            else: 
                self.send_email(input("Invalid email format. Please enter a valid email address: "))
        else: 
            self.send_email(input("Invalid email format. Please enter a valid email address: "))
        
        


class car:
    def __init__(self, name, car_name):
        self.name = name
        self.car_name = car_name

    def run(self,distanceToWork, velocity, feulrate):
        try:
            self.distanceToWork = int(distanceToWork)
            self.velocity = int(velocity)
            self.fuelrate = int(feulrate)
            if self.velocity > 0 or self.velocity < 200:
                self.time = self.distanceToWork / self.velocity
            else:
                print("Invalid velocity. Please check the distance and velocity.")
                return
            print(f"{self.name} is driving at {self.velocity} km/h for {self.distanceToWork} km. Estimated time: {self.time} hours.")
            self.fuelrate = self.fuelrate * 0.9 * (self.distanceToWork / 10)
            if self.fuelrate < 5:
                print(f"{self.name} needs refueling. Current fuel rate: {self.fuelrate} liters.")
                self.stop (self)
        except ValueError:
            self.distanceToWork = input("Invalid input. Please enter a real number for distance: ")
            self.velocity = input("Please enter a real number for velocity: ")
            self.fuelrate = input("Please enter a real number for fuel rate: ")
            self.run(self.distanceToWork, self.velocity, self.fuelrate)
            return
        

    def stop(self, distanceToWork):
        try:
            self.velocity = 0
            self.distanceToWork = distanceToWork
            print(f"{self.name}'s car is going to stop and the distance to work is {self.distanceToWork} km.")
            if self.distanceToWork != 0:
                self.refuel(input("Please enter a gas amount to refuel: "))
        except:
            pass


class office:
    def __init__(self, name, office_name):
        self.name = name
        self.office_name = office_name
        self.employees = {
        1: {"name": "Zainab", "salary": 15000, "ID": 123},
        2: {"name": "Omar", "salary": 30000, "ID": 870},
        3: {"name": "Ahmed", "salary": 20000, "ID": 532},
        4: {"name": "Amira", "salary": 10000, "ID": 666},
        5: {"name": "Zaid", "salary": 6000, "ID": 163},
        6: {"name": "Qasem", "salary": 15000, "ID": 200},
        7: {"name": "Samy", "salary": 25000, "ID": 300},
        8: {"name": "Amir", "salary": 22000, "ID": 360}

         }
        for emp in self.employees.values():
            if self.office_name.lower() == "iti" and self.name.lower() == emp["name"].lower():
                print(f"Welcome to the ITI , {self.name}.")   
                break
        else:
            print(f"You are not authorized to access this office, {self.name}.")
            exit()

    def get_all_employees(self):
        n=0
        for emp in self.employees.values():
            print(emp["name"])
            n+= 1
        print(f"Total number of employees: {n}")

    def get_employee(self, employeeID):
        for emp in self.employees.values():
            if emp["ID"] == employeeID:
                print(f"Employee found: {emp['name']} with ID: {emp['ID']} and salary: {emp['salary']}.")
                return emp
        else:
            print(f"Employee with ID {employeeID} not found.")
                

    def hire_employee(self, employee, employee_id, salary):
        for emp in self.employees.values():
            if emp["ID"] == employee_id:
                print(f"Employee with ID {employee_id} already exists.")
                return
        self.employees[len(self.employees)+1] = {"name": employee, "salary": salary, "ID": employee_id}
        print(f"Hired new employee: {employee} with ID: {employee_id} and salary: {salary}.")
   
    def fire_employee(self, employee_id):
        n=1
        for i in self.employees.values():
            if i["ID"] == employee_id:
                del self.employees[n]
                print(f"Fired employee with ID: {employee_id}.")
                return
            n += 1
        print(f"Employee with ID {employee_id} not found.")


    def deduct_salary(self, employee_id, deduction):
        for emp in self.employees.values():
            if emp["ID"] == employee_id:
                emp["salary"] -= deduction
                print(f"Deducted {deduction} from {emp['name']}'s salary. New salary: {emp['salary']}.")
                return
        print(f"Employee with ID {employee_id} not found.")

    def reward(self, employee_id, reward):
        for emp in self.employees.values():
            if emp["ID"] == employee_id:
                emp["salary"] += reward
                print(f"Rewarded {reward} to {emp['name']}. New salary: {emp['salary']}.")
                return
        print(f"Employee with ID {employee_id} not found.")

    
    def check_lateness(self, employee_id, moveHour):
        for emp in self.employees.values():
            if emp["ID"] == employee_id:
                if moveHour > 9:
                    print(f"{emp['name']} is late by {moveHour - 9} hours.")
                    emp["salary"] -= 10
                    print(f"{emp['name']}'s salary has been reduced by 10. New salary: {emp['salary']}.")
                else:
                    print(f"{emp['name']} is on time.")
                    emp["salary"] += 10
                    print(f"{emp['name']}'s salary has been increased by 10. New salary: {emp['salary']}.")
                return
        print(f"Employee with ID {employee_id} not found.")

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        time = distance / velocity
        moveHour = moveHour + time
        if time < 0:
            print("Invalid time.")
            return
        if moveHour > targetHour:
            lateness = moveHour - targetHour
            print(f"Late by {lateness} hours.")
        else:
            lateness = 0
            print("On time.")
        return lateness

    @classmethod
    def change_emps_num(cls):
        cls.employeesNum = len(cls.employees)
        print(f"Number of employees changed to: {cls.employeesNum}")
        return cls.employeesNum

    employeesNum = change_emps_num
 





# Main Code :
 
name = input("Hello Sir, What is your name? ") # The user can input any name with no restrictions.
money = input("How much money do you have? ")
x=person(name, money)
x.sleep(input("How many hours did you sleep? ")) 
x.eat(input("How many meals do you eat per day? "))

items=input("There is a supermarket near you, How many items do you want to buy? ")
x.buy(items, )

Ask_if_an_employee=input("Are you an employee? (yes/no) ")
if Ask_if_an_employee.lower() == "yes":
    y = employee(name)
    y.work(input("How many hours did you work today? "))
    y.send_email(input("Please enter the email address to send an email: "))
else:
    print("You are not an employee, so you cannot perform work-related actions.")
    
z=input("Do you have a car? (yes/no) ")
if z.lower() == "yes":
    y = employee(name)
    car_name = input("Please enter your car name: ")
    y.drive(input("How far will you go? "), input("What is the fuel rate of your car? "), car_name)

if Ask_if_an_employee.lower() == "yes":
    c=office(name,input("Please enter your office name: "))

    if (input("Do you want to see all employees? (yes/no) ").lower() == "yes"):
        c.get_all_employees()


    if (input("Do you want to get an employee by ID? (yes/no) ").lower() == "yes"):
        try:
            emp_id = int(input("Please enter the employee ID: "))
            c.get_employee(emp_id)
        except ValueError:
            c.get_employee(input("Invalid input. Please enter a valid employee ID: "))


    if (input("Do you want to hire a new employee? (yes/no) ").lower() == "yes"):
        try:
            emp_name = input("Please enter the new employee's name: ")
            emp_id = int(input("Please enter the new employee's ID: "))
            emp_salary = int(input("Please enter the new employee's salary: "))
            c.hire_employee(emp_name, emp_id, emp_salary)
        except ValueError:
            print("Invalid input. Please enter valid data for employee name, ID, and salary.")
            c.hire_employee(input("Please enter the new employee's name: "), 
                            input("Please enter the new employee's ID: "), 
                            input("Please enter the new employee's salary: "))


    if (input("Do you want to fire an employee? (yes/no) ").lower() == "yes"):
        try:
            emp_id = int(input("Please enter the employee ID to fire: "))
            c.fire_employee(emp_id)
        except ValueError:
            print("Invalid input. Please enter a valid employee ID.")
            c.fire_employee(input("Please enter the employee ID to fire: "))

    if (input("Do you want to deduct salary from an employee? (yes/no) ").lower() == "yes"):
        try:
            emp_id = int(input("Please enter the employee ID: "))
            deduction = int(input("Please enter the amount to deduct: "))
            c.deduct_salary(emp_id, deduction)
        except ValueError:
            print("Invalid input. Please enter valid data for employee ID and deduction amount.")
            c.deduct_salary(input("Please enter the employee ID: "), 
                            input("Please enter the amount to deduct: "))


    if (input("Do you want to reward an employee? (yes/no) ").lower() == "yes"):
        try:
            emp_id = int(input("Please enter the employee ID: "))
            reward = int(input("Please enter the reward amount: "))
            c.reward(emp_id, reward)
        except ValueError:
            print("Invalid input. Please enter valid data for employee ID and reward amount.")
            c.reward(input("Please enter the employee ID: "), 
                    input("Please enter the reward amount: "))

    if (input("Do you want to check lateness for an employee? (yes/no) ").lower() == "yes"):
        try:
            emp_id = int(input("Please enter the employee ID: "))
            moveHour = int(input("Please enter the hour the employee moved: "))
            c.check_lateness(emp_id, moveHour)
        except ValueError:
            c.check_lateness(input("Please enter the real employee ID: "), input ("Please enter the real hour the employee moved: "))

    if (input("Do you want to calculate lateness for an employee? (yes/no) ").lower() == "yes"): 
        try:
            targetHour = int(input("Please enter the target hour: "))
            moveHour = int(input("Please enter the hour the employee moved: "))
            distance = int(input("Please enter distance remain: "))
            velocity = int(input("Please enter the velocity: "))
            c.calculate_lateness(targetHour, moveHour, distance, velocity)
        except ValueError:
            c.check_lateness(input("Please enter the target hour: "), input("Please enter the hour the employee moved: "), input("Please enter distance remain: "), input("Please enter the velocity: "))   
            


    if (input("Do you want to see all employees again? (yes/no) ").lower() == "yes"):
        c.get_all_employees()
