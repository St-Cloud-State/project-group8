CREATE TABLE IF NOT EXISTS Courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    course_number_credits INTEGER NOT NULL,
    course_rubric TEXT NOT NULL,
    course_number INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Sections (
    section_id INTEGER PRIMARY KEY,
    section_semester TEXT NOT NULL,
    FOREIGN KEY (section_course_id) REFERENCES Courses (course_id),
    section_schedule TEXT NOT NULL,
    section_instructor TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Students (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT NOT NULL,
    student_address TEXT NOT NULL,
    student_email TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Registrations (
    registration_id INTEGER PRIMARY KEY,
    FOREIGN KEY (section_id) REFERENCES Sections (section_id),
    FOREIGN KEY (student_id) REFERENCES Students (student_id),
    registration_grade TEXT NOT NULL
);