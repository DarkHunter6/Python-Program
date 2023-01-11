class Person:
  def __init__(self, name, age): 
# All classes have a function called __init__(), which is always executed when the class is being initiated(Class Start Hoi Jokhon).
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
    self.name = name # self(Parameter).name(Variable Of self) = name(Parameter)
    self.age = age # Self(Parameter).age(Variable Of self) = age(Parameter)

p1 = Person("John", 36) # 

print(p1.name)
print(p1.age)