from index.instance import AgeFormat as object

print("Please ensure to use numerical value throughout")
try:
    get_name = input("What is your name ")
    get_year = int(input("Which year were you born "))
    get_month = int(input("Which month were you born "))
    get_day = int(input("Which day were you born "))
    age = object(get_name, get_year, get_month, get_day)
    age.generate_age()
except ValueError:
    print("Incorrect Details")
    print("Please follow the above instruction")




