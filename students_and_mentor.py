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

    def average_grade(self):
        grades_list = []
        for grade in self.grades.values():
            grades_list += grade
        average_grade = str(sum(grades_list) / len(grades_list))
        return average_grade

    def __str__(self):
        return (f'Студент \nИмя: {self.name} \nФамилия: {self.surname}'
                  f'\nСредняя оценка за домашние задания: {self.average_grade()}')

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
        return (f'Лектор \nИмя: {self.name} \nФамилия: {self.surname}'
                f'\nСредняя оценка за лекции: {self.average_rate()}\n')

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Проверяющий \nИмя: {self.name} \nФамилия: {self.surname}\n'

best_student_1 = Student('Иванов', 'Иван', 'boy')
best_student_1.courses_in_progress += ['Python', 'Git']
best_student_2 = Student('Иванова', 'Ольга', 'girl')
best_student_2.courses_in_progress += ['Python']
best_student_2.finished_courses += ['Git']

reviewer_cool_mentor_2 = Reviewer('Анна', 'Сидорова')
reviewer_cool_mentor_2.courses_attached += ['Python']
reviewer_cool_mentor_1 = Reviewer('Антон', 'Сидоров')
reviewer_cool_mentor_1.courses_attached += ['Git']

lecturer_cool_mentor_3 = Lecturer('Марина', 'Петрова')
lecturer_cool_mentor_3.courses_attached += ['Python']
lecturer_cool_mentor_1 = Lecturer('Антон', 'Сидоров')
lecturer_cool_mentor_1.courses_attached += ['Git']

reviewer_cool_mentor_2.rate_hw(best_student_1, 'Python', 7)
reviewer_cool_mentor_1.rate_hw(best_student_1, 'Git', 6)
reviewer_cool_mentor_2.rate_hw(best_student_2, 'Python', 9)

best_student_1.rate_lecturer(lecturer_cool_mentor_3, 'Python', 8)
best_student_1.rate_lecturer(lecturer_cool_mentor_1, 'Git', 6)
best_student_2.rate_lecturer(lecturer_cool_mentor_3, 'Python', 9)

print(best_student_1)
print(best_student_2)
print(reviewer_cool_mentor_2)
print(reviewer_cool_mentor_1)
print(lecturer_cool_mentor_3)
print(lecturer_cool_mentor_1)

