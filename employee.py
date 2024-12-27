"""
  File: employee.py
  Description: Creates several employee types, assigns varying attributes,
  and prints them out

  Student Name: Primo M. Marquez
  Student UT EID: pmm2734

  Course Name: CS 313E
  Unique Number: 52590
  Date Created: September 6, 2023
  Date Last Modified: September 13, 2023
"""

class Employee:
    '''Class Employee that takes name, identifier, and salary attributes'''
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.identifier = kwargs['identifier']
        self.salary = None
        if 'salary' in kwargs:
            self.salary = kwargs['salary']

    def get_salary(self):
        '''Return salary'''
        return self.salary

    def __str__(self):
        return ('Employee \n' + self.name + ', ' + self.identifier +
                    ', ' + str(self.salary))

class PermanentEmployee(Employee):
    '''PermanentEmployee, inherits Employee attributes and adds benefits'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.benefits = kwargs['benefits']

    def cal_salary(self):
        '''Calculates salary based on chosen benefits'''
        if str(self.benefits) == '[\'health_insurance\']':
            return self.salary * 0.9
        if str(self.benefits) == '[\'retirement\']':
            return self.salary * 0.8
        if str(self.benefits) == '[\'retirement\', \'health_insurance\']':
            return self.salary * 0.7
        return self.salary

    def __str__(self):
        return ('PermanentEmployee \n' + self.name + ', ' + self.identifier +
                ', ' + str(self.salary) + ', ' + str(self.benefits))

class Manager(Employee):
    '''Manager, inherits Employee attributes and adds bonus pay'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bonus = kwargs['bonus']

    def cal_salary(self):
        '''Calculate total salary, bonus included'''
        return float(self.salary + self.bonus)

    def __str__(self):
        return ('Manager \n' + self.name + ', ' + self.identifier +
                ', ' + str(self.salary) + ', ' + str(self.bonus))

class TemporaryEmployee(Employee):
    '''TemporaryEmployee, inherits Employee attributes and adds hours'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hours = kwargs['hours']

    def cal_salary(self):
        '''Calculate salary based on hours and base salary'''
        return float(self.salary * self.hours)

    def __str__(self):
        return ('TemporaryEmployee \n' + self.name + ', ' + self.identifier +
                ', ' + str(self.salary) + ', ' + str(self.hours))

class Consultant(TemporaryEmployee):
    '''Consultant, inherits TemporaryEmployee attributes and adds travel'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.travel = kwargs['travel']

    def cal_salary(self):
        '''Calculate salary based on travel and hours worked'''
        return float((self.salary * self.hours) + (self.travel * 1000))

    def __str__(self):
        return ('Consultant \n' + self.name + ', ' + self.identifier +
                ', ' + str(self.salary) + ', ' + str(self.hours) 
                + ', ' + str(self.travel))

class ConsultantManager(Consultant, Manager):
    '''ConsultantManager, inherits Concultant and Manager attributes'''
    def cal_salary(self):
        '''Calculate salary bsaed on hours, bonus, and travel'''
        return float((self.salary * self.hours) + self.bonus + (self.travel * 1000))

    def __str__(self):
        return ('ConsultantManager \n' + self.name + ', ' + self.identifier + ', ' +
                str(self.salary) + ', ' + str(self.hours) + ', ' + str(self.travel) +
                ', ' + 'ConsultantManager\n' + self.name + ', ' + self.identifier
                + ', ' + str(self.salary) + ', ' + str(self.bonus))

def main():
    """
    A Main function to create some example objects of our classes. 
    """

    chris = Employee(name="Chris", identifier="UT1")
    print(chris, "\n")

    emma = PermanentEmployee(name="Emma", identifier="UT2",
                              salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = TemporaryEmployee(name="Sam", identifier="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", identifier="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", identifier="UT5",
                        salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = ConsultantManager(name="Matt", identifier="UT6",
                              salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")

    print("Sam's Salary is:", sam.cal_salary(), "\n")

    print("John's Salary is:", john.cal_salary(), "\n")

    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")

    print("Matt's Salary is:",  matt.cal_salary(), "\n")

if __name__ == "__main__":
    main()
