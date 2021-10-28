class Exam:

    def __init__(self,
                 attempt_number,
                 date,
                 city,
                 score,
                 exam_type,
                 student,
                 employee):

        self.attempt_number = attempt_number
        self.date = date
        self.city = city
        self.score = score
        self.exam_type = exam_type
        self.student = student
        self.employee = employee

        self.fk_pesel_student = self.student.pk_pesel
        self.fk_pesel_employee = self.employee.pk_pesel

    def to_csv_string(self):
        return f'{self.attempt_number},{self.date},{self.score},{self.exam_type},{self.fk_pesel_student},{self.fk_pesel_employee}\n'
