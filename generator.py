import csv
import datetime
import random

from dateutil import relativedelta

import const
import enums.exam_type

import faker
from faker.providers import person
from faker.providers import phone_number
from faker.providers import profile

from entity.employee import Employee
from entity.student import Student
from entity.assesment_form import AssesmentForm
from entity.exam_form import ExamForm
from enums.exam_type import ExamType

PESEL = 10000000000


def get_pesel():
    global PESEL
    PESEL += 1
    return str(PESEL)


def generate_employees(number_of_employees, role, start_date, end_date):
    employees = []
    fake = faker.Faker()
    fake.add_provider(person)
    fake.add_provider(phone_number)
    fake.add_provider(profile)

    for _ in range(number_of_employees):
        random_profile = fake.profile(['sex', 'mail', 'birthdate', 'ssn'])
        employees.append(
            Employee(
                pk_pesel=get_pesel(),
                name=fake.first_name(),
                surname=fake.last_name(),
                date_of_birth=random_profile['birthdate'],
                gender=random_profile['sex'],
                phone_number=fake.phone_number(),
                email=random_profile["mail"],
                employment_date=random_date(start_date, end_date),  # needs randomizing
                role=role,  # needs randomizing
                wage_per_hour=random.randrange(10, 13)
            )
        )
    return employees


def generate_students(number_of_students, start_date, end_date):
    students = []
    fake = faker.Faker()
    fake.add_provider(person)
    fake.add_provider(phone_number)
    fake.add_provider(profile)

    for _ in range(number_of_students):
        random_profile = fake.profile(['sex', 'mail', 'birthdate', 'ssn'])
        students.append(
            Student(
                pk_pesel=get_pesel(),
                name=fake.first_name(),
                surname=fake.last_name(),
                date_of_birth=random_profile['birthdate'],
                gender=random_profile['sex'],
                phone_number=fake.phone_number(),
                email=random_profile["mail"],
                begin_date=random_date(start_date, end_date),
            )
        )
    return students


def random_date(start, end):
    delta = end - start
    int_delta = delta.days
    random_day = random.randint(0, int_delta)
    return start + datetime.timedelta(days=random_day)


def generate_from_distribution(distribution):
    num = random.uniform(0, 1)
    sum_of_elements = 0
    for idx, elem in enumerate(distribution):
        sum_of_elements += distribution[idx]
        if num <= sum_of_elements:
            return idx


def generate_assesment_forms(students):
    with open(const.assesment_forms_filename, 'w', newline='') as csvfile:
        fieldnames = ['pesel', 'lecturer_rating', 'instructor_rating', 'course_rating']
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()
        for student in students:
            form = AssesmentForm(
                student,
                generate_from_distribution(const.assesment_lecturer_rating_distribution),
                generate_from_distribution(const.assesment_instruction_rating_distribution),
                generate_from_distribution(const.assesment_course_rating_distribution),
            )
            writer.writerow({
                fieldnames[0]: form.student.pk_pesel,
                fieldnames[1]: form.lecturer_rating,
                fieldnames[2]: form.instructor_rating,
                fieldnames[3]: form.course_rating,
            })
        csvfile.close()


def unpolishify(text):
    for p_letter, np_letter in const.unpolishify_dict.items():
        text = text.replace(p_letter, np_letter)
    return text


def generate_exam_forms(students, exam_type):
    with open(const.exam_forms_filename, 'w', newline='') as csvfile:
        fieldnames = ['pesel', 'exam_type', 'score', 'attempt_number', 'exam_date', 'city']
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()
        for student in students:
            if exam_type == ExamType.THEORY:
                exam_date = student.end_date + relativedelta.relativedelta(days=random.randint(1, 5))
            else:
                exam_date = student.passed_theory_date + relativedelta.relativedelta(days=random.randint(1, 5))
            score = 0
            attempts = 0
            city = unpolishify(random.choice(const.word_cities))
            while score < 75:
                attempts += 1
                score = random.randint(0, 100) * student.exam_factor
                form = ExamForm(
                    student=student,
                    exam_type=exam_type,
                    score=score,
                    attempt_number=attempts,
                    exam_date=exam_date,
                    city=city
                )

                if exam_type == ExamType.PRACTICE:
                    if score < 75:
                        form.score = 'not passed'
                    else:
                        form.score = 'passed'

                writer.writerow({
                    fieldnames[0]: form.student.pk_pesel,
                    fieldnames[1]: ExamType(form.exam_type).name,
                    fieldnames[2]: form.score,
                    fieldnames[3]: form.attempt_number,
                    fieldnames[4]: form.exam_date,
                    fieldnames[5]: form.city,
                })
                exam_date += relativedelta.relativedelta(days=random.randint(1, 5))
            if exam_type == ExamType.THEORY:
                student.passed_theory_date = exam_date
        csvfile.close()


def generate_exam_forms_theory(students):
    return generate_exam_forms(students, ExamType.THEORY)


def generate_exam_forms_practical(students):
    return generate_exam_forms(students, ExamType.PRACTICE)
