import datetime
import time

from dateutil import relativedelta

from data_raider import DataRaider
from process import Process

if __name__ == '__main__':

    start_time = datetime.date.fromisoformat("2015-01-01")
    end_time = datetime.date.fromisoformat("2020-01-01")

    start = time.perf_counter()
    process = Process(start_time=start_time,
                      end_time=end_time,
                      number_of_students=100,
                      number_of_instructors=300,
                      number_of_lecturers=3)
    print("Starting to initialize people")
    process.initialize_people()
    ppl_finish_string = f"Initialization finished.\nCreated {len(process.students)} " \
                        f"students - that means we should have around " \
                        f"{len(process.students) / int((end_time - start_time).days / 30)} students per month.\n" \
                        f"We've also created {len(process.instructors)} instructors.\n" \
                        f"In {time.perf_counter() - start} seconds."
    print(ppl_finish_string)

    start = time.perf_counter()
    print('Starting to initialize activities - half of the months')
    current_month = start_time
    # pierwsza czesc generowania T0-T1
    for _ in range(int((end_time - start_time).days / 30 / 2)):
        process.create_activities(date_of_inclusion=current_month, hours_per_drive=4)
        current_month += relativedelta.relativedelta(months=1)

    # przed zmiana zapisanie danych
    # people
    current_students = filter(lambda student: student.begin_date <= current_month,
                              process.students)
    current_students = list(current_students)
    with open('import/person_T1.bulk', 'w') as person_file:
        for student in current_students:
            person_file.write(student.to_csv_string_person())
        for lecturer in current_students:
            person_file.write(lecturer.to_csv_string_person())
        for instructor in current_students:
            person_file.write(instructor.to_csv_string_person())

    # students
    with open('import/student_T1.bulk', 'w') as student_file:
        for student in current_students:
            student_file.write(student.to_csv_string_student())

    # employees
    with open('import/employee_T1.bulk', 'w') as employee_file:
        for lecturer in process.lecturers:
            employee_file.write(lecturer.to_csv_string_employee())
        for instructor in process.instructors:
            employee_file.write(instructor.to_csv_string_employee())

    # meetings
    with open('import/meeting_T1.bulk', 'w') as meeting_file:
        for meeting in process.lectures:
            meeting_file.write(meeting.to_csv_string())
        for meeting in process.drives:
            meeting_file.write(meeting.to_csv_string())

    # participation
    with open('import/participation_T1.bulk', 'w') as participation_file:
        for meeting in process.lectures:
            participation_file.write(meeting.to_csv_string_participation())
        for meeting in process.drives:
            participation_file.write(meeting.to_csv_string_participation())

    # exams
    with open('import/exams_T1.bulk', 'w') as exam_file:
        for exam in process.theoretical_exams:
            exam_file.write(exam.to_csv_string())
        for exam in process.practical_exams:
            exam_file.write(exam.to_csv_string())


    # tutaj zmiana danych nastepuje w T1
    data_raider = DataRaider(process)
    data_raider.random_changes(15)


    # lecimy dalej z generowaniem T1-T2
    for _ in range(int((end_time - start_time).days / 30 / 2)):
        process.create_activities(date_of_inclusion=current_month, hours_per_drive=4)
        current_month += relativedelta.relativedelta(months=1)

    print(f'Created {len(process.lectures)} lectures.\n'
          f'Created {len(process.drives)} drives.'
          f'\nIt took {time.perf_counter() - start} seconds to create activities for all students')

    all_rows = len(process.students) + len(process.lectures) + len(process.instructors) + len(
        process.lectures) + len(process.drives) + len(process.courses)
    print(f'We created {all_rows} rows for our SQL database')

    # tutaj generowanie plików do importu SQL
    # people
    with open('import/person_T2.bulk', 'w') as person_file:
        for student in process.students:
            person_file.write(student.to_csv_string_person())
        for lecturer in process.lecturers:
            person_file.write(lecturer.to_csv_string_person())
        for instructor in process.instructors:
            person_file.write(instructor.to_csv_string_person())

    # students
    with open('import/student_T2.bulk', 'w') as student_file:
        for student in process.students:
            student_file.write(student.to_csv_string_student())

    # employees
    with open('import/employee_T2.bulk', 'w') as employee_file:
        for lecturer in process.lecturers:
            employee_file.write(lecturer.to_csv_string_employee())
        for instructor in process.instructors:
            employee_file.write(instructor.to_csv_string_employee())

    # courses
    with open('import/course_T2.bulk', 'w') as course_file:
        for course in process.courses:
            course_file.write(course.to_csv_string())

    # meetings
    with open('import/meeting_T2.bulk', 'w') as meeting_file:
        for meeting in process.lectures:
            meeting_file.write(meeting.to_csv_string())
        for meeting in process.drives:
            meeting_file.write(meeting.to_csv_string())

    # participation
    with open('import/participation_T2.bulk', 'w') as participation_file:
        for meeting in process.lectures:
            participation_file.write(meeting.to_csv_string_participation())
        for meeting in process.drives:
            participation_file.write(meeting.to_csv_string_participation())

    # exams
    with open('import/exam_T2.bulk', 'w') as exam_file:
        for exam in process.theoretical_exams:
            exam_file.write(exam.to_csv_string())
        for exam in process.practical_exams:
            exam_file.write(exam.to_csv_string())
