"""
Objective oriented programming (OOP) is a programming paradigm that uses objects and classes to structure code. It allows for the creation of reusable and modular code, making it easier to manage and maintain.

1. Object: An object is an instance of a class that encapsulates data and behavior. It represents a real-world entity and can have attributes (data) and methods (functions) associated with it.
2. Class: A class is a blueprint for creating objects. It defines the attributes and methods that the objects created from the class will have.

"""
#This is the definition of the Car class, which serves as a blueprint for creating car objects. 
#The class has an __init__ method that initializes the attributes make, model, and year when a new car object is created. 
#It also has two methods, start_engine and stop_engine, which return strings indicating the status of the car's engine.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return f"The {self.year} {self.make} {self.model}'s engine has started."

    def stop_engine(self):
        return f"The {self.year} {self.make} {self.model}'s engine has stopped."

car1 = Car("Toyota", "Camry", 2020)
print(car1.start_engine()) #This is the way to call the method start_engine() of the car1 object, which is an instance of the Car class. The method returns a string indicating that the engine has started, and this string is printed to the console.
print(car1.stop_engine()) #This is the way to call the method stop_engine() of the car1 object, which is an instance of the Car class. The method returns a string indicating that the engine has stopped, and this string is printed to the console.

class prettytable:  
    def __init__(self, data):
        self.data = data

    def display(self):
        for row in self.data:
            print(" | ".join(str(item) for item in row))#first the items in the row are converted to strings using str(item) for item in row, then they are joined together with " | " as the separator using the join() method. Finally, the resulting string is printed to the console using print().

    def add_row(self, row):
        self.data.append(row) #This is the way to add a new row to the data attribute of the prettytable object. The row parameter is a list representing the new row to be added, and it is appended to the data list using the append() method.

    def remove_row(self, index):
        if 0 <= index < len(self.data):
            self.data.pop(index) #This is the way to remove a row from the data attribute of the prettytable object. The index parameter specifies the position of the row to be removed, and it is removed from the data list using the pop() method.
        else:
            print("Invalid index. Please provide a valid row index.")

    def update_row(self, index, new_row):
        if 0 <= index < len(self.data):
            self.data[index] = new_row #This is the way to update a row in the data attribute of the prettytable object. The index parameter specifies the position of the row to be updated, and the new_row parameter is a list representing the updated row. The existing row at the specified index is replaced with the new_row.
        else:
            print("Invalid index. Please provide a valid row index.")
    
a = prettytable([["Name", "Age", "City"], ["Alice", 30, "New York"], ["Bob", 25, "Los Angeles"], ["Charlie", 35, "Chicago"], ["David", 28, "Houston"], ["Eve", 32, "Phoenix"], ["Frank", 29, "Philadelphia"], ["Grace", 31, "San Antonio"], ["Hannah", 27, "San Diego"], ["Ian", 33, "Dallas"], ["Jack", 26, "San Jose"]])
a.display() #This is the way to call the method display() of the a object, which is an instance of the prettytable class.
#The method prints the data in a tabular format to the console.
a.add_row(["Kate", 34, "Austin"]) #This is the way to call the method add_row() of the a object, which is an instance of the prettytable class. The method adds a new row to the data attribute of the a object.
a.remove_row(2) #This is the way to call the method remove_row() of the a object, which is an instance of the prettytable class. The method removes the row at index 2 from the data attribute of the a object.
a.update_row(1, ["Bob", 26, "Los Angeles"]) #This is the way to call the method update_row() of the a object, which is an instance of the prettytable class. The method updates the row at index 1 with the new data provided in the new_row parameter.
a.display() #This is the way to call the method display() of the a object, which is an instance of the prettytable class. The method prints the updated data in a tabular format to the console.