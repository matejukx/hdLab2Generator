class Exam:

    def __init__(self,
                 attempt_number,
                 date,
                 score,
                 exam_type,
                 student,
                 employee):

        self.attempt_number = attempt_number
        self.date = date
        self.score = score
        self.exam_type = exam_type
        self.student = student
        self.employee = employee

        self.fk_pesel_student = self.student.pk_pesel
        self.fk_pesel_employee = self.employee.pk_pesel
