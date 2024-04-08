class student:

    def __init__(self, name, age, gruppa, gpa):
        self.gruppa = gruppa
        self.gpa = gpa
        self.name = name
        self.age = age

    def disp_info(self):
        print(f"ФИО студента:{self.name}")
        print (f"Номер группы аспиранта:{self.gruppa}")
        print (f"Средний баллл: {self.gpa}")

    def sholarship (self):
        if self.gpa == 5:
            return 6000
        else:
            if self.gpa < 5 and self.gpa >= 4:
                return 4000
            else:
                return 0

    def sravnenie_sholarship(self, other):
        if self.sholarship() > other.sholarship():
            return "больше"
        else:
            return "меньше"


"Пример.Студенты"
student1 = student("Nastya", 18, "B32", 3.6)
student2 = student("Masha",19, "B31", 4.6)
student3 = student("Matvey", 21,"B30", 2.5)


print("Информация о студенте:")
student1.disp_info()
print ("Стипендия студента №1 -", student1.sravnenie_sholarship(student2),",чем у студента №2")
print ("Стипендия студента №1 -", student1.sravnenie_sholarship(student3),",чем у студента №3")
print (" ")


print("Информация о студенте:")
student2.disp_info()
print ("Стипендия студента №2 -", student2.sravnenie_sholarship(student1),",чем у студента №1")
print ("Стипендия студента №2 -", student2.sravnenie_sholarship(student3),",чем у студента №3")
print (" ")


print("Информация о студенте:")
student3.disp_info()
print ("Стипендия студента №3 -", student3.sravnenie_sholarship(student1),",чем у студента №1")
print ("Стипендия студента №3 -", student3.sravnenie_sholarship(student2),",чем у студента №2")


class aspirant:

    def __init__(self, name, age, gruppa, gpa, science_work):
        self.gruppa = gruppa
        self.gpa = gpa
        self.science_work = science_work
        self.name = name
        self.age = age

    def disp_info(self):
        print(f"ФИО аспиранта:{self.name}")
        print(f"Номер группы аспиранта:{self.gruppa}")
        print(f"Средний баллл: {self.gpa}")
        print(f"Название научной работы:{self.science_work}")

    def sholarship (self):
        if self.gpa == 5:
            return 8000
        else:
            if self.gpa < 5 and self.gpa >= 4:
                return 6000
            else:
                return 0

    def sravnenie_sholarship(self, other):
        if self.sholarship() > other.sholarship():
            return "больше"
        else:
            return "меньше"


"Пример.Аспиранты"
aspirant1 = aspirant("Ivan", 24, "C21", 4, "Построения ML-модели для распознавания инфаркта")
aspirant2 = aspirant ("Nazar",25, "С21", 5,"Система распознавания лиц преступников")
aspirant3 = aspirant("Aleks", 32,"C25", 3, "Построение многоуровневой имитационной модели дискретного произвосдтва")


print("Информация об аспиранте:")
aspirant1.disp_info()
print ("Стипендия аспиранта №1 -", aspirant1.sravnenie_sholarship(aspirant2),",чем у аспиранта №2")
print ("Стипендия аспиранта №1 -", aspirant1.sravnenie_sholarship(aspirant3),",чем у аспиранта №3")
print (" ")


print("Информация об аспиранте:")
aspirant2.disp_info()
print ("Стипендия аспиранта №2 -", aspirant2.sravnenie_sholarship(aspirant1),",чем у аспиранта №1")
print ("Стипендия аспиранта №2 -", aspirant2.sravnenie_sholarship(aspirant3),",чем у аспиранта №3")
print (" ")


print("Информация об аспиранте:")
aspirant3.disp_info()
print ("Стипендия аспиранта №3 -", aspirant3.sravnenie_sholarship(aspirant1),",чем у аспиранта №1")
print ("Стипендия аспиранта №3 -", aspirant3.sravnenie_sholarship(aspirant2),",чем у аспиранта №2")



