from entity.student import Student
from enums.meeting_type import MeetingType


class Meeting:

    def __init__(self,
                 meeting_id,
                 begin_date,
                 end_date,
                 meeting_type,
                 students,
                 employee,
                 course):
        self.meeting_id = meeting_id,
        self.begin_date = begin_date,
        self.end_date = end_date,
        self.meeting_type = meeting_type,
        if self.meeting_type == MeetingType.PRACTICE:
            self.meeting_type_string = "Practice"
        else:
            self.meeting_type_string = "Lecture"
        self.students = students,
        self.employee = employee,
        self.course = course

    def to_csv_string(self):
        return f'{self.meeting_id[0]},{self.begin_date[0]},{self.end_date[0]},{self.meeting_type_string},{self.employee[0].pk_pesel},{self.course.course_id}\n'

    def to_csv_string_participation(self):
        string = ''
        for student in self.students[0]:
            string += f'{self.meeting_id[0]},{student.pk_pesel}\n'
        return string
