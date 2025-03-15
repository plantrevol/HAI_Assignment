class Student:
    def __init__(self,student_id,name,age):
        self.Student_id = student_id
        self.Name = name
        self.Age = age
    def display_info(self):
        print("ID: {0}번 / 이름: {1} / 나이: {2}살".format(self.Student_id, self.Name, self.Age))
class StudentManager:
    def __init__(self):
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def display_all_students(self):
        for i in self.students:
            i.display_info()
      
student1 = Student("1", "김철수", 20)
student2 = Student("2", "이영희", 21)
student3 = Student("3", "박지민", 19)
manager = StudentManager()

manager.add_student(student1)
manager.add_student(student2)
manager.add_student(student3)

print("현재 등록된 학생 목록:")
manager.display_all_students()

student4 = Student("4", "한지수", 22)
manager.add_student(student4)

print("\n학번 4번 학생 추가 후:")
manager.display_all_students()
