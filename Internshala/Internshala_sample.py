class employe:
  def __init__ (self,id,name,designation,age,salary):
    self.id=id
    self.name=name
    self.designation=designation
    self.age=age
    self.salary=salary
  def company(self):
    print("emp id = " + self.id)
    print("emp name = " + self.name)
    print("emp designation = " + self.designation)
    print("emp age = " + self.age)
    print("emp salary = " + self.salary)

em=employe(1,"afeffa","pata ne",16,500)
em.company()