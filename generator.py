import datetime
import random
import requests

from entity.employee import Employee
from entity.student import Student


def generate_employees(number_of_employees_per_request, iterations, role, start_date, end_date):
    employees = []
    if number_of_employees_per_request > 100 or number_of_employees_per_request < 1:
        print("Employees per request must be positive and less than 101!")
        return
    for _ in range(iterations):
        try:
            response = requests.get(
                "https://random-data-api.com/api/users/random_user?size=" + str(number_of_employees_per_request))
            random_employees = response.json()
            for random_employee in random_employees:
                employees.append(
                    Employee(
                        pk_pesel=random_employee["social_insurance_number"] + "00",
                        name=random_employee["first_name"],
                        surname=random_employee["last_name"],
                        date_of_birth=random_employee["date_of_birth"],
                        gender=random_employee["gender"],
                        phone_number=random_employee["phone_number"],
                        email=random_employee["email"],
                        employment_date=random_date(start_date, end_date),  # needs randomizing
                        role=role,  # needs randomizing
                        wage_per_hour=random.randrange(10, 13)
                    )
                )
        except requests.exceptions.HTTPError as error:
            print(error)
    return employees


def generate_students(number_of_students_per_request, iterations, start_date, end_date):
    students = []
    if number_of_students_per_request > 100 or number_of_students_per_request < 1:
        print("Students per request must be positive and less than 101!")
        return
    for _ in range(iterations):
        try:
            response = requests.get(
                "https://random-data-api.com/api/users/random_user?size=" + str(number_of_students_per_request))
            random_students = response.json()
            for random_student in random_students:
                students.append(
                    Student(
                        pk_pesel=random_student["social_insurance_number"] + "00",
                        name=random_student["first_name"],
                        surname=random_student["last_name"],
                        date_of_birth=random_student["date_of_birth"],
                        gender=random_student["gender"],
                        phone_number=random_student["phone_number"],
                        email=random_student["email"],
                        begin_date=random_date(start_date, end_date),  # needs randomizing
                    )
                )
        except requests.exceptions.HTTPError as error:
            print(error)
    return students


def random_date(start, end):
    delta = end - start
    int_delta = delta.days
    random_day = random.randint(0, int_delta)
    return start + datetime.timedelta(days=random_day)


