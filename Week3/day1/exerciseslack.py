# Create a Employee class, With the attributes : firstname, lastname, age, job, salary
# Create 2 users object and display their attribute
# Lea Smith 30 years old developer 30000
# David Schartz 20 years old project manager 20000
# Add those methods to the class
# get_fullname(self) : that return the firstname + lastname
# happy_birthday(self) : that return the age incremented by one
# get_promotion(self, promotion_amount) : that increment the salary of the user by the promotion
# Call all the methods


class Employee :
    def __init__(self, firstname_employee, lastname_employee, age_employee, job_employee, salary_employee):
        self.firstname = firstname_employee
        self.lastname = lastname_employee
        self.age = age_employee
        self.job = job_employee
        self.salary = salary_employee

    def get_fullname(self) :
        fullname = self.firstname + " " + self.lastname
        print(fullname)
        return fullname
    
    def happy_birthday(self) :
       self.age += 1
       

    def get_promotion(self, promotion_amount):
        self.salary += promotion_amount
        return promotion_amount
        
    def game ():
        lst_names = ["John","Lea","Emma","Josh", "Eli"]
        lst_lastnames = ["Cohen","Smith", "Doe", "Sevi", "Shwartz"]
        lst_jobs = ["John","Lea","Emma","Josh", "Eli"]
    
Lea = Employee("Lea","Smith" , 30, "Developper", 30000)
David = Employee("David", "Shwartz", 30, "PM", 20000)
Lea.get_fullname()
David.get_fullname()
Lea.happy_birthday()
David.happy_birthday()
Lea.promotion_amount(2000)
David.promotion_amount(5000)

    
        

