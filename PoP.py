'''from random import randrange

i = randrange(1, 20)

if(i == 10):
    print(f'{i} Draw')
elif (i > 10):
    print(f'{i} K.O')
else:
    print(f'{i} You Lose')
    '''
    
'''Duck Typing

class Animal:
    alive = True
    
class Toad(Animal):
    def Speak(self):
        print("Crock!")

class Frog(Animal):
    def Speak(self):
        print("Crack!")
        
class Cat:
    alive = False
    
    
    def Speak(self):
        print("UIIAIUIIIIAI")
        
animals = [Toad(), Frog(), Cat() ]

for animal in animals:
    animal.Speak()
    print(animal.alive)
    '''
    
'''Aggregation
    
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def list_books(self):
        return [f"{book.book_title} by {book.book_author}" for book in self.books]

class Book:
    def __init__(self, book_title, book_author):
        self.book_title = book_title
        self.book_author = book_title
        
library = Library("Raiabry")


bookOne = Book("Pyhthonu Purogramingu", "Markuru izu thamiku")
bookTwo = Book("Javaru Purogramingu Foru Bregrinnerus", "Johnru Aborunatinu")

library.add_book(bookOne)
library.add_book(bookTwo)

print(library.name)
for book in library.list_books():
    print(book)
    '''
    
    
'''Aggregation and Composition
    
class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power
    
class Wheel:
    def __init__(self, size):
        self.size = size
        
class Car:
    def __init__(self, manufacturer, model, horse_power, wheel_size):
        self.manufacturer = manufacturer
        self.model = model
        self.engine = Engine(horse_power)
        self.wheel = [Wheel(wheel_size) for wheel in range(4)]
        
    def display_car_details(self):
        return f"{self.manufacturer}, {self.model}, {self.engine.horse_power}, {self.wheel[0].size}"
        
car = Car("Bugghottie", "FRFRari", 1000, 20)
print(car.display_car_details())
'''

'''Nested Classes'''

class LethalCompany:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position
            
        def get_details(self):
            return f"{self.name} {self.position}"
            
    def __init__(self, name):
        self.name = name
        self.employees = []
        
    def add_employee(self, employee_name, employee_position):
        new_employee = self.Employee(employee_name, employee_position)
        self.employees.append(new_employee)

    def list_employee(self):
        return [employee.get_details() for employee in self.employees]
        
class REPO:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position
            
        def get_details(self):
            return f"{self.name}, {self.position}"
        
    def __init__(self, name, employee_Name, employee_Position):
        self.name = name
        self.employee = self.Employee(employee_Name, employee_Position)
        
        
company = LethalCompany("Chum Bucket")

company.add_employee("SpongeBob", "Manager")
company.add_employee("Plankton", "Cook")
company.add_employee("Mr.Crabs", "Dead")

companyTwo = REPO("Krusty Krab", "Patrick", "Manager")

print(company.name)
for employee in company.list_employee():
    print(employee)
    
print(companyTwo.name)
print(companyTwo.employee.get_details())