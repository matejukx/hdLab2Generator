from entity.student import Student


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
        self.students = students,
        self.employee = employee,
        self.course = course

    def to_csv_string(self):
        return f'{self.meeting_id},{self.begin_date},{self.end_date},{self.meeting_type},{self.course.course_id}\n'

    def to_csv_string_participation(self):
        string = ''
        for student in self.students[0]:
            string += f'{self.meeting_id}, {student.pk_pesel}\n'
        return string
