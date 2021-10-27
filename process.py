import datetime

import generator
from enums.employee_role import EmployeeRole


class StartProcess:
    def __init__(self,
                 start_time,
                 end_time,
                 number_of_students_per_request,
                 student_iterations,
                 number_of_instructors_per_request,
                 instructor_iterations,
                 number_of_lecturers):

        self.students = []
        self.employees = []
        self.instructors = []
        self.lecturers = []

        self.courses = []
        self.lectures = []
        self.theoretical_exams = []
        self.practical_exams = []

        self.start_time = start_time
        self.end_time = end_time

        self.s_per_req = number_of_students_per_request
        self.i_per_req = number_of_instructors_per_request
        self.s_iterations = student_iterations
        self.i_iterations = instructor_iterations

        self.lecturers_number = number_of_lecturers

    def start(self):
        self.students = generator.generate_students(number_of_students_per_request=self.s_per_req,
                                                    iterations=self.s_iterations,
                                                    start_date=self.start_time,
                                                    end_date=self.end_time)

        self.instructors = generator.generate_employees(number_of_employees_per_request=self.i_per_req,
                                                        iterations=self.i_iterations,
                                                        role=EmployeeRole.PRACTICE_INSTRUCTOR,
                                                        start_date=self.start_time - datetime.timedelta(days=50),
                                                        end_date=self.start_time)

        self.lecturers = generator.generate_employees(number_of_employees_per_request=3,
                                                      iterations=1,
                                                      role=EmployeeRole.THEORY_INSTRUCTOR,
                                                      start_date=self.start_time - datetime.timedelta(days=50),
                                                      end_date=self.start_time
                                                      )
