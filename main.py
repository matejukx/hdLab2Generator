import datetime
import time

import generator as gen
from process import StartProcess

if __name__ == '__main__':

    start_time = datetime.date.fromisoformat("2015-01-01")
    end_time = datetime.date.fromisoformat("2020-01-01")

    start = time.perf_counter()
    start_process = StartProcess(start_time=start_time,
                                 end_time=end_time,
                                 number_of_students_per_request=100,
                                 student_iterations=100,
                                 number_of_instructors_per_request=50,
                                 instructor_iterations=10,
                                 number_of_lecturers=3)
    print("Starting to initialize people")
    start_process.initialize_people()
    ppl_finish_string = f"Initialization finished.\nCreated {len(start_process.students)} " \
                        f"students - that means we should have around " \
                        f"{len(start_process.students) / int((end_time - start_time).days / 30)} students per month.\n" \
                        f"We've also created {len(start_process.instructors)} instructors.\n" \
                        f"In {time.perf_counter() - start} seconds."
    print(ppl_finish_string)

    start = time.perf_counter()
    print('Starting to initialize activities - first month of students')
    start_process.create_activities(date_of_inclusion=start_time, hours_per_drive=4)
    print(f'Created {len(start_process.lectures)} lectures.\n'
          f'Created {len(start_process.drives)} drives.'
          f'\nIt took {time.perf_counter() - start} seconds to create activities for approx'
          f' \n {len(start_process.students) / int((end_time - start_time).days / 30)} students')

