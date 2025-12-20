# 🧪 PRACTICE TASK
# Create a class Employee with:
# Attributes: name, salary
# Method: display_details()
class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def diplay_details(self):
        print("Employee Name:",self.name)
        print("Employee Salary:",self.salary)
emp1 = employee("Muhammed Ismayeel", 9000)
emp2 = employee("jhon",7000)
emp1.diplay_details()
emp2.diplay_details()

# 🧪 PRACTICE TASK
# Create:
# Parent class: Vehicle (attribute: brand)
# Child class: Car (attribute: model)
# Method to display full details
class Vehicle:
    def __init__(self, brand_name):
        self.brand_name = brand_name

class Car(Vehicle):
    def __init__(self, brand_name, model_name):
        super().__init__(brand_name)
        self.model_name = model_name

    def display_info(self):
        print("Car Brand:", self.brand_name)
        print("Car Model:", self.model_name)
car1 = Car("Ford", "Mustang")
car1.display_info()

# 🧪 Small Practice (Easy)
# Create:
# Parent class Bank
# Child classes SBI and HDFC
# Same method interest_rate() with different outputs
class Bank:
    def interest_rate(self):
        print("The interest rate is 5%")
class SBI(Bank):
    def interest_rate(self):
        print("The interest rate is 6%")
class HDFC(Bank):
    def interest_rate(self):
        print("The interest rate is 7%")   
bank = Bank()
sbi = SBI()
hdfc = HDFC()
bank.interest_rate()
sbi.interest_rate()
hdfc.interest_rate()

# Create a class Account with:
# Private variable __balance
# Method deposit(amount)
# Method show_balance()   
class Account:
    def __init__(self,balance):
        self.__balance = balance #private attribute
    def deposit (self,amount):
        print("Depositing: " , amount)
        self.__balance += amount
    def show_balance(self):
        print("Current Balance :" , self.__balance)
acc = Account(1000)
acc.show_balance()
acc.deposit(400)
acc.show_balance()

        