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
    section_course_id INTEGER NOT NULL,
    section_schedule TEXT NOT NULL,
    section_instructor TEXT NOT NULL,
    FOREIGN KEY (section_course_id) REFERENCES Courses (course_id)
);

CREATE TABLE IF NOT EXISTS Students (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT NOT NULL,
    student_address TEXT NOT NULL,
    student_email TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Registrations (
    registration_id INTEGER PRIMARY KEY,
    registration_section_id INTEGER NOT NULL,
    registration_student_id INTEGER NOT NULL,
    registration_grade TEXT NOT NULL,
    FOREIGN KEY (registration_section_id) REFERENCES Sections (section_id),
    FOREIGN KEY (registration_student_id) REFERENCES Students (student_id)
);