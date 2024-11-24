# Tech4Girls_DB Project

## Overview
This project demonstrates the creation and management of a database for a user registration system. It includes SQL scripts to create and populate tables and scripts for interacting with the database. The purpose is to showcase fundamental SQL concepts such as table creation, relationships, data insertion, and constraints.
Database, a structured or unstructured colection of data that a backend server uses to store and manage information efficiently.

## Scripts
## Question 1
### Database Creation Script
- **Filename**: `create_database.sql`
- **Purpose**: Creates the `Tech4Girls_DB` database and switches to using this database.
- **SQL Concepts Demonstrated**:
  - `CREATE DATABASE`: Creates a new database.
  - `USE`: Switches to the specified database for subsequent operations.

### Users Table Script
- **Filename**: `create_users_table.sql`
- **Purpose**: Creates the `Users` table with columns for user information.
- **SQL Concepts Demonstrated**:
  - `CREATE TABLE`: Creates a new table with specified columns and data types.
  - `PRIMARY KEY`: Sets a column as the unique identifier for table records.
  - `AUTO_INCREMENT`: Automatically generates a unique value for the primary key column.
  - `TIMESTAMP`: Records the date and time a row is inserted or updated.

### Sample Data Insertion Script for Users
- **Filename**: `insert_users_data.sql`
- **Purpose**: Inserts sample data into the `Users` table.
- **SQL Concepts Demonstrated**:
  - `INSERT INTO`: Adds new rows of data to a table.

## Question 2
### Posts Table Script
- **Filename**: `create_posts_table.sql`
- **Purpose**: Creates the `Posts` table to store blog post data and establish relationships with the `Users` table.
- **SQL Concepts Demonstrated**:
  - `FOREIGN KEY`: Establishes a relationship between tables.
  - `VARCHAR` and `TEXT`: Defines columns to store string data of varying lengths.

### Sample Data Insertion Script for Posts
- **Filename**: `insert_posts_data.sql`
- **Purpose**: Inserts sample data into the `Posts` table.
- **SQL Concepts Demonstrated**:
  - Establishes a one-to-many relationship between `Users` and `Posts`.

## Question 3
### Courses Table Script
- **Filename**: `create_courses_table.sql`
- **Purpose**: Creates the `Courses` table to store course information.
- **SQL Concepts Demonstrated**:
  - `VARCHAR`: Defines a column to store string data of a fixed length.

### User_Courses Table Script
- **Filename**: `create_user_courses_table.sql`
- **Purpose**: Creates the `User_Courses` table to manage many-to-many relationships between users and courses.
- **SQL Concepts Demonstrated**:
  - `PRIMARY KEY (user_id, course_id)`: Sets a composite primary key.
  - `FOREIGN KEY`: Links the table to the `Users` and `Courses` tables.

### Sample Data Insertion Script for Courses and User_Courses
- **Filename**: `insert_courses_user_courses_data.sql`
- **Purpose**: Inserts sample data into the `Courses` and `User_Courses` tables.
- **SQL Concepts Demonstrated**:
  - Demonstrates many-to-many relationships with data insertion.

## Conclusion
This project showcases various SQL concepts such as database creation, table creation, data types, primary and foreign keys, auto-increment columns, timestamps, and relationships between tables.


