class Person:
    def __init__(self,person_name,person_age):
        self.person_name=person_name
        self.person_age=person_age
    def show_age(self):
        return self.person_age

class Student(Person):
    def __init__(self,type="",person_name="",person_age=0):
        self.type=type
        Person.__init__(self,person_name,person_age)


try:
    listt=[]
    obj3=[]
    f = open("C:\\Users\\akshatha.a.suresh\\PycharmProjects\\practice\\reading_file", "r")
    l=f.read().splitlines()
    # print(l)
    for i in l:
        c=i.split(" ")
        # print(c)
        name=c[0]
        age=c[1]
        type=c[2]
        obj3.append(Student(type,name,age))
    for k in obj3:
        print(k.show_age())

except FileNotFoundError:
    print("Please Enter a valid path")




