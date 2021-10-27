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
        self.end_date = None # this will be set after final exam

        # those should not be mapped anywhere
        self.lectures_done = 0
        self.drives_done = 0
        if self.gender == 'Non-binary' or self.gender == 'Female':
            self.additional_drives_factor = 1.5
        else:
            self.additional_drives_factor = 1
        self.needed_drives = int(random.randint(30, 35) * self.additional_drives_factor)
        if self.gender == 'Male' or self.gender == 'Agender':
            self.exam_factor = 0.8
        else:
            self.exam_factor = 1