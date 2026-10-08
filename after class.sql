CREATE TABLE Students (
    ID INT,
    Name VARCHAR(50),
    Class INT,
    Marks INT
);

INSERT INTO Students (ID, Name, Class, Marks)
VALUES
(1, 'Rahul', 6, 85),
(2, 'Aman', 6, 72),
(3, 'Priya', 7, 91),
(4, 'Riya', 7, 65),
(5, 'Arjun', 6, 88);

SELECT * FROM Students;

SELECT * FROM Students
WHERE Marks > 80;


SELECT * FROM Students
WHERE Class = 6;

SELECT * FROM Students
WHERE Marks < 70;