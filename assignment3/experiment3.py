
total = int(input("enter total number of students : \n"))

class student:
    def __init__(self,name,course,uid, address):
        self.name = name
        self.course = course
        self.uid = uid
        self.address = address
        
    def details(self):
        print("The name of the student is : ",self.name)
        print("Course he/she pursing is : ", self.course)
        print("Id of the student is : ",self.uid)
        print("the address of the student is : ", self.address,"\n")
        
stu = []
for i in range(total):
    uid = input("enter roll no.: ")
    name = input("enter name : ")
    course = input("enter class : ")
    address = input("enter student address : ")
    
    stu_data = student(name,course,uid, address)
    stu.append(stu_data)
    
for j in stu:
    j.details()

