class Car:
    def __init__(self, trade_mark: str, model: str, year: int):
        self.trade_mark = trade_mark
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.trade_mark} {self.model}\'s engine is starting!")

    def drive(self, distance=200):
        print(f"{self.trade_mark} {self.model}, is driving {distance} kilometers!")

    def stop_engine(self):
        print(f"The {self.trade_mark} {self.model}\'s engine is stopping!")


car1 = Car("Toyota", "Rav4", 2022)
car2 = Car("Mercedes", "E200", 1999)

print(car1.trade_mark)
print(car2.year)

car1.start_engine()
car2.stop_engine()

car1.drive()
