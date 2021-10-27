from entity.person import Person
from enums.employee_role import EmployeeRole


class Employee(Person):

    def __init__(self,
                 pk_pesel,
                 name,
                 surname,
                 date_of_birth,
                 gender,
                 phone_number,
                 email,
                 employment_date,
                 role,
                 wage_per_hour):

        super().__init__(pk_pesel,
                         name,
                         surname,
                         date_of_birth,
                         gender,
                         phone_number,
                         email)
        self.employment_date = employment_date
        self.role = role
        if self.role == EmployeeRole.PRACTICE_INSTRUCTOR:
            self.role_string = 'Instructor'
        else:
            self.role_string = 'Lecturer'
        self.wage_per_hour = wage_per_hour
        # those should not be mapped anywhere
        self.is_currently_busy = False

    def is_employed(self, current_date):
        return self.employment_date < current_date

    def to_csv_string_employee(self):
        return f'{self.pk_pesel},{self.employment_date},{self.role_string},{self.wage_per_hour}\n'

