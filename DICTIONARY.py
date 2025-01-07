student = {
    "name" : "Alice",
    "age"  : 20,
    "courses" : ["Math","Physics"]
}
print(student)

Product1 = {

  "Product" : "Majesty 8 string guitar",
  "Price" : 17000,
  "Quantity" : 1
}

print(Product1)

student_information1 = {
    "name" : "Bob",
    "age"  :  21,
    "Major" : "Computer Science"
}

student_information2 = dict(Name="emma", Age=22, Major="Biology")

print(student_information1)
print(student_information2)


Student3 =  {
    "Name" : "Charlie",
    "Age":  19,
    "Major":  "Physics"

}

print(Student3["Name"])

Student3["GPA"] = 3.1

Student3["Age"] = 20

Student3.pop("Major")

print(Student3)
