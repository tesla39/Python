
#kwargs is used to provide extra argument than protoyped
def describe_vehicle(color, year, **kwargs):
    print(f"This vehicle is {color} and was built in {year}.")
    #here  'f' formats the values also as a string
    if kwargs:
        print("Additional attributes:")
         
describe_vehicle("blue", 2023, brand="Toyota", model="Camry", features="GPS")
