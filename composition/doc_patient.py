
"""5. Hospital: Doctor & Patient
Model real-world relationships using multiple composed objects.
▲ Hide
Create an Address class with city and country."""
class Address :
    def __init__(self, city, country):
        self.city = city
        self.country = country

"""Create a Doctor class with name, specialization, and an Address object"""
class Doctor:
    def __init__(self, name, spec, address):
        self.name = name
        self.spec = spec
        self.address = address
        
"""Create a Patient class with name, age, and an assigned Doctor object.""""""

Add a report() method on Patient that prints: name, age, and their doctor's name and location."""
class Patient:
    def __init__(self, name, age, doc):
        self.name = name
        self.age = age
        self.doc =  doc
    
    def report(self):
        print(f"Details of the patient:\n Name: {self.name} \n Age: {self.age} \n Doctor's name: {self.doc.name} \n Doctor's Location: {self.doc.address.city}, {self.doc.address.country} ")
"""        
Create 2 patients assigned to different doctors and call report() on each."""

address1 = Address("Kathmandu", "Nepal")
address2 = Address("NY", "USA")

doc1 = Doctor("Dr. strange", "cardio", address1)
doc2 = Doctor("Dr. Brace", "orthodento", address2)

pat1 = Patient("Lal Badur", 24, doc2)
pat2 = Patient("Jiban", 34, doc1)

pat1.report()



