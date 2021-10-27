import time

import generator

if __name__ == '__main__':
    gen = generator.Generator()

    start = time.perf_counter()
    gen.generate_students(number_of_students_per_request=100, iterations=100)
    stop = time.perf_counter() - start
    print(stop)
    # for student in gen.students:
    #     print(
    #         str(student.pk_pesel),
    #         str(student.name),
    #         str(student.surname),
    #         str(student.date_of_birth),
    #         str(student.gender),
    #         str(student.phone_number),
    #         str(student.email),
    #         str(student.begin_date),
    #         str(student.end_date)
    #           )
