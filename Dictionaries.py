Student = { 
   "Name":"Alice",
   "Age": 24,
   "Major": "Computer Science"
}

print("Name:", Student["Name"])
print("Major:", Student["Major"])

Student["Age"] = 25
Student[ "GPA"] = 3.8
print(Student)

for key, value in Student.items():
    print(f"{key}:{value}")

def check_key(Student, key):
    if key in Student: 
        return "Key exists"
    else:
        return "Key dose not exist"
print(check_key(Student, "Name"))

words = ["Apple","Apple","Apple","Apple","Bananna","Bananna","Bananna","Bananna"]

word_count = {}
for  word in words:
    if word in word_count:
        word_count[word] += 1 
else:
    word_count[word] = 1

print(word_count)


Dictionary1 = { "Yoasobi": 100, 
"Onerepublic": 100}
Dictionary2 = {"U2", "Polyphia"}

merged_dictionary = (Dictionary1, Dictionary2 )
print(merged_dictionary)

Student.pop("Age", None)
print(Student)


Classroom = {
    "Student1":{"Name": "Jhon", "Age1": 29},
    "Student2":{"Name": "Emma", "Age2": 39}
}

print("Student1 Name:", Classroom["Student1"]["Name"])
print("Student2 Age2:", Classroom["Student2"]["Age2"])

