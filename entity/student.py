from entity.person import Person
import random


class Student(Person):

    def __init__(self,
                 pk_pesel,
                 name,
                 surname,
                 date_of_birth,
                 gender,
                 phone_number,
                 email,
                 begin_date):

        super().__init__(pk_pesel,
                         name,
                         surname,
                         date_of_birth,
                         gender,
                         phone_number,
                         email)
        self.begin_date = begin_date
        self.end_date = None  # this will be set after final exam

        # those should not be mapped anywhere
        self.drives_done = 0
        if self.gender == 'Female':
            self.additional_drives_factor = 1.5
        else:
            self.additional_drives_factor = 1
        self.needed_drives = int(random.randint(30, 35) * self.additional_drives_factor)
        if self.gender == 'Male':
            self.exam_factor = 0.95
        else:
            self.exam_factor = 1

        self.instructor = None
        self.lecturer = None

    def to_csv_string_person(self):
        return f'{self.pk_pesel},{self.name},{self.surname},{self.gender},{self.phone_number},{self.email}\n'

    def to_csv_string_student(self):
        return f'{self.pk_pesel},{self.begin_date},{self.end_date}\n'
