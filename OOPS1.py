class Student:
  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade

  def get(self):
    print(f"Name: {self.name}")
    print(f"Age: {self.age}")
    sum = 0
    count = 0
    for i in self.grade:
      sum += i
      count+=1
    avg = sum/count
    print(f"Grade: {avg}")
  
  