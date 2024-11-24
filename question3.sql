-- Tech4Girls_DB database
CREATE DATABASE Tech4Girls_DB;

-- Use the database
USE Tech4Girls_DB;

-- Create the Users table
CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert the sample data into the Users table
INSERT INTO Users (username, email, created_at)
VALUES ('ama', 'ama@example.com', '2024-11-01 10:30:00'),
('Abena', 'Abena@example.com', '2024-11-02 12:00:00'),
('adjoa', 'adjoa@example.com', '2024-11-03 14:15:00');

-- Creating Many-to-Many Relationships
-- Create the Courses table
CREATE TABLE Courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL
);

-- Create the User_Courses table to establish a many-to-many relationship
CREATE TABLE User_Courses (
    user_id INT,
    course_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (course_id) REFERENCES Courses(id),
    PRIMARY KEY (user_id, course_id)
);

-- Insert sample data into the Courses table
INSERT INTO Courses (course_name)
VALUES ('Multimedia'),
('Data Structures'),
('Web Development');

-- Insert sample data into the User_Courses table
INSERT INTO User_Courses (user_id, course_id)
VALUES (1, 1), -- Ama enrolls in Multimedia
(1, 2), -- Ama enrolls in Data Structures
(2, 1), -- Abena enrolls in Multimedia
(2, 3), -- Abena enrolls in Web Development
(3, 3); -- Adjoa enrolls in Web Development
