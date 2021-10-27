class Course:

    def __init__(self,
                 course_id,
                 employee_pesel):
        self.course_id = course_id
        self.employee_pesel = employee_pesel

    def to_csv_string(self):
        return f'{self.course_id},{self.employee_pesel}\n'

