# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючий студента.
# Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.
class Student:
    def __init__(self, first_name, last_name, age, middle_point):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.middle_point = middle_point

    def greet(self):
        print(f'Привіт, мене звати {self.first_name} {self.last_name}, мені {self.age} років, мій середній бал {self.middle_point}')

    def set_middle_point(self,new_middle_point):
        self.middle_point = new_middle_point

student1 = Student('Аліна', 'Вибиванець', 28, 100)
student1.greet()
student1.set_middle_point(95)
print(f'Мій новий бал {student1.middle_point}')