-- po T2
BULK INSERT dbo.Person
FROM 'C:\Users\mmatejuk\studia\hdLab2Generator\person_T2.bulk' 
WITH (FIELDTERMINATOR=',')

BULK INSERT dbo.Student
FROM 'C:\Users\mmatejuk\studia\hdLab2Generator\student_T2.bulk' 
WITH (FIELDTERMINATOR=',')

BULK INSERT dbo.Employee
FROM 'C:\Users\mmatejuk\studia\hdLab2Generator\employee_T2.bulk' 
WITH (FIELDTERMINATOR=',')

BULK INSERT dbo.Course
FROM 'C:\Users\mmatejuk\studia\hdLab2Generator\course_T2.bulk' 
WITH (FIELDTERMINATOR=',')

BULK INSERT dbo.Meeting
FROM 'C:\Users\mmatejuk\studia\hdLab2Generator\meeting_T2.bulk' 
WITH (FIELDTERMINATOR=',')

BULK INSERT dbo.Participation
FROM 'C:\Users\mmatejuk\studia\hdLab2Generator\participation_T2.bulk' 
WITH (FIELDTERMINATOR=',')

BULK INSERT dbo.Exam
FROM 'C:\Users\mmatejuk\studia\hdLab2Generator\exam_T2.bulk' 
WITH (FIELDTERMINATOR=',')