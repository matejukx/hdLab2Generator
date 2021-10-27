import datetime
import time

import generator
from process import StartProcess

if __name__ == '__main__':
    gen = generator
    start_time = datetime.date.fromisoformat("2015-01-01")
    end_time = datetime.date.fromisoformat("2020-01-01")

    start = time.perf_counter()
    start_process = StartProcess(start_time=start_time,
                                 end_time=end_time,
                                 number_of_students_per_request=100,
                                 student_iterations=100,
                                 number_of_instructors_per_request=100,
                                 instructor_iterations=5,
                                 number_of_lecturers=3)
    print("Starting to initialize people")
    start_process.start()
    ppl_finish_string = f"Initialization finished.\nCreated {len(start_process.students)} " \
                        f"students - that means we have around " \
                        f"{len(start_process.students) / (end_time - start_time).days / 30} students per month.\n" \
                        f"We've also created {len(start_process.instructors)} instructors.\n" \
                        f"In {time.perf_counter() - start} seconds."
    print(ppl_finish_string)


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
