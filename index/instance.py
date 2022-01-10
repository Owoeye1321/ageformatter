from datetime import datetime
import math as mt


class AgeFormat:
    def __init__(self, name, year, month, day):
        self.name = name
        self.year = year
        self.month = month
        self.day = day

    def generate_age(self):
        current_year = datetime.now().timetuple()[0]
        current_month = datetime.now().timetuple()[1]
        current_day = datetime.now().timetuple()[2]
        if current_month > self.month:
            age = current_year - self.year
            print(f"Happy birthday in arrears {self.name}, your age is {age}")
        elif current_month < self.month:
            age = current_year - self.year-1
            in_addy_month = int(mt.fabs(current_month - self.month))
            print(f"T A D A !{self.name} Your age is {age} and your birthday is "
                  f"{self.day}th of the next {in_addy_month}months")
        elif current_month == self.month:
            if current_day > self.day:
                age = current_year - self.year
                print(f"Happy birthday in arrears {self.name}, your age is {age}")
            elif current_day < self.day:
                age = current_year - self.year-1
                in_addy_day = current_day - self.day
                print(f"T A D A ! {self.name} Your age is {age} and your birthday is in next {in_addy_day} days")
