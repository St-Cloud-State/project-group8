CREATE TABLE IF NOT EXISTS Courses (
    Course_ID INTEGER PRIMARY KEY,
    Course_Name TEXT NOT NULL,
    Course_Number_Credits INTEGER NOT NULL,
    Course_Rubric TEXT NOT NULL,
    Course_Number INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Sections (
    Section_ID INTEGER PRIMARY KEY,
    Section_Semester TEXT NOT NULL,
    Section_Course_ID INTEGER NOT NULL,
    Section_Schedule TEXT NOT NULL,
    Section_Instructor TEXT NOT NULL,
    FOREIGN KEY (Section_Course_ID) REFERENCES Courses (Course_ID)
);

CREATE TABLE IF NOT EXISTS Students (
    Student_ID INTEGER PRIMARY KEY,
    Student_Name TEXT NOT NULL,
    Student_Address TEXT NOT NULL,
    Student_Email TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Registrations (
    Registration_ID INTEGER PRIMARY KEY,
    Registration_Section_ID INTEGER NOT NULL,
    Registration_Student_ID INTEGER NOT NULL,
    Registration_Grade TEXT NOT NULL,
    FOREIGN KEY (Registration_Section_ID) REFERENCES Sections (Section_ID),
    FOREIGN KEY (Registration_Student_ID) REFERENCES Students (Student_ID)
);