import random
import faker
from faker.providers import person
from faker.providers import phone_number
from faker.providers import profile


class DataRaider:
    def __init__(self, process):
        self.process = process

    def random_changes(self, number_of_changes):
        fake = faker.Faker()
        fake.add_provider(person)
        fake.add_provider(phone_number)
        fake.add_provider(profile)

        for _ in range(number_of_changes):
            who_to_change = random.randint(0, 100)
            if who_to_change < 50:
                # we'll be changing employee
                who_to_change = random.randint(0, 100)
                if who_to_change < 50:
                    employee_index = random.randint(0, len(self.process.instructors)-1)
                    entity_object = self.process.instructors[employee_index]
                else:
                    employee_index = random.randint(0, len(self.process.lecturers) - 1)
                    entity_object = self.process.lecturers[employee_index]
            else:
                # we'll be changing student
                student_index = random.randint(0, len(self.process.students)-1)
                entity_object = self.process.students[student_index]

            with open('data_change_log.txt', 'a') as log:
                log.write(f'Before: {str(entity_object)}\n')

            what_do = random.randint(0,100)
            if what_do < 33:
                # we change gender
                if entity_object.gender == 'Male':
                    entity_object.gender = 'Female'
                    entity_object.name = fake.first_name_female()
                else:
                    entity_object.gender = 'Female'
                    entity_object.name = fake.first_name_male()
            elif 33 < what_do < 66:
                # we change surname
                entity_object.surname = fake.last_name()
            else:
                # we change phone number
                entity_object.phone_number = fake.phone_number()

            with open('data_change_log.txt', 'a') as log:
                log.write(f'After: {str(entity_object)}\n')
