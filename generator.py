import datetime
import random

import requests

import enums.employee_role
from entity.employee import Employee
from entity.student import Student


class Generator:

    def __init__(self):
        self.students = []
        self.employees = []

    def generate_students(self, number_of_students):

        for _ in range(number_of_students):
            try:
                response = requests.get("https://random-data-api.com/api/users/random_user")
                random_student = response.json()

                self.students.append(
                    Student(
                        pk_pesel=random_student["social_insurance_number"] + "00",
                        name=random_student["first_name"],
                        surname=random_student["last_name"],
                        date_of_birth=random_student["date_of_birth"],
                        gender=random_student["gender"],
                        phone_number=random_student["phone_number"],
                        email=random_student["email"],
                        begin_date=datetime.date.today(),  # needs randomizing
                    )
                )
            except requests.exceptions.HTTPError as error:
                print(error)

    def generate_employees(self, number_of_employees):

        for _ in range(number_of_employees):
            try:
                response = requests.get("https://random-data-api.com/api/users/random_user")
                random_employee = response.json()
                self.employees.append(
                    Employee(
                        pk_pesel=random_employee["social_insurance_number"],
                        name=random_employee["first_name"],
                        surname=random_employee["last_name"],
                        date_of_birth=random_employee["date_of_birth"],
                        gender=random_employee["gender"],
                        phone_number=random_employee["phone_number"],
                        email=random_employee["email"],
                        employment_date=datetime.date.today(),  # needs randomizing
                        role=enums.employee_role.EmployeeRole.THEORY_INSTRUCTOR,  # needs randomizing
                        wage_per_hour=random.randrange(10, 13)
                    )
                )
            except requests.exceptions.HTTPError as error:
                print(error)
