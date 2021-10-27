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
        self.student = None,
        self.employee = employee,
        self.course = course
