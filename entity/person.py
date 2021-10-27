class Person:

    def __init__(self, 
                 pk_pesel,
                 name,
                 surname,
                 date_of_birth,
                 gender,
                 phone_number,
                 email):

        self.pk_pesel = pk_pesel
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        if gender == 'F':
            self.gender = 'Female'
        else:
            self.gender = 'Male'
        self.phone_number = phone_number
        self.email = email
