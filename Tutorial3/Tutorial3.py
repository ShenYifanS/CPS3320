# defines a class called Person.
class Person:
    # a constructor function to initiate the variables of any person
    def __init__(self):
        self.name = ""
        self.age = 0
        self.weight = ""
        self.height = ""

    # allows the user to input user attributes
    def input_person_data(self):
        self.name = input("Please enter the name: ")
        self.age = int(input("Please enter the age: "))
        self.weight = input("Please enter the weight: ")
        self.height = input("Please enter the height: ")
        return
        # print a person name, age, weight.

    def get_person_data(self):
        print("The name is :", self.name)
        print("The age is :", self.age, " years old")
        print("The weight of the is :", self.weight)
        print("The height of the is :", self.height)


# Create a main() function
if __name__ == "__main__":
    # create two instances(objects) p1 and p2
    p1 = Person()
    p1.input_person_data()
    p1.get_person_data()

    print("\n\n")

    p2 = Person()
    p2.input_person_data()
    p2.get_person_data()
