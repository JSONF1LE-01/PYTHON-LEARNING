import useful_tools

#pip install (python module)
#external modules /lib/site packages

#classes & Objects practice below
from Classes_Objects import Student
from chef import Chef
from Chinese_chef import ChineseChef

student1 = Student("timmy", "sempai", 4.0, False)

print(student1.name)
print(student1.major)
print(student1.gpa)
print(student1.is_on_probation)
print(student1.on_honor_role())

#inheritance
mychef = ChineseChef()
mychef.make_special_dish()
mychef.make_special_dish()