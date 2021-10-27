import datetime
import random
import uuid

from dateutil import relativedelta

import generator
from entity.course import Course
from entity.metting import Meeting
from enums.employee_role import EmployeeRole
from enums.meeting_type import MeetingType


class Process:
    def __init__(self,
                 start_time,
                 end_time,
                 number_of_students,
                 number_of_instructors,
                 number_of_lecturers):

        self.students = []
        self.employees = []
        self.instructors = []
        self.lecturers = []

        self.courses = []
        self.lectures = []
        self.drives = []
        self.theoretical_exams = []
        self.practical_exams = []

        self.start_time = start_time
        self.end_time = end_time

        self.students_number = number_of_students
        self.instructors_number = number_of_instructors
        self.lecturers_number = number_of_lecturers

    def initialize_people(self):
        self.students = generator.generate_students(number_of_students=self.students_number,
                                                    start_date=self.start_time,
                                                    end_date=self.end_time)

        self.instructors = generator.generate_employees(number_of_employees=self.instructors_number,
                                                        role=EmployeeRole.PRACTICE_INSTRUCTOR,
                                                        start_date=self.start_time - datetime.timedelta(days=50),
                                                        end_date=self.start_time)

        self.lecturers = generator.generate_employees(number_of_employees=self.lecturers_number,
                                                      role=EmployeeRole.THEORY_INSTRUCTOR,
                                                      start_date=self.start_time - datetime.timedelta(days=50),
                                                      end_date=self.start_time
                                                      )

    def create_activities(self, date_of_inclusion, hours_per_drive):
        start_date = date_of_inclusion + relativedelta.relativedelta(months=1)
        current_date = start_date

        print(f'Collecting students from {date_of_inclusion} to {start_date}')
        current_students = filter(lambda student:
                                  start_date > student.begin_date >= date_of_inclusion,
                                  self.students)
        current_students = list(current_students)
        print(f'Collected {len(current_students)} for this month.')

        current_lecturer_index = random.randint(0, len(self.lecturers) - 1)
        current_lecturer = self.lecturers[current_lecturer_index]
        print(f'This month lecturer: {current_lecturer.pk_pesel} {current_lecturer.name} {current_lecturer.surname}')

        current_course = Course(course_id=uuid.uuid4(), employee_pesel=current_lecturer.pk_pesel)
        self.courses.append(current_course)

        print(f'Started creating lectures')
        for _ in range(15):
            self.lectures.append(
                Meeting(
                    meeting_id=uuid.uuid4(),
                    begin_date=start_date + relativedelta.relativedelta(hours=12),
                    end_date=start_date + relativedelta.relativedelta(hours=14),
                    meeting_type=MeetingType.THEORY,
                    students=current_students,
                    employee=current_lecturer,
                    course=current_course
                )
            )
            current_date += relativedelta.relativedelta(days=1)
            if current_date.strftime("%A") == 'Saturday':
                current_date += relativedelta.relativedelta(days=2)

            if current_date.strftime("%A") == 'Sunday':
                current_date += relativedelta.relativedelta(days=1)

        print(f'Lectures created!')

        # wygenerowac tutaj egzaminy teoretyczne wewnetrzne

        print(f'Started creating drives')

        students_needing_drives = filter(lambda student:
                                         student.drives_done < student.needed_drives and student.instructor is None,
                                         current_students)

        students_needing_drives = list(students_needing_drives)
        max_date = current_date
        current_meeting_hour = 8
        while len(students_needing_drives) > 0:
            starting_current_date = current_date
            # each instructor takes a student and we create all drives for them
            for instructor in self.instructors:
                if len(students_needing_drives) == 0:
                    continue
                student = students_needing_drives.pop()
                student.instructor = instructor

                while student.drives_done < student.needed_drives:
                    meeting_time = current_date + relativedelta.relativedelta(hours=current_meeting_hour)
                    drive = (
                        Meeting(
                            meeting_id=uuid.uuid4(),
                            begin_date=meeting_time,
                            end_date=meeting_time + relativedelta.relativedelta(hours=hours_per_drive),
                            meeting_type=MeetingType.PRACTICE,
                            students=None,
                            employee=instructor,
                            course=current_course
                        )
                    )
                    drive.student = student
                    self.drives.append(drive)
                    student.drives_done += hours_per_drive

                    current_date += relativedelta.relativedelta(days=1)
                    if current_date.strftime("%A") == 'Saturday':
                        current_date += relativedelta.relativedelta(days=2)

                    if current_date.strftime("%A") == 'Sunday':
                        current_date += relativedelta.relativedelta(days=1)

                    if current_date > max_date:
                        max_date = current_date
                current_date = starting_current_date

            current_meeting_hour += hours_per_drive
            if current_meeting_hour > 23:
                print("There are too many students for this amount of instructors!")
            current_date = starting_current_date

        print(f'Finished generating drives!')

        # tutaj generowanie egzaminow wewnetrznych praktycznych

        print(f'Finished generating activities.\n It took {(max_date - start_date).days} days'
              f' for all students from month: {date_of_inclusion} to finish their course')
