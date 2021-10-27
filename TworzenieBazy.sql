CREATE DATABASE DrivingSchool9
GO

USE DrivingSchool9
GO

CREATE TABLE [Person]
(
	[PK_PESEL] VARCHAR(11) PRIMARY KEY,
	[Name] VARCHAR(100),
	[Surname] VARCHAR(100),
	[Gender] nvarchar(255) NOT NULL CHECK ([Gender] IN ('Male', 'Female', 'Other', 'Prefer_not_to_say')),
	[Phone_number] VARCHAR(100),
	[Email] VARCHAR(100)
)
GO

CREATE TABLE [Student] (
  [PK_PESEL] VARCHAR(11) UNIQUE FOREIGN KEY REFERENCES [Person],
  [Begin_date] date,
  [End_date] date
)
GO

CREATE TABLE [Employee] (
  [PK_PESEL] VARCHAR(11) UNIQUE FOREIGN KEY REFERENCES [Person],
  [Employment_date] date,
  [Role] nvarchar(255) NOT NULL,
  [Wage_per_hour] float
)
GO

CREATE TABLE [Course] (
  [PK_Id] uniqueidentifier PRIMARY KEY,
  [FK_Responsible_Employee_PESEL] VARCHAR(11) FOREIGN KEY REFERENCES [Employee] ([PK_PESEL])
)
GO

CREATE TABLE [Meeting] (
  [PK_Id] uniqueidentifier PRIMARY KEY,
  [Begin_date] datetime,
  [End_date] datetime,
  [Type] nvarchar(255) NOT NULL CHECK ([Type] IN ('Theory', 'Practice')),
  [FK_Employee_PESEL] VARCHAR(11) FOREIGN KEY REFERENCES [Employee] ([PK_PESEL]),
  [FK_Course_id] uniqueidentifier FOREIGN KEY REFERENCES [Course] ([PK_Id])
)
GO

CREATE TABLE [Participation] (
  [FK_Meeting_Id] uniqueidentifier FOREIGN KEY REFERENCES [Meeting] ([PK_Id]),
  [FK_Student_PESEL] VARCHAR(11) FOREIGN KEY REFERENCES [Student] ([PK_PESEL])
)
GO

CREATE TABLE [Exam] (
  [Attempt_number] integer,
  [Date] date,
  [Score] float,
  [Type] nvarchar(255) NOT NULL CHECK ([Type] IN ('Theory', 'Practice')),
  [FK_Student_PESEL] VARCHAR(11) FOREIGN KEY REFERENCES [Student] ([PK_PESEL]),
  [FK_Employee_PESEL] VARCHAR(11) FOREIGN KEY REFERENCES [Employee] ([PK_PESEL])
)
GO

