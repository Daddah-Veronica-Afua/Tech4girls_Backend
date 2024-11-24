-- Create the database
-- Setting Up aand Populating a Database 
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


-- Tech4Girls_DB database
-- Building Relationships
USE Tech4Girls_DB;

-- Create the Posts table
CREATE TABLE Posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

-- sample data into the Posts table
INSERT INTO Posts (user_id, title, content, created_at) VALUES
(1, 'Welcome to the World of Ama', 'This is the first post by Ama.', '2024-11-01 11:00:00'),
(2, 'Abena\'s Adventures', 'This is the first post by Abena.', '2024-11-02 12:30:00'),
(3, 'Adjoa\'s Journey', 'This is the first post by Adjoa.', '2024-11-03 15:00:00'),
(1, 'Ama\'s Second Post', 'This is another post by Ama.', '2024-11-01 13:00:00');


