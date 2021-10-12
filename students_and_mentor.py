class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, rate):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress and
                course in lecturer.courses_attached):
            if course in lecturer.rating:
                lecturer.rating[course] += [rate]
            else:
                lecturer.rating[course] = [rate]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Студент \nИмя: {self.name} \nФамилия: {self.surname}')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rating = {}

    def average_rate(self):
        rates_list = []
        for rate in self.rating.values():
            rates_list += rate
        average_rate = str(sum(rates_list) / len(rates_list))
        return average_rate

    def __str__(self):
        return (f'Лектор \nИмя: {self.name} \nФамилия: {self.surname}')
                #f'\nСредняя оценка за лекции: {self.average_rate()}\n')

best_student_1 = Student('Иванов', 'Иван', 'boy')
best_student_1.courses_in_progress += ['Python', 'Git']
best_student_2 = Student('Иванова', 'Ольга', 'girl')
best_student_2.courses_in_progress += ['Python']
best_student_2.finished_courses += ['Git']

lecturer_cool_mentor_3 = Lecturer('Марина', 'Петрова')
lecturer_cool_mentor_3.courses_attached += ['Python']
lecturer_cool_mentor_1 = Lecturer('Антон', 'Сидоров')
lecturer_cool_mentor_1.courses_attached += ['Git']

best_student_1.rate_lecturer(lecturer_cool_mentor_3, 'Python', 8)
best_student_1.rate_lecturer(lecturer_cool_mentor_1, 'Git', 6)
best_student_2.rate_lecturer(lecturer_cool_mentor_3, 'Python', 9)

print(best_student_1)
print(best_student_2)
print(lecturer_cool_mentor_3)
print(lecturer_cool_mentor_1)

