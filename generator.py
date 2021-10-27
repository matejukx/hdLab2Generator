import datetime
import random

import faker
from faker.providers import person
from faker.providers import phone_number
from faker.providers import profile


from entity.employee import Employee
from entity.student import Student


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
                pk_pesel=random_profile['ssn'].replace('-', '') + '00',
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
                pk_pesel=random_profile['ssn'].replace('-', '') + '00',
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
