class Student:

    scholarship_max = 6000
    scholarship_min = 4000
    without_scholarship = 0
    score_max = 5
    score_min = 4


    def __init__(self, name, age, group, gpa):
        self.group = group
        self.gpa = gpa
        self.name = name
        self.age = age


    def disp_info(self):
        print(f"ФИО студента:{self.name}")
        print(f"Номер группы студента:{self.group}")
        print(f"Средний баллл: {self.gpa}")


    def scholarship(self):
        if self.gpa == Student.score_max:
            return Student.scholarship_max
        else:
            if (self.gpa < Student.score_max) and (self.gpa >= Student.score_min):
                return Student.scholarship_min
            else:
                return Student.without_scholarship

    def compare_scholarship(self, other):
        if self.scholarship() > other.scholarship():
            return True
        else:
            return False


"Пример.Студенты"
student1 = Student("Nastya", 18, "B32", 5.0)
student2 = Student("Masha",19, "B31", 4.6)
student3 = Student("Matvey", 21,"B30", 2.5)


print("Информация о студенте:")
student1.disp_info()
print ("Стипендия студента №1 -", student1.compare_scholarship(student2),",чем у студента №2")
print ("Стипендия студента №1 -", student1.compare_scholarship(student3),",чем у студента №3")
print (" ")


print("Информация о студенте:")
student2.disp_info()
print ("Стипендия студента №2 -", student2.compare_scholarship(student1),",чем у студента №1")
print ("Стипендия студента №2 -", student2.compare_scholarship(student3),",чем у студента №3")
print (" ")


print("Информация о студенте:")
student3.disp_info()
print ("Стипендия студента №3 -", student3.compare_scholarship(student1),",чем у студента №1")
print ("Стипендия студента №3 -", student3.compare_scholarship(student2),",чем у студента №2")
print (" ")

class Aspirant:

    scholarship_max = 8000
    scholarship_min = 6000
    without_scholarship = 0
    score_max = 5
    score_min = 4

    def __init__(self, name, age, group, gpa, science_work):
        self.group = group
        self.gpa = gpa
        self.science_work = science_work
        self.name = name
        self.age = age

    def disp_info(self):
        print(f"ФИО аспиранта:{self.name}")
        print(f"Номер группы аспиранта:{self.group}")
        print(f"Средний баллл: {self.gpa}")
        print(f"Название научной работы:{self.science_work}")

    def sсholarship (self):
        if self.gpa == Student.score_max:
            return Student.scholarship_max
        else:
            if (self.gpa < Student.score_max) and (self.gpa >= Student.score_min):
                return Student.scholarship_min
            else:
                return Student.without_scholarship

    def compare_scholarship(self, other):
        if self.sсholarship() > other.sсholarship():
            return True
        else:
            return False


"Пример.Аспиранты"
aspirant1 = Aspirant("Ivan", 24, "C21", 4, "Построения ML-модели для распознавания инфаркта")
aspirant2 = Aspirant("Nazar",25, "С21", 5,"Система распознавания лиц преступников")
aspirant3 = Aspirant("Aleks", 32,"C25", 3, "Построение многоуровневой имитационной модели дискретного произвосдтва")


print("Информация об аспиранте:")
aspirant1.disp_info()
print ("Стипендия аспиранта №1 -", aspirant1.compare_scholarship(aspirant2),",чем у аспиранта №2")
print ("Стипендия аспиранта №1 -", aspirant1.compare_scholarship(aspirant3),",чем у аспиранта №3")
print (" ")


print("Информация об аспиранте:")
aspirant2.disp_info()
print ("Стипендия аспиранта №2 -", aspirant2.compare_scholarship(aspirant1),",чем у аспиранта №1")
print ("Стипендия аспиранта №2 -", aspirant2.compare_scholarship(aspirant3),",чем у аспиранта №3")
print (" ")


print("Информация об аспиранте:")
aspirant3.disp_info()
print ("Стипендия аспиранта №3 -", aspirant3.compare_scholarship(aspirant1),",чем у аспиранта №1")
print ("Стипендия аспиранта №3 -", aspirant3.compare_scholarship(aspirant2),",чем у аспиранта №2")



