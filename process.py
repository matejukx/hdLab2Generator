import datetime
import random
import uuid

from dateutil import relativedelta

import generator
from entity.course import Course
from entity.metting import Meeting
from enums.employee_role import EmployeeRole
from enums.meeting_type import MeetingType


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

    def initialize_people(self):
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

    def create_activities(self, date_of_inclusion):
        start_date = date_of_inclusion + relativedelta.relativedelta(months=1)

        print(f'Collecting students from {date_of_inclusion} to {start_date}')
        current_students = filter(lambda student:
                                  start_date > student.begin_date >= date_of_inclusion,
                                  self.students)
        current_students = list(current_students)
        print(f'Collected {len(current_students)} for this month.')

        current_lecturer_index = random.randint(0, len(self.lecturers)-1)
        current_lecturer = self.lecturers[current_lecturer_index]
        print(f'This month lecturer: {current_lecturer.pk_pesel} {current_lecturer.name} {current_lecturer.surname}')

        current_course = Course(course_id=uuid.uuid4(), employee_pesel=current_lecturer.pk_pesel)
        self.courses.append(current_course)

        print(f'Started creating lectures')
        for _ in range(30):
            self.lectures.append(
                Meeting(
                    id=uuid.uuid4(),
                    begin_date=start_date + relativedelta.relativedelta(hours=12),
                    end_date=start_date + relativedelta.relativedelta(hours=14),
                    meeting_type=MeetingType.THEORY,
                    students=current_students,
                    employee=current_lecturer,
                    course=current_course
                )
            )
        print(f'Lectures created!')

        print(f'Started creating drives')

