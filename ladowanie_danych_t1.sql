use DrivingSchool9
GO
-- po T1
BULK INSERT dbo.Person
FROM 'C:\Users\mmatejuk\studia\hdLab2Generator\import\person_T1.bulk' 
WITH (FIELDTERMINATOR=',')

BULK INSERT dbo.Student
FROM 'C:\Users\mmatejuk\studia\hdLab2Generator\import\student_T1.bulk' 
WITH (FIELDTERMINATOR=',')

BULK INSERT dbo.Employee
FROM 'C:\Users\mmatejuk\studia\hdLab2Generator\import\employee_T1.bulk' 
WITH (FIELDTERMINATOR=',')

BULK INSERT dbo.Course
FROM 'C:\Users\mmatejuk\studia\hdLab2Generator\import\course_T1.bulk' 
WITH (FIELDTERMINATOR=',')

BULK INSERT dbo.Meeting
FROM 'C:\Users\mmatejuk\studia\hdLab2Generator\import\meeting_T1.bulk' 
WITH (FIELDTERMINATOR=',')

BULK INSERT dbo.Participation
FROM 'C:\Users\mmatejuk\studia\hdLab2Generator\import\participation_T1.bulk' 
WITH (FIELDTERMINATOR=',')

BULK INSERT dbo.Exam
FROM 'C:\Users\mmatejuk\studia\hdLab2Generator\import\exam_T1.bulk' 
WITH (FIELDTERMINATOR=',')
