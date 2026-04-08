class Customer:
    # THIS IS THE CONSTRUCTOR OF THE CLASS
    # SELF IS ACTING AS THIS IN JAVA OR PHP
    # IF THE METHOD IS GOING TO BE AN INSTANCE METHOD, ITS FIRST PARAMETER MUST BE SELF
    # FOR PRIVATE VARIBLES DO THIS(Eg: self._age = 10). This ensures that it is not accessible outside the class
    def __init__(self,name: str, email: str, telephone: str):
        self.name = name
        self.email = email
        self.telephone = telephone

    def place_order(self):
        print("Order placed by " + self.name)

    def cancel_order(self):
        print("Order cancelled by " + self.name)

# GETTERS AND SETTERS ARE NOT REALLY A THING IN PYTHON


# CREATING OBJECTS FROM THE CONSTRUCTOR
# IN USING IT, WE'LL ALWAYS IGNORE SELF BUT IN DECLARING IT, WE'LL ALWAYS INCLUDE SELF
cust = Customer(name="Peter", email="peter@gmail.com", telephone="0532824330")
# cust.name = "Patrick"
print(cust.name)

# INHERITANCE

# PYTHON SUPPORTS MULTIPLE INHERITANCE

class A:
    pass

class B:
    pass

class C(A,B):
    pass