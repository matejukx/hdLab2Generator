import generator

if __name__ == '__main__':
    gen = generator.Generator()

    gen.generate_students(10)
    for student in gen.students:
        print(
            str(student.pk_pesel),
            str(student.name),
            str(student.surname),
            str(student.date_of_birth),
            str(student.gender),
            str(student.phone_number),
            str(student.email),
            str(student.begin_date),
            str(student.end_date)
              )
