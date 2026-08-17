class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return f"The {self.year} {self.make} {self.model}'s engine has started."

    def stop_engine(self):
        return f"The {self.year} {self.make} {self.model}'s engine has stopped."
