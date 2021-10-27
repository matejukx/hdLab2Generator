from entity.person import Person


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
        self.wage_per_hour = wage_per_hour
        # those should not be mapped anywhere
        self.is_currently_busy = False

    def is_employed(self, current_date):
        return self.employment_date < current_date

    def to_csv_string_employee(self):
        return f'{self.employment_date},{self.role},{self.wage_per_hour}\n'

